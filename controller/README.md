# SENA Controller Modules

**Version:** 3.0.0
**Purpose:** Python automation modules for advanced SENA features

---

## Overview

This directory contains the Python modules that power SENA's autonomous and automation capabilities. These modules work alongside the MCP server to provide advanced features like auto-formatting, metrics collection, session management, and integration automation.

## Modules

### Core Integration

#### `auto_integration.py` (6.8KB)
**Purpose:** Automatic format detection and application (Rule 7)

**Features:**
- Detects user input patterns (table, why/how, fact check, code analysis)
- Automatically selects appropriate SENA format
- Trigger word detection system
- Integration with all SENA formatting rules

**Functions:**
- `check_user_input(message)` - Returns format needed
- `should_show_progress(operations)` - Determines if progress bars needed
- `get_trigger_keywords()` - Returns all trigger patterns

---

#### `claude_sena_integration.py` (8.5KB)
**Purpose:** Claude Code CLI integration layer

**Features:**
- Bridges SENA controller with Claude Code
- Manages hook execution flow
- Coordinates tool permissions
- Session state synchronization

**Functions:**
- `initialize_sena()` - Sets up SENA in Claude Code session
- `sync_permissions()` - Syncs tool permissions
- `handle_hook_result()` - Processes hook outputs

---

### Formatting & Output

#### `sena_auto_format.py` (18KB)
**Purpose:** Automatic formatting engine (Rules 1-4 enforcement)

**Features:**
- Beautiful table generation (Rule 1)
- Brilliant thinking format (Rule 2)
- Truth verification format (Rule 3)
- Code analysis format (Rule 4)
- Unicode box-drawing automation
- Output template management

**Classes:**
- `TableFormatter` - Generates Unicode tables
- `ThinkingFormatter` - Creates brilliant thinking output
- `VerificationFormatter` - Truth verification templates
- `CodeFormatter` - Code analysis templates

**Functions:**
- `format_table(data, title)` - Creates formatted table
- `format_thinking(problem, methodology)` - Brilliant thinking output
- `format_verification(claim)` - Truth verification output
- `format_code_analysis(code, language)` - Code analysis output

---

#### `sena_clean_output_100.py` (6.0KB)
**Purpose:** Output cleaning and sanitization (Rule 5)

**Features:**
- Removes tool invocation details
- Cleans "Searching...", "Looking for..." phrases
- Strips technical implementation details
- Ensures clean, professional output

**Functions:**
- `clean_output(text)` - Sanitizes output text
- `remove_tool_calls(text)` - Strips Bash/tool references
- `remove_preamble(text)` - Removes unnecessary preambles

---

#### `sena_progress_auto_100.py` (9.1KB)
**Purpose:** Progress bar automation (Rule 6)

**Features:**
- Automatic progress bar generation
- Multi-task progress tracking
- Unicode progress bar rendering
- SENA 🦁 emoji integration

**Classes:**
- `ProgressBar` - Single progress bar generator
- `MultiProgress` - Multiple task progress tracker

**Functions:**
- `create_progress(task, percent)` - Generates progress bar
- `multi_task_progress(tasks)` - Creates multi-task display
- `format_progress_box(title, tasks)` - Full progress display

---

### Metrics & Analytics

#### `sena_metrics_mcp.py` (14KB - Executable)
**Purpose:** MCP metrics collection and reporting

**Features:**
- Tool usage tracking
- Resource access analytics
- Performance metrics
- Session statistics
- MCP protocol compliance monitoring

**Classes:**
- `MCPMetricsCollector` - Collects MCP-specific metrics
- `ToolUsageTracker` - Tracks tool invocation patterns
- `ResourceAccessTracker` - Monitors resource usage

**Functions:**
- `collect_metrics()` - Gathers current metrics
- `report_usage()` - Generates usage report
- `track_tool_call(tool_name)` - Records tool invocation

---

#### `sena_metrics.py` (14KB)
**Purpose:** General analytics and performance tracking

