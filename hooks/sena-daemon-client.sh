#!/bin/bash
# SENA Daemon Client - Bash helper for hook communication
# Provides simple interface to daemon RPC calls

SOCKET_PATH="$HOME/.claude/.sena_daemon.sock"
TIMEOUT=5

# Check if daemon is running
is_daemon_running() {
    if [ ! -S "$SOCKET_PATH" ]; then
        return 1
    fi
    return 0
}

# Make RPC call to daemon
daemon_call() {
    local method="$1"
    local params="$2"

    if ! is_daemon_running; then
        echo '{"error": "daemon_not_running"}' >&2
        return 1
    fi

    # Build JSON-RPC request
    local request
    if [ -n "$params" ]; then
        request="{\"jsonrpc\":\"2.0\",\"method\":\"$method\",\"params\":$params,\"id\":1}"
    else
        request="{\"jsonrpc\":\"2.0\",\"method\":\"$method\",\"params\":{},\"id\":1}"
    fi

    # Send request and get response using nc (netcat)
    local response
    response=$(echo "$request" | nc -U -w $TIMEOUT "$SOCKET_PATH" 2>/dev/null)

    if [ $? -ne 0 ]; then
        echo '{"error": "connection_failed"}' >&2
        return 1
    fi

    echo "$response"
}

# Detect format for user input
detect_format() {
    local user_input="$1"

    # Escape user input for JSON
    local escaped_input
    escaped_input=$(echo "$user_input" | jq -Rs .)

    local params="{\"user_input\":$escaped_input}"
    local response
    response=$(daemon_call "detect_format" "$params")

    if [ $? -ne 0 ]; then
        return 1
    fi

    # Extract format_type from response
    echo "$response" | jq -r '.result.format_type // empty'
}

# Apply format to user input
apply_format() {
    local user_input="$1"
    local format_type="$2"

    # Escape user input for JSON
    local escaped_input
    escaped_input=$(echo "$user_input" | jq -Rs .)

    local params
    if [ -n "$format_type" ]; then
        params="{\"user_input\":$escaped_input,\"format_type\":\"$format_type\"}"
    else
        params="{\"user_input\":$escaped_input}"
    fi

    local response
    response=$(daemon_call "apply_format" "$params")

    if [ $? -ne 0 ]; then
        return 1
    fi

    # Extract output from response
    echo "$response" | jq -r '.result.output // empty'
}

# Check if SENA always-on mode is active
check_always_on() {
    local response
    response=$(daemon_call "check_always_on" "{}")

    if [ $? -ne 0 ]; then
        return 1
    fi

    # Extract active status
    echo "$response" | jq -r '.result.active // false'
}

# Health check
health_check() {
    local response
    response=$(daemon_call "health_check" "{}")

    if [ $? -ne 0 ]; then
        return 1
    fi

    echo "$response" | jq -r '.result.status // "unknown"'
}

# Start daemon if not running
ensure_daemon() {
    if ! is_daemon_running; then
        # Start daemon in background
        python3 "$HOME/.claude/sena_controller_v3.0/sena_daemon.py" start &>/dev/null &

        # Wait for daemon to start (max 2 seconds)
        local retries=20
        local wait_time=0.1

        for ((i=0; i<retries; i++)); do
            if is_daemon_running; then
                return 0
            fi
            sleep $wait_time
        done

        return 1
    fi

    return 0
}

# Export functions for sourcing
export -f is_daemon_running
export -f daemon_call
export -f detect_format
export -f apply_format
export -f check_always_on
export -f health_check
export -f ensure_daemon

# If called directly (not sourced), execute command
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    case "$1" in
        is_running)
            if is_daemon_running; then
                echo "Daemon is running"
                exit 0
            else
                echo "Daemon is NOT running"
                exit 1
            fi
            ;;
        detect_format)
            detect_format "$2"
            ;;
        apply_format)
            apply_format "$2" "$3"
            ;;
        check_always_on)
            check_always_on
            ;;
        health)
            health_check
            ;;
        ensure)
            ensure_daemon
            ;;
        *)
            echo "Usage: $0 {is_running|detect_format|apply_format|check_always_on|health|ensure}"
            exit 1
            ;;
    esac
fi
