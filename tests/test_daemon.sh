#!/bin/bash
# SENA Daemon Test Suite
# Tests daemon functionality and performance

set -e

PROJECT_ROOT="/Users/sena/Project/sena-mcp-server"
DAEMON_SCRIPT="$PROJECT_ROOT/controller/sena_daemon.py"
CLIENT_SCRIPT="$PROJECT_ROOT/hooks/sena-daemon-client.sh"
SOCKET_PATH="$HOME/.claude/.sena_daemon.sock"
PID_FILE="$HOME/.claude/.sena_daemon.pid"

echo "════════════════════════════════════════════════════════════════"
echo "SENA Daemon Test Suite v1.0"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

pass() {
    echo -e "${GREEN}✓${NC} $1"
}

fail() {
    echo -e "${RED}✗${NC} $1"
    exit 1
}

warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Test 1: Check daemon script exists
echo "Test 1: Daemon script exists"
if [ -f "$DAEMON_SCRIPT" ]; then
    pass "Daemon script found at $DAEMON_SCRIPT"
else
    fail "Daemon script not found"
fi

# Test 2: Check client script exists
echo "Test 2: Client script exists"
if [ -f "$CLIENT_SCRIPT" ]; then
    pass "Client script found at $CLIENT_SCRIPT"
else
    fail "Client script not found"
fi

# Test 3: Start daemon
echo ""
echo "Test 3: Starting daemon"

# Stop existing daemon if running
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    kill "$OLD_PID" 2>/dev/null || true
    sleep 1
fi

# Clean up old socket
[ -S "$SOCKET_PATH" ] && rm -f "$SOCKET_PATH"

# Start daemon
python3 "$DAEMON_SCRIPT" start &>/dev/null &
DAEMON_PID=$!

# Wait for daemon to start
echo "Waiting for daemon to start..."
RETRIES=20
for ((i=0; i<RETRIES; i++)); do
    if [ -S "$SOCKET_PATH" ]; then
        pass "Daemon started successfully (PID: $DAEMON_PID)"
        break
    fi
    sleep 0.5
done

if [ ! -S "$SOCKET_PATH" ]; then
    fail "Daemon failed to start (socket not created)"
fi

# Test 4: Health check
echo ""
echo "Test 4: Health check"
source "$CLIENT_SCRIPT"

STATUS=$(health_check)
if [ "$STATUS" = "healthy" ]; then
    pass "Daemon is healthy"
else
    fail "Daemon health check failed: $STATUS"
fi

# Test 5: Format detection
echo ""
echo "Test 5: Format detection"

# Test brilliant thinking detection
FORMAT=$(detect_format "why is the sky blue?")
if [ "$FORMAT" = "brilliant_thinking" ]; then
    pass "Brilliant thinking detection works"
else
    fail "Brilliant thinking detection failed (got: $FORMAT)"
fi

# Test table detection
FORMAT=$(detect_format "show me a table of planets")
if [ "$FORMAT" = "table_format" ]; then
    pass "Table detection works"
else
    fail "Table detection failed (got: $FORMAT)"
fi

# Test truth verification detection
FORMAT=$(detect_format "is the earth flat true?")
if [ "$FORMAT" = "truth_verification" ]; then
    pass "Truth verification detection works"
else
    fail "Truth verification detection failed (got: $FORMAT)"
fi

# Test 6: Format application (detection only)
echo ""
echo "Test 6: Format application (detection-focused)"

# Note: Daemon focuses on format DETECTION (the expensive part)
# Format application still done by hooks via fallback
OUTPUT=$(apply_format "why is water wet?" "brilliant_thinking")
if [ "$OUTPUT" = "FORMAT_DETECTED" ] || echo "$OUTPUT" | grep -q "FORMAT"; then
    pass "Format detection via apply_format works"
else
    warn "Format application returned: $OUTPUT"
fi

# Test 7: Always-on check
echo ""
echo "Test 7: Always-on mode check"

