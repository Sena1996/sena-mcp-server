"""
SENA Controller v3.0 - Python Automation Modules

This package contains the Python automation modules that power
SENA's advanced features including auto-formatting, metrics,
session management, and integration automation.

Modules:
    - auto_integration: Automatic format detection and application
    - sena_auto_format: Auto formatting engine (Rule 1-4 enforcement)
    - sena_metrics_mcp: MCP metrics collection and reporting
    - sena_metrics: Analytics and performance tracking
    - session_manager: Session state and coordination
    - sena_clean_output_100: Output cleaning and formatting
    - sena_progress_auto_100: Progress bar automation
    - sena_controller_100: Main controller orchestration
    - claude_sena_integration: Claude Code integration layer
"""

__version__ = "3.0.0"
__all__ = [
    "auto_integration",
    "sena_auto_format",
    "sena_metrics_mcp",
    "sena_metrics",
    "session_manager",
    "sena_clean_output_100",
    "sena_progress_auto_100",
    "sena_controller_100",
    "claude_sena_integration",
]
