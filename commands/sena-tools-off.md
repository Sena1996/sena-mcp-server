# SENA Tool Permissions - Disable Tool

Disable a specific Claude Code tool or all tools at runtime.

**Usage:**
- `/sena-tools-off Edit` - Disable Edit tool
- `/sena-tools-off all` - Disable all tools

**Execute this Python code:**

```python
import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

from tool_permission_manager import get_tool_permission_manager
from v3.ui.terminal_ui import TerminalUI as UI

# Get tool name from user (will be provided as argument)
# For now, you'll need to modify the tool name in the code below

# INSTRUCTION: Replace 'Edit' with the tool you want to disable, or 'all' for all tools
TOOL_NAME = input("Enter tool name to disable (or 'all' for all tools): ").strip()

tpm = get_tool_permission_manager()

print("\n" + UI.header(
    "SENA 🦁 DISABLE TOOL PERMISSION",
    f"Disabling: {TOOL_NAME}",
    width=90
))

if TOOL_NAME.lower() == 'all':
    # Disable all tools
    success = tpm.disable_all_tools()
    if success:
        print("\n⚠️  WARNING: All tools disabled")
        print("   • Changes apply immediately")
        print("   • No restart required")
        print("   • You may need to re-enable tools to continue working")
    else:
        print("\n❌ ERROR: Failed to disable all tools")
else:
    # Disable specific tool
    if TOOL_NAME in tpm.AVAILABLE_TOOLS:
        success = tpm.disable_tool(TOOL_NAME)
        if success:
            print(f"\n✅ SUCCESS: {TOOL_NAME} tool disabled")
            print("   • Changes apply immediately")
            print("   • No restart required")
            print(f"   • Hook will now deny {TOOL_NAME} operations")
        else:
            print(f"\n❌ ERROR: Failed to disable {TOOL_NAME}")
    else:
        print(f"\n❌ ERROR: Unknown tool '{TOOL_NAME}'")
        print("\n📋 Available tools:")
        for tool in tpm.AVAILABLE_TOOLS:
            print(f"   • {tool}")

print("\n" + UI.DOUBLE_HORIZONTAL * 90)
print("\n💡 Run /sena-tools-status to see current permissions")
print("💡 Run /sena-tools-on to re-enable tools")
print(UI.DOUBLE_HORIZONTAL * 90 + "\n")
```

**Quick Examples:**

Disable Edit tool:
```python
import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')
from tool_permission_manager import get_tool_permission_manager
tpm = get_tool_permission_manager()
tpm.disable_tool('Edit')
print("✅ Edit tool disabled")
```

Disable all tools:
```python
import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')
from tool_permission_manager import get_tool_permission_manager
tpm = get_tool_permission_manager()
tpm.disable_all_tools()
print("⚠️  All tools disabled")
```
