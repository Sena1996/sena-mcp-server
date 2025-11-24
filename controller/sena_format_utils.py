#!/usr/bin/env python3
"""
SENA Format Utilities - Reusable formatting functions
Eliminates 200+ lines of repeated box drawing code
"""

from typing import List, Dict, Optional


def create_title_box(title: str, width: int = 64, emoji: str = "🦁") -> List[str]:
    """
    Generate SENA formatted title box

    Args:
        title: Title text to display
        width: Width of the box (default 64)
        emoji: Emoji to display in title (default 🦁)

    Returns:
        List of strings forming the box
    """
    top = "╔" + "═" * width + "╗"
    empty = "║" + " " * width + "║"

    # Center title with emoji
    title_text = f"SENA {emoji} {title}"
    title_line = "║" + title_text.center(width) + "║"

    bottom = "╚" + "═" * width + "╝"

    return [top, empty, title_line, empty, bottom]


def create_section_separator(title: str, width: int = 64) -> List[str]:
    """
    Generate section separator with title

    Args:
        title: Section title
        width: Width of separator (default 64)

    Returns:
        List of strings forming the separator
    """
    line = "═" * width
    title_line = f"  {title}"
    return [line, title_line, line]


def create_data_table(headers: List[str], rows: List[List[str]],
                      title: Optional[str] = None,
                      emoji: Optional[str] = None) -> List[str]:
    """
    Generate Unicode box-drawing table

    Args:
        headers: List of column headers
        rows: List of rows (each row is a list of cell values)
        title: Optional title to display above table
        emoji: Optional emoji for title

    Returns:
        List of strings forming the table
    """
    output = []

    # Add title if provided
    if title:
        title_emoji = emoji if emoji else "📊"
        table_width = 60
        top = "╔" + "═" * table_width + "╗"
        title_line = "║" + f" {title_emoji} {title}".center(table_width) + "║"
        bottom = "╚" + "═" * table_width + "╝"
        output.extend([top, title_line, bottom, ""])

    # Calculate column widths (min 15 chars per column)
    col_widths = []
    for i in range(len(headers)):
        max_width = max(
            len(headers[i]),
            max((len(str(row[i])) for row in rows), default=0)
        )
        col_widths.append(max(max_width + 2, 15))

    total_width = sum(col_widths) + len(headers) + 1

    # Top border
    output.append("┌" + "─" * (total_width - 2) + "┐")

    # Headers
    header_line = "│"
    for i, header in enumerate(headers):
        header_line += f" {header:<{col_widths[i]-1}}│"
    output.append(header_line)

    # Separator
    output.append("├" + "─" * (total_width - 2) + "┤")

    # Rows
    for row in rows:
        row_line = "│"
        for i, cell in enumerate(row):
            row_line += f" {str(cell):<{col_widths[i]-1}}│"
        output.append(row_line)

    # Bottom border
    output.append("└" + "─" * (total_width - 2) + "┘")

    return output


def create_progress_bar(task_name: str, progress: int,
                       max_progress: int = 100, width: int = 20,
                       emoji: str = "🦁") -> str:
    """
    Generate progress bar with SENA emoji

    Args:
        task_name: Name of the task
        progress: Current progress value
        max_progress: Maximum progress value (default 100)
        width: Width of progress bar in characters (default 20)
        emoji: Emoji to use (default 🦁)

    Returns:
        Formatted progress bar string
    """
    percentage = int((progress / max_progress) * 100)
    filled = int((progress / max_progress) * width)

    # Build progress bar
    bar = "█" * filled
    empty = "░" * (width - filled)

    # Add emoji at progress position or at end if complete
    if percentage >= 100:
        status = f"{bar}{emoji} ✅"
    elif filled > 0:
        status = f"{bar}{emoji}{empty}"
    else:
        status = f"{emoji}{empty}"

    return f"[{status}] {percentage}% - {task_name}"


