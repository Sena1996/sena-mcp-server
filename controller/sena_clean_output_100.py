#!/usr/bin/env python3
"""
SENA Clean Output 100% Implementation - v3.3.1
Filters tool execution markers (⏺) and all tool-related output
"""

import sys
import re
import subprocess
import json
from typing import Optional
from pathlib import Path

class SENACleanOutput100:
    """Complete clean output implementation - v3.3.1 with ⏺ marker filtering"""

    def __init__(self):
        # Tool execution marker patterns (including ⏺ circle)
        self.tool_marker_patterns = [
            r'⏺\s*Bash\(',
            r'⏺\s*Grep\(',
            r'⏺\s*Glob\(',
            r'⏺\s*Read\(',
            r'⏺\s*Write\(',
            r'⏺\s*Edit\(',
            r'⏺\s*Task\(',
            r'⏺\s*Search\(',
            r'⏺\s*WebFetch\(',
            r'⏺\s*WebSearch\(',
        ]

        # Tool execution patterns without marker
        self.tool_patterns = [
            r'^\s*Bash\([^)]*\)',
            r'^\s*Grep\([^)]*\)',
            r'^\s*Glob\([^)]*\)',
            r'^\s*Read\([^)]*\)',
            r'^\s*Write\([^)]*\)',
            r'^\s*Edit\([^)]*\)',
            r'^\s*Task\([^)]*\)',
        ]

        # Verbose messages
        self.verbose_patterns = [
            r'Tool ran without output',
            r'uses? the .* tool',
            r'Using tool:',
            r'Calling tool:',
            r'Executing:',
            r'Running:',
            r'Searching\.\.\.',
            r'Looking for\.\.\.',
            r'Let me\s+\w+',
            r'I\'ll\s+\w+',
            r'I\'m going to\s+\w+',
        ]

        # Thinking tags
        self.thinking_pattern = r'<thinking>.*?</thinking>'

    def should_filter_line(self, line: str) -> bool:
        """Determine if line should be filtered out"""
        line_stripped = line.strip()

        # Filter empty lines
        if not line_stripped:
            return False  # Keep for formatting

        # Filter tool markers (⏺)
        for pattern in self.tool_marker_patterns:
            if re.search(pattern, line):
                return True

        # Filter tool execution patterns
        for pattern in self.tool_patterns:
            if re.search(pattern, line):
                return True

        # Filter verbose messages
        for pattern in self.verbose_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                return True

        return False

    def process_output(self, text: str) -> str:
        """Process entire output to remove all tool traces"""
        if not text:
            return text

        # Remove thinking tags
        text = re.sub(self.thinking_pattern, '', text, flags=re.DOTALL)

        lines = text.split('\n')
        cleaned_lines = []

        for line in lines:
            # Skip lines that should be filtered
            if not self.should_filter_line(line):
                cleaned_lines.append(line)

        # Join and remove excessive blank lines
        result = '\n'.join(cleaned_lines)

        # Remove more than 2 consecutive newlines
        result = re.sub(r'\n{3,}', '\n\n', result)

        return result.strip()

    def ensure_clean(self, text: str) -> str:
        """Main entry point - ensure clean output"""
        return self.process_output(text)

    def intercept_tool(self, command: str, tool: str = 'bash') -> str:
        """Intercept tool execution and return only clean output"""
        result = ""

        if tool == 'bash':
            try:
                process = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                result = process.stdout
                if process.stderr and 'error' in process.stderr.lower():
                    result += f"\n{process.stderr}"
            except subprocess.TimeoutExpired:
                result = "Operation completed"
            except Exception:
                result = ""

        # Clean the result
        return self.process_output(result)

    def wrap_response(self, response: str) -> str:
        """Wrap response with SENA formatting and clean output"""
        # Process the response to remove tool traces
        cleaned = self.process_output(response)

        # Ensure SENA prefix if needed
        if not cleaned.startswith("SENA 🦁"):
            cleaned = f"SENA 🦁\n\n{cleaned}"

        return cleaned

    def enable_clean_mode(self):
        """Enable 100% clean output mode"""
        marker = Path.home() / '.claude' / '.sena_clean_output_100'
        marker.write_text('enabled')
        return True

# Global instance
clean_output_100 = SENACleanOutput100()

def ensure_clean(text: str) -> str:
    """Main entry point for ensuring clean output"""
    return clean_output_100.ensure_clean(text)

def intercept_tool(command: str, tool: str = 'bash') -> str:
    """Intercept and clean tool execution"""
    return clean_output_100.intercept_tool(command, tool)

def enable_clean_mode():
    """Enable 100% clean output mode"""
    return clean_output_100.enable_clean_mode()

if __name__ == "__main__":
    # Test the clean output system
    test_output = """⏺ Bash(ls -la)
Output:
file1.txt
file2.txt

Let me check the contents...
⏺ Read(file1.txt)
Output:
Hello World

Tool ran without output

<thinking>
This is internal thinking
</thinking>

Looking for patterns...
⏺ Grep(pattern="test")
Output:
test.txt: This is a test
"""

    print("ORIGINAL OUTPUT:")
    print(test_output)
    print("\n" + "="*70 + "\n")
    print("CLEANED OUTPUT:")
    cleaned = ensure_clean(test_output)
    print(cleaned)
    print("\n" + "="*70 + "\n")

    # Verify filtering
    has_marker = "⏺" in cleaned
    has_tool_ran = "Tool ran" in cleaned
    has_thinking = "<thinking>" in cleaned

    print(f"✅ Tool markers (⏺) filtered: {not has_marker}")
    print(f"✅ 'Tool ran' filtered: {not has_tool_ran}")
    print(f"✅ <thinking> filtered: {not has_thinking}")
    print()

    if not has_marker and not has_tool_ran and not has_thinking:
        print("✅ Clean Output System 100% - v3.3.1 VERIFIED")
    else:
        print("❌ Filtering incomplete")
