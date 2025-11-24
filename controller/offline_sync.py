"""
Offline-First Architecture - Innovation 20
100% offline functionality with local-first data and conflict-free sync
"""

from typing import Dict, Any, List, Optional, Set
from pathlib import Path
from threading import RLock
from datetime import datetime, timedelta
from dataclasses import dataclass, field
import json
import hashlib
import time

from base.component import BaseComponent


@dataclass
class Change:
    """Represents a data change"""
    id: str
    timestamp: float
    operation: str  # create, update, delete
    collection: str
    key: str
    value: Any
    author: str
    vector_clock: Dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'operation': self.operation,
            'collection': self.collection,
            'key': self.key,
            'value': self.value,
            'author': self.author,
            'vector_clock': self.vector_clock,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Change':
        return cls(**data)


class CRDT:
    """
    Conflict-Free Replicated Data Type

    Last-Write-Wins Register implementation
    """

    def __init__(self, author_id: str):
        self.author_id = author_id
        self.data: Dict[str, Any] = {}
        self.vector_clock: Dict[str, int] = {author_id: 0}
        self.tombstones: Set[str] = set()  # Track deletions

    def set(self, key: str, value: Any) -> Change:
        """Set a value"""
        self.vector_clock[self.author_id] = self.vector_clock.get(self.author_id, 0) + 1

        if key in self.tombstones:
            self.tombstones.remove(key)

        self.data[key] = {
            'value': value,
            'timestamp': time.time(),
            'vector_clock': self.vector_clock.copy(),
        }

        return Change(
            id=self._generate_change_id(),
            timestamp=time.time(),
            operation='update',
            collection='default',
            key=key,
            value=value,
            author=self.author_id,
            vector_clock=self.vector_clock.copy(),
        )

    def get(self, key: str) -> Optional[Any]:
        """Get a value"""
        if key in self.tombstones:
            return None

        if key in self.data:
            return self.data[key]['value']

        return None

    def delete(self, key: str) -> Change:
        """Delete a value"""
        self.vector_clock[self.author_id] = self.vector_clock.get(self.author_id, 0) + 1

        if key in self.data:
            del self.data[key]

        self.tombstones.add(key)

        return Change(
            id=self._generate_change_id(),
            timestamp=time.time(),
            operation='delete',
            collection='default',
            key=key,
            value=None,
            author=self.author_id,
            vector_clock=self.vector_clock.copy(),
        )

    def merge(self, change: Change) -> bool:
        """
        Merge a change from another replica

        Returns:
            True if change was applied
        """
        # Update vector clock
        for author, clock in change.vector_clock.items():
            self.vector_clock[author] = max(
                self.vector_clock.get(author, 0),
                clock
            )

        # Handle operation
        if change.operation == 'delete':
            self.tombstones.add(change.key)
            if change.key in self.data:
                del self.data[change.key]
            return True

        elif change.operation in ('create', 'update'):
            # Check if we should apply this change
            if change.key in self.tombstones:
                # Already deleted, check if this is newer
                pass

            if change.key not in self.data:
                # New key, apply change
                self.data[change.key] = {
                    'value': change.value,
                    'timestamp': change.timestamp,
                    'vector_clock': change.vector_clock.copy(),
                }
                return True

            # Conflict resolution: Last-Write-Wins
            existing = self.data[change.key]

            if change.timestamp > existing['timestamp']:
                # Newer timestamp wins
                self.data[change.key] = {
                    'value': change.value,
                    'timestamp': change.timestamp,
                    'vector_clock': change.vector_clock.copy(),
                }
                return True

            elif change.timestamp == existing['timestamp']:
                # Same timestamp, use author ID as tiebreaker
                if change.author > self.author_id:
                    self.data[change.key] = {
                        'value': change.value,
                        'timestamp': change.timestamp,
                        'vector_clock': change.vector_clock.copy(),
                    }
                    return True

        return False

    def _generate_change_id(self) -> str:
        """Generate unique change ID"""
        data = f"{self.author_id}{time.time()}{id(object())}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]


