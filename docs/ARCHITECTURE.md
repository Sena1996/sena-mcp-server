# SENA MCP Server - Architecture Documentation

**Last Updated:** November 24, 2025
**Version:** 1.1.0
**Repository:** https://github.com/Sena1996/sena-mcp-server

---

## Overview

SENA (Systematic Enhanced Natural Analysis) MCP Server is a Model Context Protocol implementation that extends Claude with advanced intelligence capabilities, knowledge bases, and enforcement hooks for CLI environments.

### Design Philosophy

1. **Universal Tools** - MCP tools work in both Claude Desktop (GUI) and Claude Code (CLI)
2. **Persistent Knowledge** - Knowledge bases accessible as MCP resources across all sessions
3. **Clean Separation** - MCP for intelligence, Hooks for CLI behavior enforcement
4. **Cross-Platform** - Works on macOS, Linux, and Windows
5. **Standard Compliant** - Built with official MCP Python SDK (FastMCP)

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        SENA MCP SERVER                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐     ┌────────────────────────────────┐  │
│  │   MCP TOOLS      │     │   MCP RESOURCES                │  │
│  │   (Universal)    │     │   (Knowledge Bases)            │  │
│  ├──────────────────┤     ├────────────────────────────────┤  │
│  │ • Brilliant      │     │ • Reasoning Frameworks (579L)  │  │
│  │   Thinking       │     │ • Security Patterns (612L)     │  │
│  │ • Truth          │     │ • Performance Patterns (544L)  │  │
│  │   Verification   │     │ • Architecture Patterns (808L) │  │
│  │ • Table          │     │                                │  │
│  │   Formatting     │     │ Total: 2,543 lines of         │  │
│  │ • Code Analysis  │     │ persistent intelligence       │  │
│  │ • Health Status  │     │                                │  │
│  └──────────────────┘     └────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
         │                                        │
         │ Works in Claude Desktop                │ Works in Claude Code CLI
         ▼                                        ▼
┌──────────────────────┐            ┌─────────────────────────────┐
│  Claude Desktop      │            │  Claude Code CLI            │
│  (GUI Application)   │            │  (Terminal)                 │
├──────────────────────┤            ├─────────────────────────────┤
│ • MCP Tools ✅       │            │ • MCP Tools ✅              │
│ • MCP Resources ✅   │            │ • MCP Resources ✅          │
│ • Hooks ❌           │            │ • Hooks ✅ (CLI-specific)   │
└──────────────────────┘            └─────────────────────────────┘
```

---

## Component Architecture

### 1. MCP Server Core (`src/sena_mcp/server.py`)

**Purpose:** Main server implementation using FastMCP SDK

**Components:**
- **5 MCP Tools** - Intelligence operations (brilliant_thinking, verify_truth, format_table, analyze_code, get_health)
- **4 MCP Resources** - Knowledge base access (reasoning, security, performance, architecture)
- **Version Management** - Semantic versioning
- **Health Monitoring** - Component status tracking

**Technology Stack:**
- Python 3.11+
- FastMCP (MCP Python SDK)
- Pydantic for validation
- Unicode box-drawing for formatting

### 2. Knowledge Bases (`knowledge/`)

**Purpose:** Persistent intelligence accessible across all sessions

**Structure:**
```
knowledge/
├── README.md (Guide + statistics)
├── reasoning-frameworks.md (579 lines)
│   ├── First Principles Thinking
│   ├── Root Cause Analysis
│   ├── Decision Matrices
│   ├── Systems Thinking
│   └── 6 more frameworks
├── security-patterns.md (612 lines)
│   ├── Authentication (MFA, JWT)
│   ├── Authorization (RBAC, ABAC)
│   ├── Input Validation
│   └── OWASP Top 10 coverage
├── performance-patterns.md (544 lines)
│   ├── Algorithmic Complexity
│   ├── Database Optimization
│   ├── Caching Strategies
│   └── Profiling tools
└── architecture-patterns.md (808 lines)
    ├── DDD, CQRS, Event Sourcing
    ├── SOLID Principles
    ├── Design Patterns
    └── API Design
```

**Access Methods:**
- **Claude Desktop:** Via MCP resources (`sena://knowledge/reasoning-frameworks`)
- **Claude Code CLI:** Via MCP resources + referenced in CLAUDE.md rules

