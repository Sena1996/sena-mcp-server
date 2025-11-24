#!/usr/bin/env python3
"""
SENA Metrics MCP Server - v3.5.2 OPTIMIZED
MCP wrapper that delegates to standalone sena_metrics module
Code duplication eliminated: 441 lines → 50 lines (-88%)
"""

from mcp.server.fastmcp import FastMCP
from sena_metrics import (
    get_sena_health,
    get_innovation_metrics,
    get_test_results,
    check_sena_config,
    get_phase_status
)

# Initialize FastMCP server
mcp = FastMCP("SENA Metrics")


@mcp.tool()
def sena_health() -> dict:
    """
    Get comprehensive SENA Controller health status

    Returns complete health metrics including component status,
    version information, test coverage, and background processes.
    """
    return get_sena_health()


@mcp.tool()
def sena_innovation_metrics() -> dict:
    """
    Get SENA innovation metrics and completion status

    Returns detailed metrics for all 24 innovations including
    implementation status, test coverage, and quality metrics.
    """
    return get_innovation_metrics()


@mcp.tool()
def sena_test_results() -> dict:
    """
    Get comprehensive test results for all SENA components

    Returns test status, coverage, and pass/fail metrics for
    all controller modules, hooks, and integration tests.
    """
    return get_test_results()


@mcp.tool()
def sena_config_check() -> dict:
    """
    Validate SENA configuration and integration with Claude Code

    Returns configuration status, settings validation, hook setup,
    and MCP server registration status.
    """
    return check_sena_config()


@mcp.tool()
def sena_phase_status() -> dict:
    """
    Get development phase status and completion metrics

    Returns status for all three development phases including
    completion percentage, feature counts, and remaining work.
    """
    return get_phase_status()


def main():
    """Main entry point for SENA Metrics MCP server"""
    mcp.run()


if __name__ == "__main__":
    main()
