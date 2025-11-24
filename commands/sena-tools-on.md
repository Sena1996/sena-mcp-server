# SENA Tool Permissions - Enable Tool

Enable a specific Claude Code tool or all tools at runtime.

**Usage:**
- `/sena-tools-on Edit` - Enable Edit tool
- `/sena-tools-on all` - Enable all tools

**Execute this Python code:**

```python
import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

from tool_permission_manager import get_tool_permission_manager
from v3.ui.terminal_ui import TerminalUI as UI

# Get tool name from user (will be provided as argument)
# For now, you'll need to modify the tool name in the code below

# INSTRUCTION: Replace 'Edit' with the tool you want to enable, or 'all' for all tools
TOOL_NAME = input("Enter tool name to enable (or 'all' for all tools): ").strip()

tpm = get_tool_permission_manager()

print("\n" + UI.header(
    "SENA 🦁 ENABLE TOOL PERMISSION",
    f"Enabling: {TOOL_NAME}",
    width=90
))

if TOOL_NAME.lower() == 'all':
    # Enable all tools
    success = tpm.enable_all_tools()
    if success:
        print("\n✅ SUCCESS: All tools enabled")
        print("   • Changes apply immediately")
        print("   • No restart required")
    else:
        print("\n❌ ERROR: Failed to enable all tools")
else:
    # Enable specific tool
    if TOOL_NAME in tpm.AVAILABLE_TOOLS:
        success = tpm.enable_tool(TOOL_NAME)
        if success:
            print(f"\n✅ SUCCESS: {TOOL_NAME} tool enabled")
            print("   • Changes apply immediately")
            print("   • No restart required")
            print(f"   • Hook will now allow {TOOL_NAME} operations")
        else:
            print(f"\n❌ ERROR: Failed to enable {TOOL_NAME}")
    else:
        print(f"\n❌ ERROR: Unknown tool '{TOOL_NAME}'")
        print("\n📋 Available tools:")
        for tool in tpm.AVAILABLE_TOOLS:
            print(f"   • {tool}")

print("\n" + UI.DOUBLE_HORIZONTAL * 90)
print("\n💡 Run /sena-tools-status to see current permissions")
print(UI.DOUBLE_HORIZONTAL * 90 + "\n")
```

**Quick Examples:**

Enable Edit tool:
```python
import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')
from tool_permission_manager import get_tool_permission_manager
tpm = get_tool_permission_manager()
tpm.enable_tool('Edit')
print("✅ Edit tool enabled")
```

Enable all tools:
```python
import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')
from tool_permission_manager import get_tool_permission_manager
tpm = get_tool_permission_manager()
tpm.enable_all_tools()
print("✅ All tools enabled")
```