class OfflineSync(BaseComponent):
    """
    Offline-First Synchronization Engine

    Features:
    - 100% offline functionality
    - Local-first data storage
    - CRDT-based conflict resolution
    - Automatic sync when online
    - Change log for sync
    - Multi-device support

    Architecture:
    - Local storage (primary)
    - Change log (append-only)
    - Sync queue (when online)
    - Vector clocks (causality)

    Usage:
        sync = OfflineSync(author_id="sena-laptop")

        # Write data (works offline)
        sync.set("user.preferences", {"theme": "dark"})

        # Read data (works offline)
        value = sync.get("user.preferences")

        # Sync with remote (when online)
        changes = sync.get_pending_changes()
        # ... send to remote
        remote_changes = # ... receive from remote
        sync.apply_remote_changes(remote_changes)
    """

    def __init__(self, author_id: Optional[str] = None):
        super().__init__("OfflineSync")

        self._lock = RLock()

        # Author ID (device/user identifier)
        self._author_id = author_id or self._generate_author_id()

        # CRDT storage
        self._crdt = CRDT(self._author_id)

        # Change log (append-only)
        self._change_log: List[Change] = []

        # Sync state
        self._last_sync: Optional[datetime] = None
        self._sync_in_progress = False
        self._pending_changes: List[Change] = []

        # Configuration
        self._config = {
            'auto_sync': False,
            'sync_interval_seconds': 300,  # 5 minutes
            'max_change_log_size': 10000,
        }

        # Storage
        self._storage_dir = Path.home() / '.claude' / 'data' / 'offline'
        self._storage_dir.mkdir(parents=True, exist_ok=True)

        self._data_file = self._storage_dir / 'local_data.json'
        self._change_log_file = self._storage_dir / 'change_log.jsonl'

        # Metrics
        self._metrics = {
            'writes': 0,
            'reads': 0,
            'syncs': 0,
            'conflicts_resolved': 0,
            'changes_applied': 0,
        }

    def initialize(self) -> None:
        """Initialize offline sync"""
        with self._lock:
            self._load_local_data()
            self._load_change_log()

    def set(self, key: str, value: Any) -> None:
        """
        Set a value (works offline)

        Args:
            key: Data key (e.g., "user.preferences")
            value: Value to store
        """
        with self._lock:
            change = self._crdt.set(key, value)

            # Add to change log
            self._change_log.append(change)
            self._pending_changes.append(change)

            # Persist
            self._save_local_data()
            self._append_to_change_log(change)

            self._metrics['writes'] += 1

    def get(self, key: str) -> Optional[Any]:
        """
        Get a value (works offline)

        Args:
            key: Data key

        Returns:
            Value or None
        """
        with self._lock:
            self._metrics['reads'] += 1
            return self._crdt.get(key)

    def delete(self, key: str) -> None:
        """Delete a value (works offline)"""
        with self._lock:
            change = self._crdt.delete(key)

            # Add to change log
            self._change_log.append(change)
            self._pending_changes.append(change)

            # Persist
            self._save_local_data()
            self._append_to_change_log(change)

            self._metrics['writes'] += 1

    def get_all(self) -> Dict[str, Any]:
        """Get all data"""
        with self._lock:
            result = {}
            for key in self._crdt.data:
                if key not in self._crdt.tombstones:
                    result[key] = self._crdt.data[key]['value']
            return result

    def get_pending_changes(self) -> List[Dict[str, Any]]:
        """
        Get changes pending sync

        Returns:
            List of changes to sync to remote
        """
        with self._lock:
            return [change.to_dict() for change in self._pending_changes]

    def apply_remote_changes(self, remote_changes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Apply changes from remote

        Args:
            remote_changes: List of changes from remote

        Returns:
            Sync result statistics
        """
        with self._lock:
            applied = 0
            conflicts = 0

            for change_data in remote_changes:
                change = Change.from_dict(change_data)

                # Try to merge
                was_applied = self._crdt.merge(change)

                if was_applied:
                    applied += 1
                    self._metrics['changes_applied'] += 1

                    # Add to change log
                    self._change_log.append(change)
                else:
                    conflicts += 1
                    self._metrics['conflicts_resolved'] += 1

            # Persist if any changes applied
            if applied > 0:
                self._save_local_data()

            # Clear pending changes (they've been synced)
            self._pending_changes.clear()
            self._last_sync = datetime.now()
            self._metrics['syncs'] += 1

            return {
                'applied': applied,
                'conflicts': conflicts,
                'total': len(remote_changes),
            }

    def is_online(self) -> bool:
        """Check if online (placeholder - will integrate with network check)"""
        # For now, assume always offline
        return False

    def needs_sync(self) -> bool:
        """Check if sync is needed"""
        with self._lock:
            if not self._pending_changes:
                return False

            if not self._last_sync:
                return True

            interval = timedelta(seconds=self._config['sync_interval_seconds'])
            return datetime.now() - self._last_sync > interval

    def get_sync_status(self) -> Dict[str, Any]:
        """Get sync status"""
        with self._lock:
            return {
                'author_id': self._author_id,
                'last_sync': self._last_sync.isoformat() if self._last_sync else None,
                'pending_changes': len(self._pending_changes),
                'sync_in_progress': self._sync_in_progress,
                'online': self.is_online(),
                'needs_sync': self.needs_sync(),
            }

    def get_stats(self) -> Dict[str, Any]:
        """Get offline sync statistics"""
        with self._lock:
            return {
                'author_id': self._author_id,
                'total_changes': len(self._change_log),
                'pending_changes': len(self._pending_changes),
                'total_keys': len(self._crdt.data),
                'tombstones': len(self._crdt.tombstones),
                'last_sync': self._last_sync.isoformat() if self._last_sync else None,
                **self._metrics,
            }

    def get_status(self) -> Dict[str, Any]:
        """Get offline sync status"""
        return self.get_stats()

    def _generate_author_id(self) -> str:
        """Generate unique author ID"""
        import socket
        hostname = socket.gethostname()
        return f"{hostname}-{int(time.time())}"

    def _load_local_data(self):
        """Load local data from disk"""
        try:
            if self._data_file.exists():
                with open(self._data_file, 'r') as f:
                    data = json.load(f)

                self._crdt.data = data.get('data', {})
                self._crdt.vector_clock = data.get('vector_clock', {self._author_id: 0})
                self._crdt.tombstones = set(data.get('tombstones', []))

        except Exception:
            pass

    def _save_local_data(self):
        """Save local data to disk"""
        try:
            data = {
                'version': '3.0.0',
                'author_id': self._author_id,
                'data': self._crdt.data,
                'vector_clock': self._crdt.vector_clock,
                'tombstones': list(self._crdt.tombstones),
                'last_updated': datetime.now().isoformat(),
            }

            # Atomic write
            temp_file = self._data_file.with_suffix('.tmp')
            with open(temp_file, 'w') as f:
                json.dump(data, f, indent=2)

            temp_file.replace(self._data_file)

        except Exception:
            pass

    def _load_change_log(self):
        """Load change log from disk"""
        try:
            if self._change_log_file.exists():
                with open(self._change_log_file, 'r') as f:
                    for line in f:
                        if line.strip():
                            change_data = json.loads(line)
                            change = Change.from_dict(change_data)
                            self._change_log.append(change)

        except Exception:
            pass

    def _append_to_change_log(self, change: Change):
        """Append change to change log file"""
        try:
            with open(self._change_log_file, 'a') as f:
                f.write(json.dumps(change.to_dict()) + '\n')

        except Exception:
            pass

    def cleanup(self) -> None:
        """Cleanup - save all data"""
        with self._lock:
            self._save_local_data()
