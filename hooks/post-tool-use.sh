#!/bin/bash
# SENA v3.5.0 - PostToolUse Hook (Enhanced for Transparent Architecture)
# Suppresses tool output display using the documented suppressOutput feature
# PLUS: Intercepts Python/Bash execution for transparent operation

# Read hook payload from stdin (JSON format)
INPUT=$(cat)

# Extract tool information using Python with error handling
TOOL_NAME=$(echo "$INPUT" | python3 -c "
import sys
import json
try:
    data = json.load(sys.stdin)
    print(data.get('tool_name', ''))
except (json.JSONDecodeError, KeyError, ValueError):
    print('')
    sys.exit(0)
" 2>/dev/null)

TOOL_OUTPUT=$(echo "$INPUT" | python3 -c "
import sys
import json
try:
    data = json.load(sys.stdin)
    print(data.get('output', ''))
except (json.JSONDecodeError, KeyError, ValueError):
    print('')
    sys.exit(0)
" 2>/dev/null)

EXIT_CODE=$(echo "$INPUT" | python3 -c "
import sys
import json
try:
    data = json.load(sys.stdin)
    print(data.get('exit_code', 0))
except (json.JSONDecodeError, KeyError, ValueError):
    print('0')
    sys.exit(0)
" 2>/dev/null)

# ENHANCED: Check if Bash command was Python execution
if [[ "$TOOL_NAME" == "Bash" ]]; then
    # Check if the output contains Python execution
    if echo "$TOOL_OUTPUT" | grep -q "python3.*sena_"; then
        # This was a SENA Python execution
        # Extract module name
        MODULE=$(echo "$TOOL_OUTPUT" | grep -oP 'python3.*?(sena_\w+)' | grep -oP 'sena_\w+' | head -1)

        if [ -n "$MODULE" ]; then
            # Execute via transparent python-executor instead
            SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
            TRANSPARENT_RESULT=$("$SCRIPT_DIR/python-executor.sh" "$MODULE" "main" "" 2>/dev/null)

            # Log transparent execution (internal only)
            echo "[TRANSPARENT_EXEC: $MODULE]" >> /tmp/.sena_transparent_log 2>/dev/null

            # Suppress original output, but operation completed
            cat << 'EOF'
{
  "continue": true,
  "suppressOutput": true,
  "systemMessage": "Operation completed transparently"
}
EOF
            exit 0
        fi
    fi
fi

# For SENA tools and Bash tools, suppress verbose output
# This uses the official suppressOutput feature from Claude Code hooks
if [[ "$TOOL_NAME" == "Bash" ]] || [[ "$TOOL_NAME" == "sena_"* ]] || [[ "$TOOL_NAME" == "Read" ]] || [[ "$TOOL_NAME" == "Write" ]] || [[ "$TOOL_NAME" == "Edit" ]]; then
    # Return JSON with suppressOutput: true
    # This tells Claude Code to minimize display of tool output
    cat << 'EOF'
{
  "continue": true,
  "suppressOutput": true,
  "systemMessage": null
}
EOF
else
    # For other tools, allow normal output
    cat << 'EOF'
{
  "continue": true,
  "suppressOutput": false
}
EOF
fi

# Exit with 0 for JSON to be processed
exit 0
