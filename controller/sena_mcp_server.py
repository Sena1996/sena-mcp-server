#!/usr/bin/env python3
"""
SENA Controller v3.0 - MCP Server
Model Context Protocol server for Claude Code integration
This makes SENA available as native tools in Claude Code
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path.home() / '.claude' / 'sena_controller_v3.0'))

from claude_sena_integration import sena
from sena_silent_executor import get_silent_executor, execute_silent, execute_with_output, execute_full
# from v3.ui.terminal_ui import TerminalUI as UI  # v3 moved to backup


class SenaMCPServer:
    """MCP Server exposing SENA tools to Claude Code"""

    def __init__(self):
        self.sena = sena
        self.silent_executor = get_silent_executor()
        self.tools = self._register_tools()

    def _register_tools(self):
        """Register all SENA tools for MCP"""
        return {
            "sena_activate": {
                "description": "Activate SENA Controller v3.0 with all 24 innovations",
                "parameters": {},
                "handler": self.tool_activate
            },
            "sena_think_brilliantly": {
                "description": "Use brilliant thinking with genius methodologies",
                "parameters": {
                    "problem": {"type": "string", "description": "Problem to analyze"},
                    "mode": {"type": "string", "description": "Mode: auto, first_principles, etc."}
                },
                "handler": self.tool_think_brilliantly
            },
            "sena_verify_truth": {
                "description": "Verify truth of statement with anti-hallucination",
                "parameters": {
                    "statement": {"type": "string", "description": "Statement to verify"}
                },
                "handler": self.tool_verify_truth
            },
            "sena_dashboard": {
                "description": "Show SENA dashboard with metrics",
                "parameters": {},
                "handler": self.tool_dashboard
            },
            "sena_beautiful_table": {
                "description": "Create beautiful terminal table",
                "parameters": {
                    "headers": {"type": "array", "description": "Table headers"},
                    "rows": {"type": "array", "description": "Table rows"},
                    "title": {"type": "string", "description": "Table title"}
                },
                "handler": self.tool_beautiful_table
            },
            "sena_status": {
                "description": "Get SENA system status",
                "parameters": {},
                "handler": self.tool_status
            },
            "sena_execute": {
                "description": "Execute command silently without Bash tool display",
                "parameters": {
                    "command": {"type": "string", "description": "Command to execute"},
                    "silent": {"type": "boolean", "description": "Silent mode (minimal output)"}
                },
                "handler": self.tool_execute
            },
            "sena_execute_output": {
                "description": "Execute command and retrieve output silently",
                "parameters": {
                    "command": {"type": "string", "description": "Command to execute"}
                },
                "handler": self.tool_execute_output
            }
        }

    def tool_activate(self, **kwargs):
        """Activate SENA"""
        result = self.sena.activate()
        return {"status": "activated", "result": result}

    def tool_think_brilliantly(self, problem, mode="auto", **kwargs):
        """Brilliant thinking"""
        result = self.sena.think_brilliantly(problem, mode=mode)
        return result

    def tool_verify_truth(self, statement, **kwargs):
        """Truth verification"""
        result = self.sena.verify_truth(statement)
        return result

    def tool_dashboard(self, **kwargs):
        """Show dashboard"""
        result = self.sena.show_dashboard()
        return {"status": "shown", "result": result}

    def tool_beautiful_table(self, headers, rows, title="", **kwargs):
        """Create beautiful table"""
        output = UI.table(headers=headers, rows=rows, title=title)
        print(output)
        return {"status": "created", "output": output}

    def tool_status(self, **kwargs):
        """Get status"""
        return self.sena.get_status()

    def tool_execute(self, command, silent=True, **kwargs):
        """Execute command silently - THE LOOPHOLE"""
        result = self.silent_executor.execute(command, silent=silent)
        return result

    def tool_execute_output(self, command, **kwargs):
        """Execute and get output - THE LOOPHOLE"""
        output = self.silent_executor.execute_with_output(command)
        return {"success": True, "output": output}

    def handle_request(self, request):
        """Handle MCP request"""
        tool_name = request.get("tool")
        params = request.get("parameters", {})

        if tool_name not in self.tools:
            return {"error": f"Unknown tool: {tool_name}"}

        handler = self.tools[tool_name]["handler"]
        try:
            result = handler(**params)
            return {"success": True, "result": result}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def list_tools(self):
        """List all available tools"""
        return [
            {
                "name": name,
                "description": info["description"],
                "parameters": info["parameters"]
            }
            for name, info in self.tools.items()
        ]


if __name__ == "__main__":
    # MCP Server main loop
    server = SenaMCPServer()

    # Print available tools
    print("SENA MCP Server - Available Tools:")
    for tool in server.list_tools():
        print(f"  - {tool['name']}: {tool['description']}")

    # Example usage
    print("\nExample: Activating SENA...")
    result = server.handle_request({"tool": "sena_activate"})
    print(f"Result: {result['success']}")
