#!/usr/bin/env python3
"""
SENA Direct Output Module
Captures SENA output and returns as string for direct embedding in Claude responses
This eliminates need for Bash tool calls
"""

import sys
from pathlib import Path
from io import StringIO
from typing import List, Dict, Any

# Ensure path
controller_path = Path.home() / '.claude' / 'sena_controller_v3.0'
if str(controller_path) not in sys.path:
    sys.path.insert(0, str(controller_path))

from sena_transparent_layer import transparent_sena


def format_table_as_text(headers: List[str], rows: List[List[str]], title: str = "") -> str:
    """
    Get SENA Beautiful UI table as string (no printing)
    Returns the formatted table that Claude can output directly
    """
    return transparent_sena.format_table(headers, rows, title)


def think_as_text(question: str) -> str:
    """
    Get SENA brilliant thinking as formatted text
    Returns the result that Claude can output directly
    """
    result = transparent_sena.think(question)

    # Format the result nicely
    output = []
    output.append(f"\n{'='*70}")
    output.append(f"SENA BRILLIANT THINKING")
    output.append(f"{'='*70}")
    output.append(f"\nQuestion: {question}")
    output.append(f"\nMode: {result.get('mode', 'auto')}")

    if 'insights' in result:
        output.append(f"\n{'─'*70}")
        output.append("INSIGHTS:")
        output.append(f"{'─'*70}")
        for insight in result['insights']:
            output.append(f"  • {insight}")

    if 'reasoning' in result:
        output.append(f"\n{'─'*70}")
        output.append("REASONING:")
        output.append(f"{'─'*70}")
        output.append(f"{result['reasoning']}")

    if 'brilliance_score' in result:
        score = result['brilliance_score']
        output.append(f"\n{'─'*70}")
        output.append(f"Brilliance Score: {score:.1%}")
        output.append(f"Verified: {'✓' if result.get('verified') else '✗'}")
        output.append(f"{'='*70}\n")

    return "\n".join(output)


def verify_fact_as_text(statement: str) -> str:
    """
    Get SENA fact verification as formatted text
    Returns the result that Claude can output directly
    """
    result = transparent_sena.verify_fact(statement)

    output = []
    output.append(f"\n{'='*70}")
    output.append(f"SENA TRUTH VERIFICATION")
    output.append(f"{'='*70}")
    output.append(f"\nStatement: {statement}")
    output.append(f"\nTruth Level: {result.get('truth_level', 'unknown')}")
    output.append(f"Confidence: {result.get('confidence', 0):.1%}")
    output.append(f"Verified: {'✓' if result.get('verified') else '✗'}")

    if result.get('warnings'):
        output.append(f"\n{'─'*70}")
        output.append("WARNINGS:")
        output.append(f"{'─'*70}")
        for warning in result['warnings']:
            output.append(f"  ⚠️  {warning}")

    if result.get('reasoning'):
        output.append(f"\n{'─'*70}")
        output.append("REASONING:")
        output.append(f"{'─'*70}")
        output.append(f"{result['reasoning']}")

    output.append(f"{'='*70}\n")

    return "\n".join(output)


# Export
__all__ = ['format_table_as_text', 'think_as_text', 'verify_fact_as_text']
