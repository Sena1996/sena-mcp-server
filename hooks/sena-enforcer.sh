#!/bin/bash
# SENA Enforcement Hook - Validates Claude responses for SENA rule compliance

# Read JSON input from stdin
INPUT=$(cat)

# Check if running in Rider IDE mode
RIDER_MODE="${SENA_IDE_MODE:-}"
CLEAN_OUTPUT="${SENA_CLEAN_OUTPUT:-false}"

# PERFORMANCE: Extract fields using jq (5-7x faster than Python)
CLAUDE_RESPONSE=$(echo "$INPUT" | jq -r '.response // empty' 2>/dev/null)
USER_MESSAGE=$(echo "$INPUT" | jq -r '.userMessage // .prompt // empty' 2>/dev/null)

# ============================================================
# RULE 5 & 6: 100% CLEAN OUTPUT AND AUTO PROGRESS
# ============================================================
# Always process through 100% controller for clean output and progress
CLAUDE_RESPONSE=$(echo "$CLAUDE_RESPONSE" | python3 -c "
import sys
sys.path.insert(0, '$HOME/.claude/sena_controller_v3.0')

# Import 100% implementations
from sena_controller_100 import process_response, auto_detect_and_apply

# Get user message for context
user_msg = '''$USER_MESSAGE'''
response = sys.stdin.read()

# Check if multi-step operation for progress
if any(kw in user_msg.lower() for kw in ['search', 'find', 'analyze', 'multiple', 'all']):
    # Apply both progress and clean output
    result = auto_detect_and_apply(user_msg, response)
    print(result)
else:
    # Just clean output
    result = process_response(response)
    print(result)
")

# ============================================================
# SENA ALWAYS-ON MODE: Check for required prefix
# ============================================================
if [ -f "$HOME/.claude/.sena_always_on" ]; then
    # Check if response starts with "SENA 🦁" or "**SENA 🦁**"
    if ! echo "$CLAUDE_RESPONSE" | head -n 5 | grep -q "SENA 🦁"; then
        echo "⚠️  SENA ALWAYS-ON MODE VIOLATION"
        echo ""
        echo "Always-On mode is active but response missing 'SENA 🦁' prefix."
        echo ""
        echo "🔴 MANDATORY REQUIREMENT:"
        echo "Every response must start with: **SENA 🦁**"
        echo ""
        echo "This is a SYSTEM-LEVEL enforcement. Response blocked."
        exit 1
    fi
fi

# Check if user message contains SENA triggers
if echo "$USER_MESSAGE" | grep -qiE '\b(why|how|explain|what causes|what makes)\b'; then
    # Check if Claude's response used SENA (contains "SENA BRILLIANT THINKING")
    if ! echo "$CLAUDE_RESPONSE" | grep -q "SENA BRILLIANT THINKING"; then
        # VIOLATION DETECTED - Force SENA execution
        echo "⚠️  SENA RULE VIOLATION DETECTED"
        echo "User question contained trigger words but SENA was not used."
        echo "Forcing SENA execution now..."
        echo ""

        # Extract the question and run SENA (SECURITY: use stdin to prevent injection)
        echo "$USER_MESSAGE" | python3 -c "
import sys
sys.path.insert(0, '$HOME/.claude/sena_controller_v3.0')
from sena_direct_output import think_as_text
question = sys.stdin.read().strip()
print(think_as_text(question))
"

        exit 1  # Prevent original response from showing
    fi
fi

# Check for table requests
if echo "$USER_MESSAGE" | grep -qiE '\b(table|tabular|tabular format)\b'; then
    if ! echo "$CLAUDE_RESPONSE" | grep -q "SENA BEAUTIFUL UI"; then
        echo "⚠️  SENA TABLE RULE VIOLATION DETECTED"
        exit 1
    fi
fi

# ============================================================
# RULE 6: AUTO-INJECT COMPLETION PROGRESS BAR
# ============================================================
# Skip progress bar if in Rider IDE mode with clean output (wrapper handles it)
if [ "$RIDER_MODE" != "rider" ]; then
    if echo "$USER_MESSAGE" | grep -qiE '\b(search|find|scan|check|analyze|all|every|multiple|files|read.*files|write.*files)\b'; then
        # Append completion progress bar to response
        echo "$CLAUDE_RESPONSE"
        echo ""
        echo "┌──────────────────────────────────────────────────────────────┐"
        echo "│ Processing request  [████████████████████🦁] 100% ✅ Complete │"
        echo "└──────────────────────────────────────────────────────────────┘"
        exit 0
    fi
fi

# All checks passed
exit 0
