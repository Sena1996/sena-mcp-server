#!/usr/bin/env python3
"""
SENA Controller v3.0 - Complete Claude Integration
Transparent, automatic operation - zero optional parameters
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime

# Ensure SENA is in path
controller_path = Path.home() / '.claude' / 'sena_controller_v3.0'
if str(controller_path) not in sys.path:
    sys.path.insert(0, str(controller_path))

# from v3.core.controller import SenaController  # v3 moved to backup
# from bootstrap_v3 import create_full_system_v3  # bootstrap_v3 moved to backup
# from v3.ui.terminal_ui import TerminalUI as UI  # v3 moved to backup


class ClaudeSenaIntegration:
    """
    Complete integration - SENA IS Claude's core system
    No optional parameters - just transparent operation
    """

    def __init__(self):
        self._system = None
        self._controller = None
        self._genius_mode = False
        self._activation_time = None

    def activate(self) -> Dict[str, Any]:
        """
        Silent activation - SENA is part of the system, not something to announce
        """
        if self._system is None:
            self._system = create_full_system_v3(enable_all=True)
            self._controller = self._system['controller']
            self._activation_time = datetime.now()

        return {"status": "activated", "mode": "transparent"}

    def think_brilliantly(self, problem: str, mode: str = "auto") -> Dict[str, Any]:
        """
        Brilliant thinking - transparent operation
        NO optional parameters - just works
        """
        if not self._controller:
            self.activate()

        return self._controller.think_brilliantly(problem, mode=mode)

    def verify_truth(self, statement: str) -> Dict[str, Any]:
        """
        Truth verification - transparent operation
        NO optional parameters - just works
        """
        if not self._controller:
            self.activate()

        return self._controller.verify_truth(statement)

    def scan_security(self, code: str) -> Dict[str, Any]:
        """
        Security scan - transparent operation
        NO optional parameters - just works
        """
        if not self._controller:
            self.activate()

        return self._controller.scan_security(code)

    def check_constitutional(self, command: str) -> Dict[str, Any]:
        """
        Constitutional check - transparent operation
        NO optional parameters - just works
        """
        if not self._controller:
            self.activate()

        result = self._controller.review(command)
        return {
            'command': command,
            'approved': result.get('approved', True),
            'concerns': result.get('concerns', []),
            'suggestions': result.get('suggestions', [])
        }

    def get_status(self) -> Dict[str, Any]:
        """Get system status"""
        if not self._controller:
            return {'error': 'Not activated', 'active': False}

        status = self._controller.get_status()
        return {
            'active': True,
            'version': '3.0.0',
            'health': status.get('health', {}),
            'config': status.get('config', {}),
            'activation_time': self._activation_time.strftime("%Y-%m-%d %H:%M:%S") if self._activation_time else None
        }

    def toggle_genius_mode(self) -> bool:
        """Toggle genius mode"""
        self._genius_mode = not self._genius_mode
        return self._genius_mode

    # ========================================================================
    # UI METHODS - Only for explicit user requests (dashboard, help, etc.)
    # These are the ONLY methods that show UI - because user explicitly asked
    # ========================================================================

    def show_dashboard(self) -> Dict[str, Any]:
        """Show dashboard - explicit user request for UI"""
        if not self._controller:
            self.activate()

        status = self._controller.get_status()
        config = status.get('config', {})
        metrics = self._controller._metrics

        # Header
        print("\n" + UI.header(
            "SENA CONTROLLER v3.0 - LIVE DASHBOARD",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            width=90
        ))

        # System Information
        print("\n" + UI.section_header("SYSTEM INFORMATION", width=90))

        uptime = UI.format_uptime(metrics['uptime_start']) if 'uptime_start' in metrics else "N/A"
        active_innovations = sum(1 for k, v in config.items() if k.startswith('enable_') and v)

        sys_info = {
            "Version": status['version'],
            "Health": status['health']['current_level'],
            "Uptime": uptime,
            "Active Innovations": f"{active_innovations}/24",
            "Genius Mode": "ON" if self._genius_mode else "OFF"
        }

        print(UI.key_value_box(sys_info, title="System Status", width=90))

        # Performance Metrics
        print("\n" + UI.section_header("PERFORMANCE METRICS", width=90))

        cmd_card = UI.metric_card("Commands", str(metrics.get('commands_processed', 0)), "Processed", width=21)
        allow_card = UI.metric_card("Allowed", str(metrics.get('commands_allowed', 0)), "Approved", width=21)
        deny_card = UI.metric_card("Denied", str(metrics.get('commands_denied', 0)), "Blocked", width=21)
        predict_card = UI.metric_card("Predictions", str(metrics.get('predictions_made', 0)), "Generated", width=21)

        print(UI.side_by_side([cmd_card, allow_card, deny_card, predict_card], spacing=1))

        # Cache Performance
        cache_hits = metrics.get('cache_hits', 0)
        cache_misses = metrics.get('cache_misses', 0)
        total_cache = cache_hits + cache_misses
        hit_rate = (cache_hits / total_cache * 100) if total_cache > 0 else 0

        print("\n  CACHE PERFORMANCE:")
        print("    " + UI.progress_bar(cache_hits, total_cache, width=50, label="Hit Rate"))

        cache_stats = {
            "Total Requests": total_cache,
            "Cache Hits": cache_hits,
            "Cache Misses": cache_misses,
            "Hit Rate": f"{hit_rate:.1f}%"
        }
        print("\n" + UI.key_value_box(cache_stats, title="Cache Statistics", width=90))

        # Brilliance System
        if 'brilliance' in status:
            print("\n" + UI.section_header("BRILLIANCE SYSTEM", width=90))

            brilliance = status['brilliance']
            b_metrics = brilliance['metrics']

            b_rows = [
                ["Brilliant Thoughts", str(b_metrics['brilliant_thoughts'])],
                ["First Principles Used", str(b_metrics['first_principles_used'])],
                ["Hallucinations Prevented", str(b_metrics['hallucinations_prevented'])],
                ["Average Brilliance Score", f"{b_metrics.get('brilliance_avg_score', 0):.1%}"]
            ]

            print(UI.table(
                headers=["Metric", "Value"],
                rows=b_rows,
                widths=[35, 50],
                title="Brilliance Metrics"
            ))

        print("\n" + UI.DOUBLE_HORIZONTAL * 90 + "\n")

        return status

    def show_all_commands(self) -> None:
        """Show all available commands - explicit user request"""
        print("\n" + UI.header(
            "SENA CONTROLLER v3.0 - COMMAND REFERENCE",
            "Complete Command List",
            width=90
        ))

        categories = [
            ("Core System Commands", [
                ("/sena-status", "Show current system status"),
                ("/sena-dashboard", "Display comprehensive live dashboard"),
                ("/sena-help", "Show this help"),
            ]),
            ("Features", [
                ("Brilliant Thinking", "Automatic for complex questions"),
                ("Truth Verification", "Automatic anti-hallucination"),
                ("Security Scanning", "Automatic code analysis"),
                ("Beautiful UI", "Automatic table formatting"),
            ]),
        ]

        for category_name, commands in categories:
            print("\n" + UI.section_header(category_name, width=90))
            cmd_rows = []
            for cmd, desc in commands:
                cmd_rows.append([cmd, desc])

            print(UI.table(
                headers=["Command/Feature", "Description"],
                rows=cmd_rows,
                widths=[25, 60],
                title=category_name
            ))

        print("\n" + UI.DOUBLE_HORIZONTAL * 90 + "\n")


# Global singleton instance
sena = ClaudeSenaIntegration()

# Export
__all__ = ['sena', 'ClaudeSenaIntegration']
