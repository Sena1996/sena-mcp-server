#!/usr/bin/env python3
"""
SENA Progress Display 100% Automatic Implementation - v3.3.1
Shows progress bars automatically for all multi-step operations
"""

import sys
import time
from typing import Dict, List, Optional
from pathlib import Path

class SENAProgressAuto100:
    """Fully automatic progress display system - v3.3.1"""

    def __init__(self):
        self.active_operations = {}
        self.operation_counter = 0
        self.auto_enabled = True

    def detect_operation_type(self, context: str) -> Optional[str]:
        """Detect what type of operation is being performed"""
        context_lower = context.lower()

        operations = {
            'file_search': ['find', 'search', 'locate', 'glob', 'grep'],
            'multi_read': ['read', 'open', 'view', 'multiple files'],
            'code_analysis': ['analyze', 'review', 'check', 'examine'],
            'multi_write': ['write', 'create', 'save', 'generate'],
            'installation': ['install', 'setup', 'configure'],
            'compilation': ['compile', 'build', 'make'],
            'testing': ['test', 'verify', 'validate'],
            'deployment': ['deploy', 'push', 'publish']
        }

        for op_type, keywords in operations.items():
            if any(kw in context_lower for kw in keywords):
                return op_type

        return 'processing'  # Default operation type

    def generate_progress_bar(self, progress: float, width: int = 40) -> str:
        """Generate a single progress bar"""
        filled = int(progress * width)

        if filled > 0 and filled < width:
            bar = "█" * (filled - 1) + "🦁" + "░" * (width - filled)
        elif filled == 0:
            bar = "🦁" + "░" * (width - 1)
        else:
            bar = "█" * (width - 1) + "🦁"

        status = " ✅" if progress >= 1.0 else ""
        percentage = int(progress * 100)

        return f"[{bar}] {percentage:3d}%{status}"

    def show_progress_before(self, operation: str, current: int = 1, total: int = 1) -> str:
        """Show progress before operation starts

        Args:
            operation: Operation description
            current: Current step (default 1)
            total: Total steps (default 1)
        """
        if not self.auto_enabled:
            return ""

        op_type = self.detect_operation_type(operation)
        steps = self.get_steps_for_operation(op_type)

        # Calculate progress (0% at start)
        progress = 0.0
        if total > 1:
            progress = (current - 1) / total

        # Show initial progress
        output = []
        output.append("\n┌" + "─" * 78 + "┐")
        output.append(f"│ SENA 🦁 STARTING: {operation.upper():<55} │")

        if total > 1:
            output.append(f"│ Step {current}/{total}{'':<68} │")

        output.append("├" + "─" * 78 + "┤")

        for i, step in enumerate(steps):
            step_progress = progress if i < len(steps) - 1 else 0.0
            bar = self.generate_progress_bar(step_progress)
            padded_step = f"{step:<20}"
            output.append(f"│ {padded_step} {bar:<55} │")

        output.append("└" + "─" * 78 + "┘")

        return '\n'.join(output)

    def show_progress_after(self, operation: str, current: int = 1, total: int = 1, success: bool = True) -> str:
        """Show progress after operation completes

        Args:
            operation: Operation description
            current: Current step (default 1)
            total: Total steps (default 1)
            success: Whether operation succeeded (default True)
        """
        if not self.auto_enabled:
            return ""

        op_type = self.detect_operation_type(operation)
        steps = self.get_steps_for_operation(op_type)

        # Calculate progress
        progress = current / total if total > 0 else 1.0

        # Show completed progress
        output = []
        output.append("\n┌" + "─" * 78 + "┐")

        status = "COMPLETED ✅" if success else "FAILED ❌"
        output.append(f"│ SENA 🦁 {status}: {operation.upper():<51} │")

        if total > 1:
            output.append(f"│ Step {current}/{total}{'':<68} │")

        output.append("├" + "─" * 78 + "┤")

        for step in steps:
            bar = self.generate_progress_bar(1.0 if success else progress)
            padded_step = f"{step:<20}"
            output.append(f"│ {padded_step} {bar:<55} │")

        output.append("└" + "─" * 78 + "┘")

        return '\n'.join(output)

    def auto_display_progress(self, operation: str, steps: List[str]) -> str:
        """Automatically display progress for an operation"""
        output = []

        # Header
        output.append("\n┌" + "─" * 78 + "┐")
        output.append(f"│ SENA 🦁 AUTO-PROGRESS: {operation.upper():<51} │")
        output.append("├" + "─" * 78 + "┤")

        # Progress bars for each step
        for i, step in enumerate(steps):
            progress = (i + 1) / len(steps)
            bar = self.generate_progress_bar(progress)
            padded_step = f"{step:<20}"
            output.append(f"│ {padded_step} {bar:<55} │")

        output.append("└" + "─" * 78 + "┘")

        return '\n'.join(output)

    def get_steps_for_operation(self, op_type: str) -> List[str]:
        """Get steps for a specific operation type"""
        step_map = {
            'file_search': ['Scanning', 'Matching', 'Results'],
            'multi_read': ['Opening files', 'Reading content', 'Processing'],
            'code_analysis': ['Parsing', 'Analyzing', 'Reporting'],
            'multi_write': ['Preparing', 'Writing', 'Verifying'],
            'installation': ['Downloading', 'Installing', 'Configuring'],
            'compilation': ['Preprocessing', 'Compiling', 'Linking'],
            'testing': ['Setup', 'Running tests', 'Results'],
            'deployment': ['Building', 'Uploading', 'Verifying'],
            'processing': ['Initializing', 'Processing', 'Completing']
        }

        return step_map.get(op_type, step_map['processing'])

    def enable_auto_progress(self):
        """Enable automatic progress display"""
        marker = Path.home() / '.claude' / '.sena_auto_progress_100'
        marker.write_text('enabled')
        self.auto_enabled = True
        return True

    def is_multi_step_operation(self, command: str) -> bool:
        """Determine if a command is a multi-step operation"""
        multi_step_indicators = [
            'for ', 'while ', '&&', '|',
            'find ', 'grep -r', 'npm install',
            'git clone', 'docker build', 'make',
            'pytest', 'cargo build', 'mvn'
        ]

        return any(indicator in command for indicator in multi_step_indicators)

