# SENA Slash Commands

**Version:** 2.0.0
**Purpose:** Essential slash commands for Claude Code CLI

---

## Overview

This directory contains slash commands that extend SENA's capabilities in Claude Code CLI. These commands provide quick access to SENA features and utilities.

**Note:** This is a curated subset of 10 essential commands. The full SENA v3.3.1 installation includes 122+ commands covering various development tasks.

---

## Installation

### Claude Code CLI

Copy commands to your Claude config directory:

```bash
cp commands/*.md ~/.claude/commands/
```

Or use the install script (recommended):

```bash
./install.sh
```

---

## Available Commands

### Core SENA Commands

#### `/activate-sena`
**Purpose:** Activate SENA controller features

**Usage:**
```
/activate-sena
```

**Actions:**
- Enables SENA always-on mode
- Activates autonomous skills
- Initializes controller modules
- Sets feature flags

---

#### `/deactivate-sena`
**Purpose:** Deactivate SENA controller features

**Usage:**
```
/deactivate-sena
```

**Actions:**
- Disables SENA always-on mode
- Deactivates autonomous skills
- Clears feature flags
- Restores default Claude behavior

---

#### `/check-sena`
**Purpose:** Check SENA system status

**Usage:**
```
/check-sena
```

**Output:**
- SENA version and mode
- Feature status (enabled/disabled)
- Controller module status
- Configuration file locations
- MCP server status
- Hook installation status

---

#### `/sena-health`
**Purpose:** Comprehensive health check

**Usage:**
```
/sena-health
```

**Output:**
- System health status
- Component operational status
- Performance metrics
- Configuration validation
- Integration status

---

#### `/sena-help`
**Purpose:** SENA documentation and help

**Usage:**
```
/sena-help [topic]
```

**Topics:**
- `rules` - SENA operational rules
- `skills` - Autonomous skills guide
- `commands` - Slash commands list
- `mcp` - MCP server usage
- `config` - Configuration guide

---

#### `/sena-capabilities`
**Purpose:** List all SENA capabilities

**Usage:**
```
/sena-capabilities
```

**Output:**
- MCP tools available
- MCP resources available
- Autonomous skills
- Controller modules
- Slash commands
- Feature coverage percentage

---

#### `/sena-always-on`
**Purpose:** Enable always-on mode (SENA 🦁 prefix)

**Usage:**
```
/sena-always-on
```

**Effect:**
- Creates `~/.claude/.sena_always_on` flag file
- Every response starts with "SENA 🦁"
- Enforced via hooks

---

#### `/sena-always-off`
**Purpose:** Disable always-on mode

**Usage:**
```
/sena-always-off
```

**Effect:**
- Removes `~/.claude/.sena_always_on` flag file
- Normal response format
- No mandatory prefix

---

### Development Commands

#### `/deep-think`
**Purpose:** Deep analysis with extended thinking

**Usage:**
```
/deep-think [problem or question]
```

**Features:**
- Extended reasoning
- First principles analysis
- Multiple methodology consideration
- Comprehensive problem breakdown
- Structured conclusions

---

#### `/analyze-code`
**Purpose:** Comprehensive code analysis

**Usage:**
```
/analyze-code [file or code block]
```

**Analysis:**
- Code quality metrics
- Performance assessment
- Security vulnerabilities
- Best practices compliance
- Improvement suggestions

---

## Command Usage Patterns

### Basic Usage
```
/command-name
```

### With Arguments
```
/command-name argument1 argument2
```

### With Code
````
/analyze-code
```python
def example():
    pass
```
````

---

## Creating Custom Commands

Create a markdown file in `~/.claude/commands/`:

**File:** `~/.claude/commands/my-command.md`

**Content:**
```markdown
Your command instructions here.

This text will be injected into the conversation when /my-command is used.
```

**Usage:**
```
/my-command
```

---

## Command Conventions

### Naming
- Use kebab-case: `my-command.md`
- Descriptive names
- Avoid special characters

### Content
- Clear instructions
- Specific actions
- Expected output format
- Examples when helpful

---

## Full Command List (SENA v3.3.1)

The complete SENA installation includes 122+ commands across categories:

**SENA Core:** (10 commands - **included here**)
- activate-sena, deactivate-sena, check-sena
- sena-health, sena-help, sena-capabilities
- sena-always-on, sena-always-off
- deep-think, analyze-code

**Development:** (30+ commands)
- API architecture, database tuning
- Performance optimization, security analysis
- Code generation, refactoring tools

**Testing:** (15+ commands)
- Test generation, coverage analysis
- Integration testing, E2E testing

**DevOps:** (20+ commands)
- CI/CD, deployment, monitoring
- Container management, infrastructure

**Documentation:** (10+ commands)
- README generation, API docs
- Changelog, architecture diagrams

**Utilities:** (40+ commands)
- Code formatting, linting
- Dependency management, metrics
- Various developer tools

---

## Integration with MCP Server

Commands can interact with MCP tools:

```markdown
Use the sena_brilliant_thinking MCP tool to analyze:
[problem description]
```

---

## Troubleshooting

### Command not found
```bash
# Check if file exists
ls ~/.claude/commands/my-command.md

# Verify file permissions
chmod +r ~/.claude/commands/my-command.md
```

### Command not working
```bash
# Check file content
cat ~/.claude/commands/my-command.md

# Ensure .md extension
mv ~/.claude/commands/my-command ~/.claude/commands/my-command.md
```

---

## Adding More Commands

To get the full set of 122+ commands from SENA v3.3.1:

```bash
# Copy all commands from SENA installation
cp ~/.claude/commands/*.md /path/to/sena-mcp-server/commands/

# Or selectively copy categories
cp ~/.claude/commands/sena-*.md /path/to/sena-mcp-server/commands/
cp ~/.claude/commands/api-*.md /path/to/sena-mcp-server/commands/
```

---

*Updated: November 24, 2025*
*SENA v2.0.0 Commands*
*10 essential commands included (122+ available in full SENA)*
