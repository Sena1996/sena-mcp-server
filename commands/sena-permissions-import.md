# Import SENA Permissions

Import permission preferences from a backup file.

**Execute this Python code:**

```python
import sys
from pathlib import Path
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

from permission_manager import get_permission_manager
from v3.ui.terminal_ui import TerminalUI as UI

pm = get_permission_manager()

# Import from home directory (default backup location)
import_path = str(Path.home() / 'sena_permissions_backup.json')

# You can change merge to True to merge with existing permissions
success = pm.import_permissions(import_path, merge=False)

if success:
    print("\n" + UI.header(
        "SENA 🦁 PERMISSIONS IMPORTED",
        "Backup Restored Successfully",
        width=80
    ))

    print(f"\n  ✅ Permissions imported from:")
    print(f"     {import_path}")
    print(f"\n  📦 Total permissions: {len(pm.get_all_permissions())}")
    print("\n  Run /sena-permissions to view all imported preferences")
    print("\n" + UI.DOUBLE_HORIZONTAL * 80 + "\n")
else:
    print("\n❌ Error: Could not import permissions")
    print(f"   Make sure the file exists at: {import_path}\n")
```

This will restore your permissions from the backup file.
