#!/bin/bash
# SENA Auto Progress Hook v3.3
# Automatically shows progress for every conversation

# Check if progress is already running
if pgrep -f "sena_live_progress.py" > /dev/null; then
    # Kill existing progress
    pkill -f "sena_live_progress.py"
fi

# Start progress in background with 10 second timeout
(
    python3 $HOME/.claude/sena_live_progress.py &
    PROGRESS_PID=$!

    # Let it run for conversation processing (10 seconds)
    sleep 10

    # Gracefully terminate
    kill -TERM $PROGRESS_PID 2>/dev/null
) &

# Continue with original hook processing
exec "$@"