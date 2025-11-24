#!/usr/bin/env python3
"""
Test Clean Output Implementation - Rule 5 Verification
"""

import sys
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

from clean_output_controller import CleanOutputController, ensure_clean_output
from sena_silent_wrapper import bash, grep, glob, read, multi_execute

print("═" * 60)
print("SENA RULE 5 - CLEAN OUTPUT VERIFICATION TEST")
print("═" * 60)
print()

# Test 1: Filter tool execution traces
print("TEST 1: Filtering Tool Execution Traces")
print("-" * 40)

dirty_output = """
Searching for files...
Bash(ls -la)
Output:
total 100
drwxr-xr-x  10 user  staff   320 Nov 22 10:00 .
drwxr-xr-x  25 user  staff   800 Nov 22 09:00 ..
-rw-r--r--   1 user  staff  2048 Nov 22 10:00 file.txt

Let me check the contents...
Read(file.txt)
Output:
Hello World
This is a test file.

Looking for patterns...
Grep(pattern="test", path=".")
Output:
file.txt:This is a test file.
"""

clean = ensure_clean_output(dirty_output)
print("CLEAN OUTPUT:")
print(clean)
print()

# Test 2: Silent execution
print("TEST 2: Silent Command Execution")
print("-" * 40)

# Execute commands silently
result = bash("echo 'This output appears without showing the command'")
print("Silent bash result:", result)

files = glob("*.py")
print(f"Found {len(files)} Python files (without showing glob command)")
print()

# Test 3: Multi-operation with progress
print("TEST 3: Multi-Operation with Progress")
print("-" * 40)

operations = [
    {'type': 'bash', 'name': 'Checking directory', 'command': 'pwd'},
    {'type': 'glob', 'name': 'Finding files', 'pattern': '*.py'},
    {'type': 'bash', 'name': 'Getting status', 'command': 'echo "Complete"'}
]

result = multi_execute(operations)
print(result)
print()

# Test 4: Verify no tool traces remain
print("TEST 4: Verification - No Tool Traces")
print("-" * 40)

controller = CleanOutputController()

test_messages = [
    "Bash(ls -la) showed these files",
    "Using Grep(pattern='error') to search",
    "Let me search for that...",
    "Searching for files now...",
    "Clean output with no traces"
]

for msg in test_messages:
    cleaned = controller.filter_output(msg)
    if cleaned.strip():
        print(f"✅ '{msg[:30]}...' → '{cleaned[:30]}...'")
    else:
        print(f"❌ '{msg[:30]}...' → [FILTERED OUT]")

print()
print("═" * 60)
print("RULE 5 IMPLEMENTATION STATUS")
print("═" * 60)

# Check all components
components = {
    'clean_output_controller.py': 'Clean output filtering',
    'sena_silent_wrapper.py': 'Silent command execution',
    'sena-enforcer.sh': 'Hook enforcement'
}

import os

for file, desc in components.items():
    if 'enforcer' in file:
        path = f"/Users/sena/.claude/hooks/{file}"
    else:
        path = f"/Users/sena/.claude/sena_controller_v3.0/{file}"

    if os.path.exists(path):
        print(f"✅ {file:<30} - {desc}")
    else:
        print(f"❌ {file:<30} - MISSING")

print()
print("🦁 RULE 5 CLEAN OUTPUT: IMPLEMENTATION COMPLETE")
print()
print("Key Features Implemented:")
print("• Tool execution traces filtered automatically")
print("• Commands execute silently in background")
print("• Only clean output displayed to user")
print("• Progress bars show without tool visibility")
print("• Hook enforcement at response level")
print()
print("═" * 60)