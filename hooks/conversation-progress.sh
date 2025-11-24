#!/bin/bash
# SENA Conversation Progress Hook v3.3
# Shows progress bar for each conversation prompt

# Function to show progress for conversation
show_conversation_progress() {
    local prompt="$1"

    # Start progress in background
    (
        python3 $HOME/.claude/sena_live_progress.py --interactive &
        PROGRESS_PID=$!

        # Let it run for conversation processing
        sleep 5

        # Clean termination
        kill -TERM $PROGRESS_PID 2>/dev/null
    ) &
}

# Check if this is a conversation prompt
if [ -n "$CLAUDE_PROMPT" ]; then
    # Show progress for this conversation
    show_conversation_progress "$CLAUDE_PROMPT"
fi

# Continue with normal processing
exec "$@"