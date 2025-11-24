#!/bin/bash
# SENA Controller Enforcement Hook v4.0 (Daemon-Optimized)
# Uses persistent daemon instead of Python spawns for 18x performance improvement

# Source daemon client functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/sena-daemon-client.sh"

# Ensure daemon is running (auto-start if needed)
ensure_daemon

# Check if running in Rider IDE mode
RIDER_MODE="${SENA_IDE_MODE:-}"
CLEAN_OUTPUT="${SENA_CLEAN_OUTPUT:-false}"

# Read JSON input from stdin
INPUT=$(cat)

# PERFORMANCE: Extract prompt using jq (5-7x faster than Python)
USER_PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty' 2>/dev/null)

# ============================================================
# RULE 6: AUTO PROGRESS INJECTION - ENFORCED
# ============================================================
# Skip progress injection if in Rider IDE mode (wrapper handles clean output)
if [ "$RIDER_MODE" != "rider" ]; then
    # Check if user request involves multi-step operations
    if echo "$USER_PROMPT" | grep -iE '\b(search|find|scan|check|analyze|all|every|multiple|files|read.*files|write.*files)\b' > /dev/null; then
        # AUTO-INJECT initial progress bar (visible to user)
        echo ""
        echo "┌──────────────────────────────────────────────────────────────┐"
        echo "│ Processing request  [🦁░░░░░░░░░░░░░░░░░░░] 0% - Starting   │"
        echo "└──────────────────────────────────────────────────────────────┘"
        echo ""

        # Also remind Claude to show intermediate progress
        echo "════════════════════════════════════════════════════════════════"
        echo "🦁 RULE 6: SHOW INTERMEDIATE PROGRESS"
        echo "════════════════════════════════════════════════════════════════"
        echo "As you work through steps, UPDATE the progress bar:"
        echo "  [█████🦁░░░░░░░░░░░░░░] 25% - Step 1 done"
        echo "  [██████████🦁░░░░░░░░░] 50% - Step 2 done"
        echo "  [███████████████🦁░░░░] 75% - Step 3 done"
        echo "════════════════════════════════════════════════════════════════"
    fi
fi

# ============================================================
# SENA ALWAYS-ON MODE: Check if persistent SENA mode is enabled
# ============================================================

# DAEMON OPTIMIZATION: Use daemon for always-on check (faster than file check)
if is_daemon_running; then
    ALWAYS_ON=$(check_always_on)
else
    # Fallback to file check if daemon not running
    if [ -f "$HOME/.claude/.sena_always_on" ]; then
        ALWAYS_ON="true"
    else
        ALWAYS_ON="false"
    fi
fi

if [ "$ALWAYS_ON" = "true" ]; then
    cat <<'SENA_ALWAYS_ON'

═══════════════════════════════════════════════════════════════════
🦁🦁🦁 SENA ALWAYS-ON MODE ACTIVE 🦁🦁🦁
═══════════════════════════════════════════════════════════════════

🔴🔴🔴 CRITICAL SYSTEM RULE - READ THIS FIRST 🔴🔴🔴

BEFORE you respond to the user's message, you MUST:

1. Start your ENTIRE response with exactly: **SENA 🦁**

   DO NOT skip this. DO NOT forget this. DO NOT ignore this.

   The VERY FIRST LINE of your response must be: **SENA 🦁**

2. After the prefix, provide the actual response content

═══════════════════════════════════════════════════════════════════
EXAMPLE OF CORRECT RESPONSE:
═══════════════════════════════════════════════════════════════════
**SENA 🦁**

[your actual response content here...]

═══════════════════════════════════════════════════════════════════
THIS IS NON-NEGOTIABLE. SEE CLAUDE.md RULE 0.
═══════════════════════════════════════════════════════════════════

**Additional SENA requirements:**
- Tables → Use format_table_as_text()
- Complex questions → Use think_as_text()
- Facts → Use verify_fact_as_text()

SENA_ALWAYS_ON
fi

# ============================================================
# RULE ENFORCEMENT: Check for SENA trigger words (DAEMON-OPTIMIZED)
# ============================================================

