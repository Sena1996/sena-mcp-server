# Toggle SENA Permission Auto-Apply

Toggle auto-apply for a specific permission.

**Please provide the permission ID to toggle.**

Then execute this Python code:

```python
import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

from permission_manager import get_permission_manager

pm = get_permission_manager()

# Replace with actual permission ID
permission_id = "YOUR_PERMISSION_ID_HERE"

if pm.has_permission(permission_id):
    new_state = pm.toggle_auto_apply(permission_id)
    status = "✅ ENABLED" if new_state else "❌ DISABLED"
    print(f"\nPermission: {permission_id}")
    print(f"Auto-Apply: {status}\n")
else:
    print(f"\n❌ Permission '{permission_id}' not found\n")
    print("Run /sena-permissions to see all available permissions.\n")
```

Example usage:
- To toggle "delete_temp_files" permission, replace YOUR_PERMISSION_ID_HERE with delete_temp_files
