# SENA Configuration Files

This directory contains configuration templates for SENA Controller v3.0.

---

## Configuration Files

### `CLAUDE.md.template`
**Purpose:** Main operational rules for SENA (Claude Code CLI)

**Usage:**
```bash
cp config/CLAUDE.md.template ~/.claude/CLAUDE.md
```

**Contains:**
- Rule 0: SENA Always-On Mode (mandatory prefix)
- Rule 1: Tabular Data formatting
- Rule 2: Complex Questions (Brilliant Thinking)
- Rule 3: Truth Verification
- Rule 4: Code Analysis
- Rule 5: Output Display (clean formatting)
- Rule 6: Progress Display automation
- Rule 7: Automatic System Integration
- Rule 8: GitHub Commits (no Claude credits)

**Note:** This file enforces SENA's operational behavior in Claude Code CLI

---

### `sena_skills.json.example`
**Purpose:** Skills configuration for Phase 3 Autonomous Skills

**Usage:**
```bash
cp config/sena_skills.json.example ~/.claude/sena_skills.json
# Then customize settings
```

**Contains:**
- Auto Code Review configuration
- Auto Optimize settings
- Auto Security Scan preferences
- Reasoning hooks configuration
- Proactive patterns settings
- Global skill settings

**Example Configuration:**
```json
{
  "version": "3.3.1",
  "phase": 3,
  "autonomous_skills": {
    "auto_code_review": {
      "enabled": true,
      "min_lines": 50,
      "confidence_threshold": 0.8,
      "strictness": "balanced",
      "frequency_limit": "once_per_file_per_session"
    },
    "auto_optimize": {
      "enabled": true,
      "min_complexity": "O(n^2)",
      "min_improvement_ratio": 2,
      "auto_apply": false,
      "show_benchmarks": true
    },
    "auto_security_scan": {
      "enabled": true,
      "min_severity": "medium",
      "owasp_coverage": true,
      "auto_fix": false,
      "show_attack_scenarios": true
    }
  },
  "global_settings": {
    "quiet_mode": false,
    "max_suggestions_per_session": 10,
    "learn_from_feedback": true
  }
}
```

---

## MCP Configuration

For MCP server configuration (Claude Desktop), use:

**File:** `~/.claude/settings.json` (or wherever your Claude Desktop config is)

**Add SENA MCP server:**
```json
{
  "mcpServers": {
    "sena": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/sena-mcp-server",
        "run",
        "sena-mcp-server"
      ]
    }
  }
}
```

---

## Installation Workflow

### For Claude Desktop (MCP Only)
```bash
# 1. Clone repository
git clone https://github.com/Sena1996/sena-mcp-server.git
cd sena-mcp-server

# 2. Install
./install.sh

# 3. Configure Claude Desktop
# Add MCP server to settings.json (see above)

# 4. Restart Claude Desktop
```

### For Claude Code CLI (Full SENA)
```bash
# 1. Clone repository
git clone https://github.com/Sena1996/sena-mcp-server.git
cd sena-mcp-server

# 2. Install MCP server
./install.sh

# 3. Install configuration
cp config/CLAUDE.md.template ~/.claude/CLAUDE.md
cp config/sena_skills.json.example ~/.claude/sena_skills.json

# 4. Configure hooks (already in ~/.claude/hooks/)
# Hooks are referenced in ~/.claude/settings.json

# 5. Restart Claude Code
```

---

## Configuration Priority

1. **Feature Flags** (highest priority)
   - `~/.claude/.sena_always_on`
   - `~/.claude/.sena_100_percent_mode`
   - `~/.claude/.sena_auto_progress_100`
   - `~/.claude/.sena_clean_output_100`

2. **CLAUDE.md Rules**
   - Operational rules (what SENA must do)
   - Format specifications
   - Enforcement requirements

3. **sena_skills.json**
   - Skill-specific settings
   - Thresholds and preferences
   - Feature toggles

4. **settings.json**
   - Global Claude Code settings
   - Hook configurations
   - MCP server list

---

## Customization

### Enable/Disable Features

**Disable a skill:**
```json
{
  "autonomous_skills": {
    "auto_code_review": {
      "enabled": false  // Disable code review
    }
  }
}
```

**Adjust thresholds:**
```json
{
  "autonomous_skills": {
    "auto_code_review": {
      "min_lines": 100  // Only trigger for 100+ lines
    }
  }
}
```

**Quiet mode:**
```json
{
  "global_settings": {
    "quiet_mode": true,  // Minimal interruptions
    "max_suggestions_per_session": 3
  }
}
```

---

## Environment Variables

SENA Controller modules respect these environment variables:

- `SENA_MODE` - Operation mode (mcp, cli, full)
- `SENA_DEBUG` - Enable debug logging (true/false)
- `SENA_CONFIG_DIR` - Custom config directory (default: ~/.claude)
- `SENA_QUIET` - Quiet mode override (true/false)

**Example:**
```bash
export SENA_MODE=full
export SENA_DEBUG=true
```

---

## Troubleshooting

### CLAUDE.md not applying
```bash
# Check file location
ls -la ~/.claude/CLAUDE.md

# Verify hooks are configured
grep "user-prompt-submit" ~/.claude/settings.json
```

### Skills not triggering
```bash
# Check skills config
cat ~/.claude/sena_skills.json

# Verify enabled status
jq '.autonomous_skills.auto_code_review.enabled' ~/.claude/sena_skills.json
```

### MCP server not starting
```bash
# Test server directly
cd /path/to/sena-mcp-server
uv run sena-mcp-server

# Check MCP configuration
cat ~/.claude/settings.json | jq '.mcpServers.sena'
```

---

*Updated: November 24, 2025*
*SENA v2.0.0 Configuration*
