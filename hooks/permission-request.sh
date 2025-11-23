#!/bin/bash
# SENA Tool Permission Request Hook
# Dynamically allows/denies tools based on SENA runtime preferences
# No restart required - changes apply immediately!

SENA_TOOL_PERMISSIONS="$HOME/.claude/.sena_tool_permissions.json"

# Read JSON input from stdin if provided
if [ ! -t 0 ]; then
    INPUT=$(cat)
else
    INPUT=""
fi

# Extract tool name from input (Claude Code passes this information)
# The exact format may vary, but we'll try to extract the tool name
if [ -n "$INPUT" ]; then
    TOOL_NAME=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    # Try different possible fields for tool name
    tool = data.get('tool', data.get('toolName', data.get('name', '')))
    print(tool)
except:
    pass
" 2>/dev/null)
else
    # If no input, check command line arguments
    TOOL_NAME="$1"
fi

# If we still don't have a tool name, allow by default
if [ -z "$TOOL_NAME" ]; then
    echo "allow"
    exit 0
fi

# Check if SENA tool permissions file exists
if [ ! -f "$SENA_TOOL_PERMISSIONS" ]; then
    # No SENA config yet - allow all by default
    echo "allow"
    exit 0
fi

# Check SENA state for this tool
TOOL_ENABLED=$(python3 -c "
import sys, json

try:
    with open('$SENA_TOOL_PERMISSIONS', 'r') as f:
        data = json.load(f)

    tools = data.get('tools', {})
    tool_info = tools.get('$TOOL_NAME', {})

    # Default to enabled if not configured
    enabled = tool_info.get('enabled', True)

    print('true' if enabled else 'false')
except:
    # On error, default to allow
    print('true')
" 2>/dev/null)

# Return decision based on SENA state
if [ "$TOOL_ENABLED" = "true" ]; then
    echo "allow"
else
    echo "deny"
fi

exit 0