**Features:**
- Session performance metrics
- Response time tracking
- Format usage statistics
- Skill activation rates
- Error tracking and reporting

**Classes:**
- `MetricsCollector` - Main metrics aggregator
- `PerformanceTracker` - Response time tracking
- `UsageAnalytics` - Usage pattern analysis

**Functions:**
- `track_response_time(duration)` - Records response times
- `track_format_usage(format_type)` - Records format applications
- `generate_report()` - Creates analytics report

---

### Session Management

#### `session_manager.py` (6.9KB)
**Purpose:** Session state and coordination

**Features:**
- Session lifecycle management
- State persistence
- Configuration loading
- Multi-session coordination
- Cleanup and resource management

**Classes:**
- `SessionManager` - Main session coordinator
- `SessionState` - Session state container
- `ConfigLoader` - Configuration management

**Functions:**
- `start_session()` - Initializes new session
- `load_config()` - Loads SENA configuration
- `save_state()` - Persists session state
- `cleanup()` - Cleans up resources

---

### Controller Orchestration

#### `sena_controller_100.py` (5.9KB)
**Purpose:** Main controller orchestration

**Features:**
- Coordinates all SENA modules
- Enforces operational rules
- Manages feature toggles
- Integrates with MCP server

**Classes:**
- `SENAController` - Main orchestrator
- `RuleEnforcer` - Rule compliance checker

**Functions:**
- `initialize()` - Sets up SENA controller
- `enforce_rules()` - Applies all SENA rules
- `coordinate_modules()` - Manages module interactions

---

## Usage

### Basic Integration

```python
from controller import auto_integration, sena_auto_format

# Detect format needed
format_type = auto_integration.check_user_input("give me Mars info in table")

# Apply formatting
if format_type == "table":
    output = sena_auto_format.format_table(data, title="Mars Information")
```

### Metrics Collection

```python
from controller import sena_metrics

# Track tool usage
sena_metrics.track_tool_call("sena_brilliant_thinking")

# Generate report
report = sena_metrics.generate_report()
```

### Session Management

```python
from controller import session_manager

# Start session
session = session_manager.start_session()

# Load configuration
config = session_manager.load_config()
```

---

## Configuration

These modules read configuration from:
- `~/.claude/sena_skills.json` - Skills configuration
- `~/.claude/CLAUDE.md` - Operational rules
- `~/.claude/settings.json` - Global settings
- `~/.claude/.sena_*` - Feature flags

---

## Dependencies

**Required:**
- Python 3.10+
- No external dependencies (stdlib only)

**Optional:**
- MCP Python SDK (for metrics integration)
- FastMCP (for server integration)

---

## Integration with MCP Server

These modules integrate with the MCP server (`src/sena_mcp/server.py`):

1. **Auto Integration:** Detects patterns in tool calls
2. **Formatting:** Provides output templates for tools
3. **Metrics:** Tracks tool usage and performance
4. **Session:** Manages server state

---

## Testing

```bash
# Run controller tests
python -m pytest tests/controller/

# Test individual modules
python controller/auto_integration.py
python controller/sena_metrics.py
```

---

## Module Summary

| Module | Size | Purpose | Key Feature |
|--------|------|---------|-------------|
| auto_integration | 6.8KB | Format detection | Rule 7 automation |
| sena_auto_format | 18KB | Formatting engine | Rules 1-4 templates |
| sena_metrics_mcp | 14KB | MCP metrics | Tool tracking |
| sena_metrics | 14KB | Analytics | Performance tracking |
| session_manager | 6.9KB | Session control | State management |
| sena_clean_output_100 | 6.0KB | Output cleaning | Rule 5 enforcement |
| sena_progress_auto_100 | 9.1KB | Progress bars | Rule 6 automation |
| sena_controller_100 | 5.9KB | Orchestration | Module coordination |
| claude_sena_integration | 8.5KB | CLI integration | Hook coordination |

**Total:** 9 modules, ~90KB of Python code

---

*Updated: November 24, 2025*
*SENA Controller v3.0*
*Part of: SENA MCP Server v2.0.0*