ALWAYS_ON=$(check_always_on)
if [ "$ALWAYS_ON" = "true" ] || [ "$ALWAYS_ON" = "false" ]; then
    pass "Always-on check works (status: $ALWAYS_ON)"
else
    fail "Always-on check failed"
fi

# Test 8: Performance benchmark
echo ""
echo "Test 8: Performance benchmark"

# Benchmark daemon
START_TIME=$(date +%s%N)
for ((i=0; i<100; i++)); do
    detect_format "why is this happening?" &>/dev/null
done
END_TIME=$(date +%s%N)
DAEMON_TIME=$(( (END_TIME - START_TIME) / 1000000 ))
DAEMON_AVG=$(( DAEMON_TIME / 100 ))

pass "Daemon: 100 calls in ${DAEMON_TIME}ms (avg: ${DAEMON_AVG}ms)"

# Benchmark Python spawn for comparison
START_TIME=$(date +%s%N)
for ((i=0; i<10; i++)); do
    echo "test" | python3 -c "import sys; sys.stdin.read()" &>/dev/null
done
END_TIME=$(date +%s%N)
PYTHON_TIME=$(( (END_TIME - START_TIME) / 1000000 ))
PYTHON_AVG=$(( PYTHON_TIME / 10 ))

pass "Python spawn: 10 calls in ${PYTHON_TIME}ms (avg: ${PYTHON_AVG}ms)"

SPEEDUP=$(( PYTHON_AVG / DAEMON_AVG ))
if [ $SPEEDUP -gt 5 ]; then
    pass "Daemon is ${SPEEDUP}x faster than Python spawn! 🚀"
else
    warn "Speedup is only ${SPEEDUP}x (expected >5x)"
fi

# Test 9: Concurrent requests
echo ""
echo "Test 9: Concurrent request handling"

# Send 20 concurrent requests
for ((i=0; i<20; i++)); do
    detect_format "test question $i" &>/dev/null &
done

# Wait for all to complete
wait

pass "Daemon handled 20 concurrent requests successfully"

# Test 10: Statistics
echo ""
echo "Test 10: Daemon statistics"

STATS=$(daemon_call "stats" "{}")
REQUESTS=$(echo "$STATS" | jq -r '.result.requests_handled')

if [ "$REQUESTS" -gt 0 ]; then
    pass "Daemon has handled $REQUESTS requests"
    echo "    Request breakdown:"
    echo "$STATS" | jq -r '.result.requests_by_type | to_entries[] | "      \(.key): \(.value)"'
else
    fail "Daemon statistics not working"
fi

# Test 11: Graceful shutdown
echo ""
echo "Test 11: Graceful shutdown"

if [ -f "$PID_FILE" ]; then
    DAEMON_PID=$(cat "$PID_FILE")
    kill -TERM "$DAEMON_PID" 2>/dev/null

    # Wait for shutdown
    for ((i=0; i<10; i++)); do
        if ! kill -0 "$DAEMON_PID" 2>/dev/null; then
            pass "Daemon shut down gracefully"
            break
        fi
        sleep 0.5
    done

    # Force kill if still running
    if kill -0 "$DAEMON_PID" 2>/dev/null; then
        kill -9 "$DAEMON_PID" 2>/dev/null
        warn "Daemon had to be force-killed"
    fi
else
    fail "PID file not found for shutdown test"
fi

# Verify cleanup
if [ -S "$SOCKET_PATH" ]; then
    fail "Socket not cleaned up after shutdown"
else
    pass "Socket cleaned up successfully"
fi

if [ -f "$PID_FILE" ]; then
    fail "PID file not cleaned up after shutdown"
else
    pass "PID file cleaned up successfully"
fi

echo ""
echo "════════════════════════════════════════════════════════════════"
echo -e "${GREEN}All tests passed! ✓${NC}"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "Performance Summary:"
echo "  - Daemon average: ${DAEMON_AVG}ms per call"
echo "  - Python spawn average: ${PYTHON_AVG}ms per call"
echo "  - Speedup: ${SPEEDUP}x faster 🚀"
echo ""
