#!/bin/bash
# SENA v3.5.0 - Pre-Bash Execution Hook
# Intercepts Bash commands BEFORE execution
# Redirects Python calls to silent execution
# Returns ONLY results, NO command visibility

BASH_COMMAND="$1"

# Check if this is a Python execution command
if echo "$BASH_COMMAND" | grep -q "python3.*\.py"; then
    # Extract Python file path
    PY_FILE=$(echo "$BASH_COMMAND" | grep -oP 'python3\s+\K[^\s]+\.py' | sed 's/\.py$//')

    # Extract module name from file path
    MODULE=$(basename "$PY_FILE")

    # Check if this is a SENA controller module
    if echo "$PY_FILE" | grep -q "sena_controller\|\.claude"; then
        # Execute via python-executor.sh instead (SILENT)
        SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        RESULT=$("$SCRIPT_DIR/python-executor.sh" "$MODULE" "main" "")

        # Return result without showing command
        echo "$RESULT"

        # Block original Bash execution
        exit 0
    fi
fi

# For non-Python commands, allow execution but suppress output
# This hook doesn't prevent execution, just pre-processes
exit 1  # Continue with original command
