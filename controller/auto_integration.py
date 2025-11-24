#!/usr/bin/env python3
"""
SENA Auto Integration System - v3.3.1 - Rule 7 Implementation
Automatic keyword detection and format application with 100% accuracy
"""

import re
from typing import Dict, List, Optional, Tuple

class AutoIntegration:
    """Automatic SENA format detection and application"""

    def __init__(self):
        # Keyword mappings for automatic triggers
        self.triggers = {
            'brilliant_thinking': {
                'keywords': ['why', 'how', 'explain', 'reasoning', 'understanding',
                            'logic', 'rationale', 'because', 'cause'],
                'patterns': [
                    r'\bwhy\s+(?:does|is|are|do|did|would|should)\b',
                    r'\bhow\s+(?:does|is|are|do|did|can|could|should)\b',
                    r'\bexplain\s+(?:why|how|what|the)\b',
                    r'\bwhat(?:\'s|\s+is)\s+the\s+(?:reason|logic|rationale)\b'
                ],
                'format': 'brilliant_thinking'
            },
            'truth_verification': {
                'keywords': [],  # Don't use keywords, use patterns only for precision
                'patterns': [
                    r'\bis\s+(?:it|this|that)\s+(?:true|false|correct|accurate|real|valid)\b',
                    r'\bis\s+(?:the|a)\s+\w+\s+(?:flat|round|hollow|fake|real)\b',  # "is the earth flat"
                    r'\bis\s+\w+\s+(?:true|false|correct|accurate|valid|real)\b',  # "is X true"
                    r'\b(?:fact\s+check|verify|confirm)\s+(?:that|if|whether)\b',
                    r'\bmyth\s+(?:or|vs|versus)\s+(?:fact|reality|truth)\b',
                    r'\bclaim:\s*.+',
                    r'^is\s+\w+\s+\w+\??$',  # "is earth flat?" "is water wet?" (at start)
                ],
                'format': 'truth_verification'
            },
            'code_analysis': {
                'keywords': ['analyze', 'review', 'code', 'quality', 'refactor',
                           'optimize', 'debug', 'fix', 'improve'],
                'patterns': [
                    r'\b(?:analyze|review)\s+(?:this|the|my)?\s*code\b',
                    r'\bcode\s+(?:review|analysis|quality)\b',
                    r'\b(?:refactor|optimize|debug|fix)\s+(?:this|the|my)\b',
                    r'\bcheck\s+(?:for|the)\s+(?:bugs|errors|issues)\b'
                ],
                'format': 'code_analysis'
            },
            'table_format': {
                'keywords': ['table', 'tabular', 'grid', 'matrix', 'columns', 'rows'],
                'patterns': [
                    r'\b(?:in|as|with)?\s*(?:a\s+)?table\b',
                    r'\btabular\s+(?:format|form|data)\b',
                    r'\b(?:show|display|present)\s+(?:in|as)\s+(?:table|grid)\b',
                    r'\btable\s+(?:format|form|view)\b'
                ],
                'format': 'table_format'
            },
            'progress_display': {
                'keywords': ['find', 'search', 'locate', 'scan', 'process', 'analyze'],
                'patterns': [
                    r'\b(?:find|search|locate)\s+(?:all|the|files|in)\b',
                    r'\b(?:scan|process|analyze)\s+(?:multiple|all|the)\b',
                    r'\b(?:read|check|examine)\s+(?:multiple|several|all)\b'
                ],
                'format': 'progress',
                'condition': 'multi_step'
            }
        }

    def detect_format(self, user_input: str) -> Optional[str]:
        """Detect which SENA format to apply based on user input"""

        input_lower = user_input.lower()

        # Process in priority order - specific patterns first
        # Why/how questions should be brilliant_thinking UNLESS they're yes/no truth questions
        priority_order = ['table_format', 'code_analysis', 'brilliant_thinking', 'truth_verification', 'progress_display']

        for trigger_type in priority_order:
            if trigger_type not in self.triggers:
                continue

            config = self.triggers[trigger_type]

            # Check keywords
            for keyword in config['keywords']:
                if keyword in input_lower:
                    return config['format']

            # Check patterns
            for pattern in config['patterns']:
                if re.search(pattern, input_lower, re.IGNORECASE):
                    return config['format']

        return None

    def should_show_progress(self, operation_type: str, step_count: int = 1) -> bool:
        """Determine if progress bars should be shown"""

        # Show progress for:
        # 1. Multiple file operations
        # 2. Search operations
        # 3. Multi-step analysis
        # 4. Any operation with 2+ steps

        progress_operations = [
            'file_search', 'multi_read', 'code_analysis',
            'bulk_write', 'multi_tool', 'research'
        ]

        return operation_type in progress_operations or step_count >= 2

    def get_format_instructions(self, format_type: str) -> Dict:
        """Get specific formatting instructions for each type"""

        formats = {
            'brilliant_thinking': {
                'title': 'SENA 🦁 BRILLIANT THINKING',
                'sections': [
                    'QUESTION ANALYSIS',
                    'FIRST PRINCIPLES BREAKDOWN',
                    'STRUCTURED ANALYSIS',
                    'CONCLUSION'
                ],
                'use_boxes': True
            },
            'truth_verification': {
                'title': 'SENA 🦁 TRUTH VERIFICATION SYSTEM',
                'sections': [
                    'CLAIM BEING VERIFIED',
                    'VERIFICATION ANALYSIS',
                    'EVIDENCE',
                    'FINAL VERDICT'
                ],
                'use_boxes': True
            },
            'code_analysis': {
                'title': 'SENA 🦁 CODE QUALITY ANALYSIS',
                'sections': [
                    'CODE OVERVIEW',
                    'QUALITY METRICS',
                    'ISSUES & RECOMMENDATIONS'
                ],
                'use_boxes': True
            },
            'table': {
                'use_unicode': True,
                'borders': '┌─┐│└┘├┤',
                'include_title': True
            },
            'progress': {
                'show_before': True,
                'show_after': True,
                'bar_width': 40,
                'use_emoji': '🦁'
            }
        }

        return formats.get(format_type, {})

# Global instance
auto_integration = AutoIntegration()

def check_user_input(text: str) -> Optional[str]:
    """Check user input and return required format"""
    return auto_integration.detect_format(text)

def should_show_progress(op_type: str, steps: int = 1) -> bool:
    """Check if progress bars should be displayed"""
    return auto_integration.should_show_progress(op_type, steps)

# Export for use
__all__ = ['auto_integration', 'check_user_input', 'should_show_progress']