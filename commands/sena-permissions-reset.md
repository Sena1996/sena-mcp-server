# Reset All SENA Permissions

Clear all saved permission preferences and start fresh.

**Execute this Python code:**

```python
import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

from permission_manager import get_permission_manager
from v3.ui.terminal_ui import TerminalUI as UI

pm = get_permission_manager()

# Get count before clearing
count = len(pm.get_all_permissions())

# Clear all permissions
success = pm.clear_all()

if success:
    print("\n" + UI.header(
        "SENA 🦁 PERMISSIONS RESET",
        "All Preferences Cleared",
        width=80
    ))

    print(f"\n  ✅ Successfully cleared {count} saved permissions")
    print("  ✅ Permission preference system has been reset")
    print("\n  All future questions will be asked again (first-time prompts)")
    print("\n" + UI.DOUBLE_HORIZONTAL * 80 + "\n")
else:
    print("\n❌ Error: Could not reset permissions\n")
```

This will clear all your saved permission preferences.