### 3. Enforcement Hooks (`hooks/`)

**Purpose:** CLI-specific behavior enforcement (only works in Claude Code)

**Structure:**
```
hooks/
├── user-prompt-submit.sh (12KB)
│   └── Pre-validation: Keyword detection, enforcement injection
├── sena-enforcer.sh (4.4KB)
│   └── Post-validation: Response format checking
├── post-tool-use.sh (1.1KB)
│   └── Output cleanup
├── permission-request.sh (1.7KB)
├── conversation-progress.sh (702B)
└── auto-progress.sh (589B)
```

**Functionality:**
- Automatic SENA 🦁 prefix when always-on mode active
- Keyword-triggered formatting (table, why/how, code analysis)
- Unicode table/thinking format enforcement
- Progress bar display for multi-step operations
- Git commit message sanitization (no AI credits)

**Installation:**
```bash
# Copy hooks to Claude Code hooks directory
cp hooks/* ~/.claude/hooks/

# Configure in settings
# ~/.claude/settings.json references these hooks
```

### 4. Documentation (`docs/`)

**Purpose:** User guides, compatibility matrices, examples

**Files:**
- `ARCHITECTURE.md` - This file (system architecture)
- `CLAUDE_CLI_RULES.md` - CLI enhancement rules reference
- `FEATURE_COMPATIBILITY.md` - MCP vs Hooks feature matrix
- `examples/` - Reference implementations

---

## Data Flow

### MCP Tool Invocation

```
1. User Request
   └─> Claude Desktop/CLI
       └─> MCP Client
           └─> SENA MCP Server
               └─> Tool Function (sena_brilliant_thinking, etc.)
                   └─> Process & Format
                       └─> Return Structured Result
                           └─> Claude presents to user
```

### MCP Resource Access

```
1. Claude needs knowledge
   └─> Requests resource (sena://knowledge/security-patterns)
       └─> SENA MCP Server
           └─> Read markdown file
               └─> Return full content
                   └─> Claude uses in context
```

### Hook Enforcement (CLI Only)

```
1. User types message
   └─> user-prompt-submit.sh intercepts
       └─> Checks for keywords (table, why, explain)
           └─> Injects enforcement reminder
               └─> Claude receives modified prompt
                   └─> Generates response
                       └─> sena-enforcer.sh validates
                           └─> Checks for SENA markers
                               └─> Allows/blocks response
```

---

## Configuration

### Claude Desktop (MCP Only)

**Config File:** `~/Library/Application Support/Claude/claude_desktop_config.json`

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
      ],
      "env": {
        "SENA_MODE": "full"
      }
    }
  }
}
```

### Claude Code CLI (MCP + Hooks)

**Config File:** `~/.claude/settings.json`

```json
{
  "mcpServers": {
    "sena": {
      "command": "uv",
      "args": ["--directory", "/path/to/sena-mcp-server", "run", "sena-mcp-server"]
    }
  },
  "hooks": {
    "userPromptSubmit": "~/.claude/hooks/user-prompt-submit.sh",
    "assistantResponseSubmit": "~/.claude/hooks/sena-enforcer.sh",
    "postToolUse": "~/.claude/hooks/post-tool-use.sh"
  }
}
```

---

## Feature Distribution

### MCP Tools (Universal - Works Everywhere)

✅ **sena_brilliant_thinking** - Advanced problem analysis
✅ **sena_verify_truth** - Anti-hallucination fact checking
✅ **sena_format_table** - Beautiful Unicode tables
✅ **sena_analyze_code** - Code quality analysis
✅ **sena_get_health** - System health metrics

### MCP Resources (Universal - Works Everywhere)

✅ **sena://knowledge/reasoning-frameworks** - 10 thinking frameworks
✅ **sena://knowledge/security-patterns** - 8 security categories
✅ **sena://knowledge/performance-patterns** - 10 optimization areas
✅ **sena://knowledge/architecture-patterns** - 8 pattern types

### Hooks (CLI-Specific - Terminal Only)

✅ **SENA 🦁 Prefix** - Automatic branding when enabled
✅ **Keyword Detection** - Auto-format on table/why/explain
✅ **Format Enforcement** - Block non-compliant responses
✅ **Progress Bars** - Multi-step operation tracking
✅ **Git Sanitization** - Remove AI credits from commits

---

## Security Model

### MCP Server

- **Read-Only Knowledge Bases** - Resources are read-only markdown files
- **No External Network** - Tools don't make external API calls
- **No File System Writes** - Server doesn't modify user files
- **Sandboxed Execution** - Runs in isolated Python process
- **Environment Variables** - Secrets via env vars, never hardcoded

### Hooks

- **Local Execution** - Bash scripts run on user's machine
- **No Sudo Required** - Standard user permissions
- **Transparent Operation** - All code visible and auditable
- **No Data Collection** - No analytics or telemetry
- **User Control** - Can be disabled anytime

---

## Performance Characteristics

### MCP Server Startup

- **Cold Start:** ~500ms (Python + FastMCP initialization)
- **Hot Start:** <50ms (cached process)
- **Memory:** ~30MB resident
- **CPU:** Minimal idle, spikes during tool use

### Tool Execution

- **brilliant_thinking:** 10-50ms (formatting only)
- **verify_truth:** 10-50ms (formatting only)
- **format_table:** 5-20ms (Unicode generation)
- **analyze_code:** 10-100ms (depends on code size)
- **get_health:** <5ms (simple dict return)

### Resource Access

- **Knowledge Base Load:** 5-20ms per file
- **Cached:** Yes, by MCP client
- **Size:** 2,543 lines total (~100KB uncompressed)

---

## Testing

### Manual Testing

```bash
# Test MCP server directly
cd /path/to/sena-mcp-server
uv run sena-mcp-server

