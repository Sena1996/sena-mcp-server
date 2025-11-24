#!/usr/bin/env python3
"""
SENA Controller v3.0 - Transparent Integration Layer
SENA IS Claude's operating system - not an optional tool
Zero optional parameters - just pure transparent operation
"""

import sys
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime

# Ensure path
controller_path = Path.home() / '.claude' / 'sena_controller_v3.0'
if str(controller_path) not in sys.path:
    sys.path.insert(0, str(controller_path))

from claude_sena_integration import sena
# from v3.ui.terminal_ui import TerminalUI as UI  # v3 moved to backup


class TransparentSenaLayer:
    """
    Transparent layer - SENA IS the operating system
    No flags, no options, no decisions - just works
    """

    def __init__(self):
        self.activated = False
        self.sena = sena
        self.session_start = datetime.now()

    def ensure_active(self):
        """Silently ensure SENA is active"""
        if not self.activated:
            self.sena.activate()
            self.activated = True

    def think(self, question: str) -> Dict[str, Any]:
        """
        Default thinking - routes through SENA brilliant thinking
        NO optional parameters - just works
        """
        self.ensure_active()

        # Auto-determine mode
        question_lower = question.lower()
        if any(word in question_lower for word in ['why', 'how', 'explain']):
            mode = "first_principles"
        elif any(word in question_lower for word in ['truth', 'correct', 'verify']):
            mode = "truth_verification"
        else:
            mode = "auto"

        return self.sena.think_brilliantly(question, mode=mode)

    def format_table(self, headers: List[str], rows: List[List[str]],
                     title: str = "") -> str:
        """
        Default table formatting - ALWAYS Beautiful UI
        NO optional parameters - just works
        """
        self.ensure_active()
        return UI.table(headers=headers, rows=rows, title=title)

    def verify_fact(self, statement: str) -> Dict[str, Any]:
        """
        Default fact verification - truth verification
        NO optional parameters - just works
        """
        self.ensure_active()
        return self.sena.verify_truth(statement)

    def analyze_code(self, code: str) -> Dict[str, Any]:
        """
        Default code analysis - security scanner
        NO optional parameters - just works
        """
        self.ensure_active()
        return self.sena.scan_security(code)

    def check_constitutional(self, command: str) -> Dict[str, Any]:
        """
        Constitutional check
        NO optional parameters - just works
        """
        self.ensure_active()
        return self.sena.check_constitutional(command)

    def get_status(self) -> Dict[str, Any]:
        """Get status"""
        self.ensure_active()
        return self.sena.get_status()


# Global transparent layer
transparent_sena = TransparentSenaLayer()

# Export
__all__ = ['transparent_sena', 'TransparentSenaLayer']