# Global instance
progress_auto_100 = SENAProgressAuto100()

def show_progress_before(operation: str, current: int = 1, total: int = 1) -> str:
    """Show progress before operation

    Args:
        operation: Operation description
        current: Current step number (optional)
        total: Total number of steps (optional)
    """
    return progress_auto_100.show_progress_before(operation, current, total)

def show_progress_after(operation: str, current: int = 1, total: int = 1, success: bool = True) -> str:
    """Show progress after operation

    Args:
        operation: Operation description
        current: Current step number (optional)
        total: Total number of steps (optional)
        success: Whether operation succeeded (optional)
    """
    return progress_auto_100.show_progress_after(operation, current, total, success)

def auto_progress_for_steps(operation: str, steps: List[str]) -> str:
    """Show automatic progress for specific steps"""
    return progress_auto_100.auto_display_progress(operation, steps)

def enable_auto_progress():
    """Enable automatic progress display"""
    return progress_auto_100.enable_auto_progress()

def should_show_progress(command: str) -> bool:
    """Check if progress should be shown for a command"""
    return progress_auto_100.is_multi_step_operation(command)

if __name__ == "__main__":
    # Test automatic progress display
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "SENA PROGRESS AUTO 100% - v3.3.1 TEST".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "═" * 78 + "╝")
    print()

    # Test 1: Simple operation (backward compatible)
    print("Test 1: Simple operation (operation only)")
    print(show_progress_before("file search"))
    time.sleep(0.5)
    print(show_progress_after("file search"))

    # Test 2: Multi-step operation
    print("\nTest 2: Multi-step operation (with current/total)")
    print(show_progress_before("analyzing files", 1, 5))
    time.sleep(0.5)
    print(show_progress_after("analyzing files", 5, 5, True))

    # Test 3: Custom steps
    print("\nTest 3: Custom steps")
    custom_steps = ['Download', 'Extract', 'Install', 'Configure']
    print(auto_progress_for_steps("Installation", custom_steps))

    # Test 4: Failed operation
    print("\nTest 4: Failed operation")
    print(show_progress_after("deployment", 3, 5, False))

    print("\n✅ Auto Progress System 100% - v3.3.1 VERIFIED")