# Test hooks
bash ~/.claude/hooks/user-prompt-submit.sh "give me table"

# Test in Claude Desktop
# Open Claude Desktop → MCP tools should appear

# Test in Claude Code
claude
# (tools + hooks active)
```

### Automated Testing

```bash
# Unit tests (coming in v1.2.0)
pytest tests/

# Integration tests
pytest tests/integration/
```

---

## Troubleshooting

### MCP Server Not Appearing

1. Check config file syntax (valid JSON)
2. Verify `uv` is installed (`which uv`)
3. Check server path is correct
4. Restart Claude Desktop/Code
5. Check logs: `~/Library/Logs/Claude/mcp-sena.log`

### Hooks Not Working

1. **Check always-on mode:** `ls ~/.claude/.sena_always_on`
2. **Verify hook permissions:** `ls -l ~/.claude/hooks/*.sh` (should be executable)
3. **Test hook directly:** `bash ~/.claude/hooks/user-prompt-submit.sh "test"`
4. **Check settings.json:** Hooks only work in Claude Code CLI
5. **Remember:** Hooks don't work in Claude Desktop (MCP only)

### Knowledge Bases Not Loading

1. **Verify files exist:** `ls /path/to/sena-mcp-server/knowledge/`
2. **Check resource paths:** Should be `sena://knowledge/reasoning-frameworks` (no `.md`)
3. **Restart server:** Changes require restart
4. **Check logs:** Look for file read errors

---

## Version History

### v1.1.0 (2025-11-24) - "Knowledge Integration"
- ✅ Added 4 knowledge bases as MCP resources (2,543 lines)
- ✅ Created docs/ directory with architecture documentation
- ✅ Added FEATURE_COMPATIBILITY.md matrix
- ✅ Enhanced README with comprehensive examples
- ✅ 85% feature coverage from SENA v3.3.1

### v1.0.0 (2025-11-23) - "Initial Release"
- ✅ 5 MCP tools (brilliant_thinking, verify_truth, format_table, analyze_code, get_health)
- ✅ 6 enforcement hooks for CLI
- ✅ FastMCP implementation
- ✅ GitHub repository published
- ✅ Installation script
- ✅ MIT License

---

## Future Roadmap

### v1.2.0 - "Testing & Quality"
- Automated test suite
- CI/CD with GitHub Actions
- Performance benchmarks
- Code coverage reports

### v1.3.0 - "Enhanced Intelligence"
- Multi-model orchestration tool
- Predictive pipeline analysis
- Advanced code quality metrics
- Real-time collaboration features

### v2.0.0 - "Universal Desktop"
- Desktop app for non-CLI users
- Visual knowledge base browser
- Interactive tool playground
- Cross-platform installer

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

MIT License - See [LICENSE](../LICENSE) for details.

---

**SENA 🦁 - Systematic Enhanced Natural Analysis**
