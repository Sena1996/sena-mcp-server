# Export SENA Permissions

Export all your permission preferences to a backup file.

**Execute this Python code:**

```python
import sys
from pathlib import Path
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

from permission_manager import get_permission_manager
from v3.ui.terminal_ui import TerminalUI as UI

pm = get_permission_manager()

# Export to home directory
export_path = str(Path.home() / 'sena_permissions_backup.json')

success = pm.export_permissions(export_path)

if success:
    print("\n" + UI.header(
        "SENA 🦁 PERMISSIONS EXPORTED",
        "Backup Created Successfully",
        width=80
    ))

    print(f"\n  ✅ Permissions exported to:")
    print(f"     {export_path}")
    print(f"\n  📦 Total permissions: {len(pm.get_all_permissions())}")
    print("\n  You can import this file later with /sena-permissions-import")
    print("\n" + UI.DOUBLE_HORIZONTAL * 80 + "\n")
else:
    print("\n❌ Error: Could not export permissions\n")
```

This will create a backup file in your home directory.
