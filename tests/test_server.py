"""
Tests for SENA MCP Server
"""

import pytest
from sena_mcp.server import (
    sena_brilliant_thinking,
    sena_verify_truth,
    sena_format_table,
    sena_analyze_code,
    sena_get_health,
)


def test_brilliant_thinking():
    """Test brilliant thinking tool"""
    result = sena_brilliant_thinking(
        problem="Why is performance degrading?",
        methodology="root_cause"
    )
    assert result["status"] == "success"
    assert "SENA 🦁 BRILLIANT THINKING" in result["analysis"]
    assert result["methodology"] == "root_cause"


def test_verify_truth():
    """Test truth verification tool"""
    result = sena_verify_truth(
        statement="Python is a dynamically typed language",
        require_evidence=True
    )
    assert result["status"] == "success"
    assert "TRUTH VERIFICATION" in result["analysis"]
    assert result["statement"] == "Python is a dynamically typed language"


def test_format_table():
    """Test table formatting tool"""
    result = sena_format_table(
        headers=["Name", "Age", "City"],
        rows=[
            ["Alice", "30", "NYC"],
            ["Bob", "25", "LA"]
        ],
        title="User Data"
    )
    assert result["status"] == "success"
    assert result["rows_count"] == 2
    assert result["columns_count"] == 3
    assert "┌" in result["table"]
    assert "│" in result["table"]


def test_analyze_code():
    """Test code analysis tool"""
    code = '''
def hello():
    print("Hello, World!")
'''
    result = sena_analyze_code(
        code=code,
        language="python",
        focus="all"
    )
    assert result["status"] == "success"
    assert result["language"] == "python"
    assert result["lines"] > 0
    assert "CODE QUALITY ANALYSIS" in result["analysis"]


def test_get_health():
    """Test health check tool"""
    result = sena_get_health()
    assert result["status"] == "healthy"
    assert result["version"] == "1.0.0"
    assert result["mode"] == "mcp"
    assert "brilliant_thinking" in result["components"]
    assert result["components"]["brilliant_thinking"] == "operational"