def create_multi_progress(tasks: List[Dict[str, any]],
                         title: Optional[str] = None) -> List[str]:
    """
    Generate multiple progress bars with optional title

    Args:
        tasks: List of dicts with keys: name, progress, max_progress (optional)
        title: Optional title for progress display

    Returns:
        List of strings forming the progress display
    """
    output = []

    # Add title if provided
    if title:
        output.extend(create_title_box(title, width=64, emoji="🦁"))
        output.append("")

    # Calculate max task name length for alignment
    max_name_len = max(len(task['name']) for task in tasks)
    total_width = 64
    bar_width = total_width - max_name_len - 15  # Space for name, percentage, etc.

    # Top border
    output.append("┌" + "─" * (total_width - 2) + "┐")

    # Progress bars
    for task in tasks:
        name = task['name']
        progress = task['progress']
        max_progress = task.get('max_progress', 100)

        percentage = int((progress / max_progress) * 100)
        filled = int((progress / max_progress) * bar_width)

        # Build progress bar
        bar = "█" * filled
        empty = "░" * (bar_width - filled)

        # Add emoji and status
        if percentage >= 100:
            emoji_pos = f"{bar}🦁"
            status = " ✅"
        elif filled > 0:
            emoji_pos = f"{bar}🦁{empty}"
            status = ""
        else:
            emoji_pos = f"🦁{empty}"
            status = ""

        # Format line
        line = f"│ {name:<{max_name_len}} [{emoji_pos}] {percentage:3d}%{status}{' ' * (total_width - max_name_len - bar_width - 16)}│"
        output.append(line[:total_width-1] + "│")  # Ensure exact width

    # Bottom border
    output.append("└" + "─" * (total_width - 2) + "┘")

    return output


def create_status_box(status_items: List[Dict[str, str]],
                      title: str = "STATUS") -> List[str]:
    """
    Generate status information box

    Args:
        status_items: List of dicts with keys: label, value, status (optional)
        title: Title for the box

    Returns:
        List of strings forming the status box
    """
    output = []

    # Title
    output.extend(create_section_separator(title, width=64))
    output.append("")

    # Calculate widths
    max_label_len = max(len(item['label']) for item in status_items)
    total_width = 64

    # Top border
    output.append("┌" + "─" * (total_width - 2) + "┐")

    # Status items
    for item in status_items:
        label = item['label']
        value = item['value']
        status = item.get('status', '')

        # Add status emoji if provided
        if status == 'success':
            value = f"✅ {value}"
        elif status == 'error':
            value = f"❌ {value}"
        elif status == 'warning':
            value = f"⚠️  {value}"

        # Format line with proper spacing
        line = f"│ {label:<{max_label_len}} │ {value:<{total_width - max_label_len - 8}}│"
        output.append(line[:total_width-1] + "│")  # Ensure exact width

    # Bottom border
    output.append("└" + "─" * (total_width - 2) + "┘")

    return output


# Convenience function for common SENA titles
def sena_title(title: str) -> List[str]:
    """Shorthand for creating SENA title boxes"""
    return create_title_box(title, width=64, emoji="🦁")


# Convenience function for section headers
def section(title: str) -> List[str]:
    """Shorthand for creating section separators"""
    return create_section_separator(title, width=64)


if __name__ == "__main__":
    # Test the utility functions
    print("\n".join(sena_title("FORMAT UTILITIES TEST")))
    print()
    print("\n".join(section("TITLE BOX TEST")))
    print()
    print("\n".join(create_data_table(
        ["Property", "Value"],
        [["Test 1", "Value 1"], ["Test 2", "Value 2"]],
        title="TEST TABLE",
        emoji="📊"
    )))
    print()
    print(create_progress_bar("Processing", 75, 100))
    print()
    print("\n".join(create_multi_progress([
        {"name": "Task 1", "progress": 100, "max_progress": 100},
        {"name": "Task 2", "progress": 60, "max_progress": 100},
        {"name": "Task 3", "progress": 0, "max_progress": 100}
    ], title="TASK PROGRESS")))
