#!/usr/bin/env python3
"""
SENA Controller v3.3 - Multi-Session Coordination Activator
Enables session persistence, state management, and multi-instance coordination
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

# Import session components
from session_manager import SessionManager
from offline_sync import OfflineSync


class SENASessionCoordinator:
    """
    Master coordinator for multi-session capabilities in SENA v3.3
    """

    def __init__(self):
        self.session_manager = SessionManager()
        self.offline_sync = OfflineSync()
        self.initialized = False
        self.config_path = Path.home() / '.claude' / 'sena_session_config.json'

    def initialize(self) -> bool:
        """Initialize session coordination system"""
        try:
            print("🦁 SENA Session Coordinator - Initializing...")

            # Initialize session manager
            self.session_manager.initialize()
            print("  ✅ Session Manager initialized")

            # Initialize offline sync
            self.offline_sync.initialize()
            print("  ✅ Offline Sync initialized")

            # Load or create config
            self._load_config()
            print("  ✅ Configuration loaded")

            self.initialized = True
            print("🦁 Session Coordination ACTIVE\n")
            return True

        except Exception as e:
            print(f"  ❌ Initialization failed: {e}")
            return False

    def _load_config(self):
        """Load or create session configuration"""
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                'multi_session_enabled': True,
                'max_sessions': 50,
                'sync_enabled': True,
                'auto_restore': True,
                'created_at': datetime.now().isoformat()
            }
            self._save_config()

    def _save_config(self):
        """Save configuration"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)

    def get_current_session(self):
        """Get current session state"""
        return self.session_manager.get_current_session()

    def save_command(self, command: str, result: Any = None):
        """Record command in session history"""
        self.session_manager.record_command(command, result)

    def get_session_status(self) -> Dict[str, Any]:
        """Get comprehensive session status"""
        current = self.session_manager.get_current_session()

        if current:
            return {
                'active': True,
                'session_id': current.session_id,
                'started_at': current.started_at.isoformat(),
                'commands_executed': current.commands_executed,
                'last_command': current.last_command,
                'working_directory': current.working_directory,
                'preferences': current.preferences
            }
        else:
            return {'active': False}

    def get_sync_status(self) -> Dict[str, Any]:
        """Get sync status"""
        return self.offline_sync.get_status()

    def restore_last_session(self) -> bool:
        """Attempt to restore previous session"""
        last_session = self.session_manager.get_last_session()
        if last_session:
            print(f"🦁 Restoring session {last_session.session_id[:8]}...")
            print(f"  Last command: {last_session.last_command}")
            print(f"  Commands executed: {last_session.commands_executed}")
            return True
        return False

    def enable_global_preference(self, key: str, value: Any):
        """Set a global preference that persists across sessions"""
        self.session_manager.set_preference(key, value, persist=True)

    def get_global_preferences(self) -> Dict[str, Any]:
        """Get all global preferences"""
        return self.session_manager._global_preferences

    def display_status(self):
        """Display beautiful status output"""
        print("\n" + "╔" + "="*68 + "╗")
        print("║" + " "*68 + "║")
        print("║" + "  SENA MULTI-SESSION COORDINATION STATUS".center(68) + "║")
        print("║" + " "*68 + "║")
        print("╚" + "="*68 + "╝\n")

        session_status = self.get_session_status()
        sync_status = self.get_sync_status()

        print("┌─ SESSION STATE " + "─"*52 + "┐")
        if session_status['active']:
            print(f"│  Status: ACTIVE" + " "*52 + "│")
            print(f"│  Session ID: {session_status['session_id'][:16]}..." + " "*31 + "│")
            print(f"│  Commands: {session_status['commands_executed']:<56} │")
            if session_status['last_command']:
                cmd = session_status['last_command'][:40] + "..." if len(session_status['last_command']) > 40 else session_status['last_command']
                print(f"│  Last: {cmd:<60} │")
        else:
            print(f"│  Status: NO ACTIVE SESSION" + " "*40 + "│")
        print("└" + "─"*68 + "┘\n")

        print("┌─ SYNCHRONIZATION " + "─"*50 + "┐")
        print(f"│  Offline Mode: {sync_status.get('offline_mode', 'ENABLED'):<52} │")
        print(f"│  Changes Pending: {sync_status.get('pending_changes', 0):<50} │")
        last_sync = sync_status.get('last_sync', 'Never') if sync_status.get('last_sync') else 'Never'
        print(f"│  Last Sync: {last_sync:<56} │")
        print("└" + "─"*68 + "┘\n")

        print("┌─ GLOBAL PREFERENCES " + "─"*47 + "┐")
        prefs = self.get_global_preferences()
        if prefs:
            for key, value in list(prefs.items())[:3]:
                print(f"│  {key}: {str(value)[:50]:<50} │")
        else:
            print(f"│  No global preferences set" + " "*40 + "│")
        print("└" + "─"*68 + "┘")


# Global instance
session_coordinator = None

def get_session_coordinator():
    """Get or create session coordinator instance"""
    global session_coordinator
    if session_coordinator is None:
        session_coordinator = SENASessionCoordinator()
        session_coordinator.initialize()
    return session_coordinator


def enable_session_coordination():
    """Enable multi-session coordination for SENA v3.3"""
    coordinator = get_session_coordinator()
    coordinator.display_status()
    return coordinator


if __name__ == "__main__":
    # Test session coordination
    print("Testing SENA Multi-Session Coordination...")

    coordinator = enable_session_coordination()

    # Test recording a command
    coordinator.save_command("test command", {"result": "success"})

    # Test setting global preference
    coordinator.enable_global_preference("test_pref", "test_value")

    # Show updated status
    print("\n" + "="*70)
    print("After test operations:")
    coordinator.display_status()

    print("\n✅ Multi-Session Coordination is ACTIVE!")