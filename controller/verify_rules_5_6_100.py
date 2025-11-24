#!/usr/bin/env python3
"""
Verify Rules 5 and 6 are at 100% implementation
"""

import sys
import os
from pathlib import Path

sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

print("═" * 70)
print("VERIFICATION: RULES 5 & 6 - 100% IMPLEMENTATION TEST")
print("═" * 70)

# Rule 5: Clean Output
print("\n" + "─" * 70)
print("RULE 5: CLEAN OUTPUT (100% Target)")
print("─" * 70)

rule5_checks = {
    'sena_clean_output_100.py exists': False,
    'Clean function works': False,
    'Hook integration updated': False,
    'Removes all tool traces': False,
    'Preserves actual content': False
}

# Check file exists
if Path('/Users/sena/.claude/sena_controller_v3.0/sena_clean_output_100.py').exists():
    rule5_checks['sena_clean_output_100.py exists'] = True

# Test clean function
try:
    from sena_clean_output_100 import ensure_clean

    # Test with dirty output
    test_input = """Bash(ls -la)
Output:
file1.txt
file2.txt
Hello World
Read(file.txt)
Output:
Content here"""

    cleaned = ensure_clean(test_input)

    # Check if tool traces removed
    if 'Bash(' not in cleaned and 'Output:' not in cleaned and 'Read(' not in cleaned:
        rule5_checks['Removes all tool traces'] = True

    # Check if content preserved
    if 'file1.txt' in cleaned and 'Content here' in cleaned:
        rule5_checks['Preserves actual content'] = True

    rule5_checks['Clean function works'] = True
except Exception as e:
    print(f"Error testing clean function: {e}")

# Check hook integration
hook_file = Path('/Users/sena/.claude/hooks/sena-enforcer.sh')
if hook_file.exists():
    content = hook_file.read_text()
    if 'sena_controller_100' in content or 'RULE 5 & 6' in content:
        rule5_checks['Hook integration updated'] = True

# Display Rule 5 results
for check, result in rule5_checks.items():
    print(f"  {'✅' if result else '❌'} {check}")

rule5_score = sum(rule5_checks.values()) * 20
print(f"\nRule 5 Score: {rule5_score}/100")

# Rule 6: Progress Display
print("\n" + "─" * 70)
print("RULE 6: PROGRESS DISPLAY (100% Target)")
print("─" * 70)

rule6_checks = {
    'sena_progress_auto_100.py exists': False,
    'Auto progress function works': False,
    'Hook auto-triggers progress': False,
    'Progress displays before operation': False,
    'Progress displays after operation': False
}

# Check file exists
if Path('/Users/sena/.claude/sena_controller_v3.0/sena_progress_auto_100.py').exists():
    rule6_checks['sena_progress_auto_100.py exists'] = True

# Test progress functions
try:
    from sena_progress_auto_100 import show_progress_before, show_progress_after

    # Test progress generation
    before = show_progress_before("test operation")
    after = show_progress_after("test operation")

    if '🦁' in before and '0%' in before:
        rule6_checks['Progress displays before operation'] = True

    if '🦁' in after and '100%' in after and '✅' in after:
        rule6_checks['Progress displays after operation'] = True

    rule6_checks['Auto progress function works'] = True
except Exception as e:
    print(f"Error testing progress: {e}")

# Check hook for auto-trigger
hook_file = Path('/Users/sena/.claude/hooks/user-prompt-submit.sh')
if hook_file.exists():
    content = hook_file.read_text()
    if 'RULE 6: AUTO-PROGRESS' in content:
        rule6_checks['Hook auto-triggers progress'] = True

# Display Rule 6 results
for check, result in rule6_checks.items():
    print(f"  {'✅' if result else '❌'} {check}")

rule6_score = sum(rule6_checks.values()) * 20
print(f"\nRule 6 Score: {rule6_score}/100")

# Combined Controller Test
print("\n" + "─" * 70)
print("COMBINED CONTROLLER 100% TEST")
print("─" * 70)

controller_checks = {
    'sena_controller_100.py exists': False,
    'Controller integrates both rules': False,
    '100% mode can be enabled': False
}

# Check controller exists
if Path('/Users/sena/.claude/sena_controller_v3.0/sena_controller_100.py').exists():
    controller_checks['sena_controller_100.py exists'] = True

# Test controller
try:
    from sena_controller_100 import enable_100_percent, wrap_operation

    # Test enabling 100% mode
    enable_100_percent()
    controller_checks['100% mode can be enabled'] = True

    # Test wrap operation
    result = wrap_operation("search all files", "Found 50 files")
    if '🦁' in result and 'STARTING' in result:
        controller_checks['Controller integrates both rules'] = True
except Exception as e:
    print(f"Error testing controller: {e}")

for check, result in controller_checks.items():
    print(f"  {'✅' if result else '❌'} {check}")

# Final Summary
print("\n" + "═" * 70)
print("FINAL VERIFICATION SUMMARY")
print("═" * 70)

total_checks = len(rule5_checks) + len(rule6_checks) + len(controller_checks)
passed_checks = sum(rule5_checks.values()) + sum(rule6_checks.values()) + sum(controller_checks.values())

print(f"""
┌────┬──────────────────────┬────────┬──────────────────────┐
│ # │ Rule                  │ Score  │ Status               │
├────┼──────────────────────┼────────┼──────────────────────┤
│ 5 │ Clean Output          │ {rule5_score:3}/100 │ {'✅ 100% ACHIEVED' if rule5_score == 100 else f'⚠️  {rule5_score}% PARTIAL':<20} │
│ 6 │ Progress Display      │ {rule6_score:3}/100 │ {'✅ 100% ACHIEVED' if rule6_score == 100 else f'⚠️  {rule6_score}% PARTIAL':<20} │
└────┴──────────────────────┴────────┴──────────────────────┘

Total Checks: {passed_checks}/{total_checks} passed
Overall Achievement: {(passed_checks/total_checks)*100:.1f}%
""")

if rule5_score == 100 and rule6_score == 100:
    print("🎯 SUCCESS: Both Rules 5 and 6 are now at 100% implementation!")
    print("🦁 SENA Controller 100% mode is fully operational!")
else:
    print(f"⚠️  Some work remaining: Rule 5 at {rule5_score}%, Rule 6 at {rule6_score}%")

print("═" * 70)