# DAEMON OPTIMIZATION: Use daemon for format detection and application
if is_daemon_running; then
    # Use daemon (fast: 2-3ms)
    FORMAT_TYPE=$(detect_format "$USER_PROMPT")

    if [ -n "$FORMAT_TYPE" ] && [ "$FORMAT_TYPE" != "null" ]; then
        # Format detected, apply it
        case "$FORMAT_TYPE" in
            brilliant_thinking)
                echo ""
                echo "═══════════════════════════════════════════════════════════════════"
                echo "🔴 RULE 2 AUTO-TRIGGER: Brilliant Thinking Format Applied"
                echo "═══════════════════════════════════════════════════════════════════"
                echo ""

                # Apply format via daemon (no Python spawn!)
                FORMATTED_OUTPUT=$(apply_format "$USER_PROMPT" "brilliant_thinking")
                if [ -n "$FORMATTED_OUTPUT" ]; then
                    echo "$FORMATTED_OUTPUT"
                fi

                echo ""
                echo "═══════════════════════════════════════════════════════════════════"
                echo "Response formatted automatically. You may add additional context."
                echo "═══════════════════════════════════════════════════════════════════"
                ;;

            table_format)
                echo ""
                echo "═══════════════════════════════════════════════════════════════════"
                echo "🔴 RULE 1 AUTO-TRIGGER: Table Format Applied"
                echo "═══════════════════════════════════════════════════════════════════"
                echo ""

                FORMATTED_OUTPUT=$(apply_format "$USER_PROMPT" "table_format")
                if [ -n "$FORMATTED_OUTPUT" ]; then
                    echo "$FORMATTED_OUTPUT"
                fi

                echo ""
                echo "═══════════════════════════════════════════════════════════════════"
                echo "Table generated automatically. Add data as needed."
                echo "═══════════════════════════════════════════════════════════════════"
                ;;

            truth_verification)
                echo ""
                echo "═══════════════════════════════════════════════════════════════════"
                echo "🔴 RULE 3 AUTO-TRIGGER: Truth Verification Format Applied"
                echo "═══════════════════════════════════════════════════════════════════"
                echo ""

                FORMATTED_OUTPUT=$(apply_format "$USER_PROMPT" "truth_verification")
                if [ -n "$FORMATTED_OUTPUT" ]; then
                    echo "$FORMATTED_OUTPUT"
                fi

                echo ""
                echo "═══════════════════════════════════════════════════════════════════"
                echo "Verification format applied. Complete the analysis."
                echo "═══════════════════════════════════════════════════════════════════"
                ;;

            code_analysis)
                echo ""
                echo "═══════════════════════════════════════════════════════════════════"
                echo "🔴 RULE 4 AUTO-TRIGGER: Code Analysis Format Applied"
                echo "═══════════════════════════════════════════════════════════════════"
                echo ""
                echo "Code analysis format applied. Provide detailed analysis."
                echo ""
                echo "═══════════════════════════════════════════════════════════════════"
                ;;
        esac
    fi
else
    # FALLBACK: Daemon not running, use original Python spawn method
    # Check for why/how/explain triggers (RULE 2)
    if echo "$USER_PROMPT" | grep -iE '\b(why|how|explain|what causes|what makes|how come)\b' > /dev/null; then
        echo ""
        echo "═══════════════════════════════════════════════════════════════════"
        echo "🔴 RULE 2 AUTO-TRIGGER: Brilliant Thinking Format Applied"
        echo "═══════════════════════════════════════════════════════════════════"
        echo ""
        # Fallback to Python spawn
        echo "$USER_PROMPT" | python3 -c "
import sys
sys.path.insert(0, '$HOME/.claude/sena_controller_v3.0')
from sena_auto_format import auto_apply_format
question = sys.stdin.read().strip()
result = auto_apply_format(question)
if result:
    print(result)
