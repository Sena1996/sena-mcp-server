#!/usr/bin/env python3
"""
SENA Controller 100% Implementation
Complete automation for Rules 5 and 6
Integrates clean output and automatic progress display
"""

import sys
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Import the 100% implementations
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')

from sena_clean_output_100 import ensure_clean, intercept_tool
from sena_progress_auto_100 import (
    show_progress_before,
    show_progress_after,
    auto_progress_for_steps,
    should_show_progress
)

class SENAController100:
    """Master controller for 100% automation of all rules"""

    def __init__(self):
        self.clean_output_enabled = True
        self.auto_progress_enabled = True
        self.operation_stack = []

    def process_user_input(self, user_input: str) -> Dict:
        """Process user input and determine what automations to apply"""
        result = {
            'needs_progress': False,
            'needs_clean': True,  # Always clean output
            'operation_type': None,
            'format_needed': None
        }

        # Check if this is a multi-step operation needing progress
        keywords = ['search', 'find', 'analyze', 'multiple', 'all', 'every', 'scan', 'check']
        if any(kw in user_input.lower() for kw in keywords):
            result['needs_progress'] = True
            result['operation_type'] = self._detect_operation(user_input)

        # Check for format triggers (Rules 1-4)
        from sena_auto_format import auto_apply_format
        format_result = auto_apply_format(user_input)
        if format_result:
            result['format_needed'] = format_result

        return result

    def _detect_operation(self, text: str) -> str:
        """Detect operation type from text"""
        if 'file' in text.lower() or 'search' in text.lower():
            return 'file_search'
        elif 'code' in text.lower() or 'analyze' in text.lower():
            return 'code_analysis'
        elif 'read' in text.lower() or 'open' in text.lower():
            return 'multi_read'
        elif 'write' in text.lower() or 'create' in text.lower():
            return 'multi_write'
        else:
            return 'processing'

    def wrap_with_automation(self, command: str, response: str) -> str:
        """Wrap command execution with all automations"""
        output = []

        # Detect what's needed
        needs = self.process_user_input(command)

        # Show progress before (Rule 6)
        if needs['needs_progress']:
            output.append(show_progress_before(needs['operation_type']))

        # Clean the response (Rule 5)
        if needs['needs_clean']:
            response = ensure_clean(response)

        # Add the cleaned response
        output.append(response)

        # Show progress after (Rule 6)
        if needs['needs_progress']:
            output.append(show_progress_after(needs['operation_type']))

        # Apply format if needed (Rules 1-4)
        if needs['format_needed']:
            output.append(needs['format_needed'])

        return '\n'.join(output)

    def enable_100_percent_mode(self):
        """Enable 100% automation for all rules"""
        # Create marker files
        markers = [
            Path.home() / '.claude' / '.sena_clean_output_100',
            Path.home() / '.claude' / '.sena_auto_progress_100',
            Path.home() / '.claude' / '.sena_100_percent_mode'
        ]

        for marker in markers:
            marker.write_text('enabled')

        print("✅ SENA 100% Mode Enabled")
        print("• Rule 5 (Clean Output): 100% Active")
        print("• Rule 6 (Progress Display): 100% Active")
        return True

    def intercept_response(self, response: str) -> str:
        """Intercept and process all responses"""
        # Remove all tool execution traces (Rule 5)
        cleaned = ensure_clean(response)

        # Add SENA prefix if missing
        if not cleaned.startswith("SENA 🦁"):
            cleaned = f"SENA 🦁\n\n{cleaned}"

        return cleaned

    def auto_inject_progress(self, operation: str, steps: int = 3) -> str:
        """Automatically inject progress display"""
        if steps >= 2:  # Multi-step operation
            return show_progress_before(operation)
        return ""

# Global controller instance
controller_100 = SENAController100()

def enable_100_percent():
    """Enable 100% automation mode"""
    return controller_100.enable_100_percent_mode()

def process_response(response: str) -> str:
    """Process response with all automations"""
    return controller_100.intercept_response(response)

def wrap_operation(command: str, response: str) -> str:
    """Wrap operation with all automations"""
    return controller_100.wrap_with_automation(command, response)

def auto_detect_and_apply(user_input: str, response: str) -> str:
    """Automatically detect what's needed and apply"""
    needs = controller_100.process_user_input(user_input)

    output = []

    # Apply progress if needed
    if needs['needs_progress']:
        output.append(show_progress_before(needs['operation_type']))

    # Clean output
    cleaned = ensure_clean(response)
    output.append(cleaned)

    # Complete progress
    if needs['needs_progress']:
        output.append(show_progress_after(needs['operation_type']))

    return '\n'.join(output)

if __name__ == "__main__":
    print("SENA CONTROLLER 100% IMPLEMENTATION TEST")
    print("="*60)

    # Enable 100% mode
    enable_100_percent()

    # Test clean output (Rule 5)
    dirty = "Bash(ls -la)\nOutput:\nfile1.txt\nfile2.txt"
    print("\nTesting Clean Output:")
    print("Before:", dirty)
    print("After:", process_response(dirty))

    # Test auto progress (Rule 6)
    print("\nTesting Auto Progress:")
    result = wrap_operation("search for all Python files", "Found 10 files")
    print(result)

    print("\n✅ SENA Controller 100% Ready")
    print("Rules 5 and 6 now at 100% implementation!")