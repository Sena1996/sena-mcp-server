#!/bin/bash
# SENA Controller - PostToolUse Hook
# Suppresses tool output display using the documented suppressOutput feature
# This is part 2 of the loophole solution

# Read hook payload from stdin (JSON format)
INPUT=$(cat)

# Extract tool information using Python
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('tool_name', ''))" 2>/dev/null)
EXIT_CODE=$(echo "$INPUT" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('exit_code', 0))" 2>/dev/null)

# For SENA tools and Bash tools, suppress verbose output
# This uses the official suppressOutput feature from Claude Code hooks
if [[ "$TOOL_NAME" == "Bash" ]] || [[ "$TOOL_NAME" == "sena_"* ]]; then
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