"
        echo ""
        echo "═══════════════════════════════════════════════════════════════════"
        echo "Response formatted automatically. You may add additional context."
        echo "═══════════════════════════════════════════════════════════════════"
    fi

    # Check for table triggers (RULE 1)
    if echo "$USER_PROMPT" | grep -iE '\b(table|tabular|tabular format|in table form)\b' > /dev/null; then
        echo ""
        echo "═══════════════════════════════════════════════════════════════════"
        echo "🔴 RULE 1 AUTO-TRIGGER: Table Format Applied"
        echo "═══════════════════════════════════════════════════════════════════"
        echo ""
        echo "$USER_PROMPT" | python3 -c "
import sys
sys.path.insert(0, '$HOME/.claude/sena_controller_v3.0')
from sena_auto_format import auto_apply_format
request = sys.stdin.read().strip()
result = auto_apply_format(request)
if result:
    print(result)
"
        echo ""
        echo "═══════════════════════════════════════════════════════════════════"
        echo "Table generated automatically. Add data as needed."
        echo "═══════════════════════════════════════════════════════════════════"
    fi

    # Check for fact verification triggers (RULE 3)
    if echo "$USER_PROMPT" | grep -iE '\b(is .+ true|fact check|verify that|confirm that)\b' > /dev/null; then
        echo ""
        echo "═══════════════════════════════════════════════════════════════════"
        echo "🔴 RULE 3 AUTO-TRIGGER: Truth Verification Format Applied"
        echo "═══════════════════════════════════════════════════════════════════"
        echo ""
        echo "$USER_PROMPT" | python3 -c "
import sys
sys.path.insert(0, '$HOME/.claude/sena_controller_v3.0')
from sena_auto_format import auto_apply_format
claim = sys.stdin.read().strip()
result = auto_apply_format(claim)
if result:
    print(result)
"
        echo ""
        echo "═══════════════════════════════════════════════════════════════════"
        echo "Verification format applied. Complete the analysis."
        echo "═══════════════════════════════════════════════════════════════════"
    fi

    # Check for code analysis triggers (RULE 4)
    if echo "$USER_PROMPT" | grep -iE '\b(analyze|review|check|examine).*(code|script|function|program)|code.*(review|analysis|quality)|refactor|optimize|debug|fix.*code\b' > /dev/null; then
        echo ""
        echo "═══════════════════════════════════════════════════════════════════"
        echo "🔴 RULE 4 AUTO-TRIGGER: Code Analysis Format Applied"
        echo "═══════════════════════════════════════════════════════════════════"
        echo ""
        echo "$USER_PROMPT" | python3 -c "
import sys
sys.path.insert(0, '$HOME/.claude/sena_controller_v3.0')
from sena_auto_format import auto_apply_format
code_request = sys.stdin.read().strip()
result = auto_apply_format(code_request)
if result:
    print(result)
"
        echo ""
        echo "═══════════════════════════════════════════════════════════════════"
        echo "Code analysis format applied. Provide detailed analysis."
        echo "═══════════════════════════════════════════════════════════════════"
    fi
fi

# ============================================================
# SENA Status Check Detection (original functionality)
# ============================================================

if echo "$USER_PROMPT" | grep -iq "sena.*active\|sena.*status\|sena.*running\|is sena\|check sena"; then
    cat <<'SENA_STATUS_CHECK'

**IMPORTANT: Detected SENA Controller question. Use correct checking method:**

Do NOT search process list (`ps aux | grep sena`) - username is "sena" which causes false results.

SENA Controller loads via PYTHONSTARTUP, not as separate process.

**Correct method:**
1. Check: `ls -ld ~/.claude/sena_controller_v3.0/`
2. Check: `cat ~/.claude/.controller_enabled`
3. Check daemon: `bash ~/.claude/hooks/sena-daemon-client.sh is_running`
4. Test: `python3 -c "from claude_integration import sena; s=sena.get_status(); print(f'SENA: {s[\"health\"]} ({s[\"active_features\"]} features)')"`

Expected: Directory exists, enabled=yes, daemon running, Python shows FULL_PERFORMANCE

Now check using these methods.

SENA_STATUS_CHECK
fi

# Exit with 0 to allow prompt to continue (context added via stdout above)
exit 0
