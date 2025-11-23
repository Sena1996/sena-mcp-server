# 🦁 SENA Controller - Complete Package

**Universal AI intelligence system for Claude Desktop + Claude Code CLI**

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue)](https://modelcontextprotocol.io/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Hooks-green)](https://github.com/Sena1996/sena-mcp-server)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)](https://github.com/Sena1996/sena-mcp-server)

---

## 🎯 What is SENA?

SENA is a **complete intelligence enhancement system** for Claude that works everywhere:

- **🖥️ Claude Desktop** (via MCP protocol)
- **💻 Claude Code CLI** (via hooks + MCP)

**One package. Two deployment modes. Complete intelligence.**

---

## 📦 What's Inside

### ✅ MCP Server (Works: Desktop + CLI)
Enterprise-grade AI tools through official MCP protocol:
- 🧠 **Brilliant Thinking** - First principles, root cause, systems thinking
- 🔍 **Truth Verification** - Anti-hallucination fact checking
- 📊 **Beautiful Tables** - Unicode formatting with SENA branding
- 💻 **Code Analysis** - Security, performance, architecture analysis
- 📈 **Health Metrics** - System monitoring and status

### ✅ CLI Hooks (Works: Claude Code Only)
Terminal-specific behavior enhancements:
- 🦁 **SENA Prefix** - Mandatory "SENA 🦁" branding on every response
- 🎨 **Output Filtering** - Clean, beautiful terminal display
- ⚡ **Auto-Triggers** - Automatic formatting for keywords (table, why, how)
- 🔧 **Git Integration** - Clean commit messages (no AI credits)
- 📊 **Progress Injection** - Auto-progress bars for multi-step tasks

---

## 🚀 Quick Installation

### Option 1: Automated Install (Recommended)

```bash
# Clone repository
git clone https://github.com/Sena1996/sena-mcp-server.git
cd sena-mcp-server

# Run installer
./install.sh
```

The installer will ask:
1. **Full** - MCP Server + CLI Hooks (complete experience)
2. **MCP Only** - Just intelligence tools (Claude Desktop)
3. **Hooks Only** - Just CLI behavior (Claude Code terminal)

### Option 2: Manual Installation

#### Prerequisites

```bash
# Install uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

#### For Claude Desktop (MCP Server)

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sena": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/YOUR_USERNAME/path/to/sena-mcp-server",
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

**Then restart Claude Desktop.**

#### For Claude Code CLI (Hooks)

```bash
# Copy hooks
mkdir -p ~/.claude/hooks
cp hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Enable SENA always-on mode
touch ~/.claude/.sena_always_on

# Configure hooks in ~/.claude/settings.json
{
  "userPromptSubmitHook": "~/.claude/hooks/user-prompt-submit.sh",
  "assistantResponseSubmitHook": "~/.claude/hooks/sena-enforcer.sh",
  "postToolUseHook": "~/.claude/hooks/post-tool-use.sh"
}
```

---

## 💡 Usage Examples

### In Claude Desktop (MCP Tools)

```
User: Use brilliant thinking to analyze why our API is slow
Claude: [Performs first principles analysis using SENA methodology]

User: Verify: "React 18 has automatic batching"
Claude: [Runs truth verification with evidence]

User: Create a table comparing database performance
Claude: [Generates beautiful Unicode table]

User: Analyze this code for security issues
Claude: [Comprehensive security analysis]

User: Show SENA health status
Claude: [Displays system metrics]
```

### In Claude Code CLI (Hooks + MCP)

```bash
$ claude

User: give me moon info in table
Assistant: SENA 🦁

╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                  🌙 MOON COMPREHENSIVE DATA                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════
  BASIC PROPERTIES
════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────┐
│ Property              │ Value                                │
├──────────────────────────────────────────────────────────────┤
│ Name                  │ Luna (Earth's Moon)                  │
│ Diameter              │ 3,474 km                             │
│ Distance from Earth   │ 384,400 km (average)                 │
│ Orbital Period        │ 27.3 days                            │
│ Rotation Period       │ 27.3 days (tidally locked)           │
│ Surface Temperature   │ -173°C to 127°C                      │
│ Gravity               │ 1.62 m/s² (16.5% of Earth)           │
│ Surface Area          │ 37.9 million km²                     │
│ Mass                  │ 7.342 × 10²² kg                      │
│ Age                   │ ~4.5 billion years                   │
│ Atmosphere            │ Virtually none (exosphere)           │
│ Surface Composition   │ Silicate rock, regolith              │
└──────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════
  MOON PHASES (8 Primary Phases)
════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────┐
│ Phase              │ Icon │ Illumination │ Description      │
├──────────────────────────────────────────────────────────────┤
│ New Moon           │ 🌑   │ 0%           │ Not visible      │
│ Waxing Crescent    │ 🌒   │ 1-49%        │ Growing right    │
│ First Quarter      │ 🌓   │ 50%          │ Half visible     │
│ Waxing Gibbous     │ 🌔   │ 51-99%       │ Nearly full      │
│ Full Moon          │ 🌕   │ 100%         │ Fully lit        │
│ Waning Gibbous     │ 🌖   │ 99-51%       │ Shrinking left   │
│ Last Quarter       │ 🌗   │ 50%          │ Half visible     │
│ Waning Crescent    │ 🌘   │ 49-1%        │ Shrinking right  │
└──────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════
  NOTABLE FEATURES & LANDMARKS
════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────┐
│ Feature Type       │ Examples                                │
├──────────────────────────────────────────────────────────────┤
│ 🌊 Maria (Seas)    │ Mare Tranquillitatis, Mare Serenitatis │
│ ⛰️  Highlands       │ Montes Apenninus, Montes Caucasus      │
│ 💥 Impact Craters  │ Tycho, Copernicus, Aristarchus         │
│ 🏔️  Mountain Ranges│ Leibnitz Mountains (10,000m)           │
│ 🕳️  Rilles          │ Hadley Rille, Alpine Valley            │
│ ⚪ Bright Rays      │ From Tycho, Copernicus craters         │
└──────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════
  SPACE MISSIONS & EXPLORATION
════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────┐
│ Mission/Program    │ Status      │ Achievement              │
├──────────────────────────────────────────────────────────────┤
│ 🚀 Apollo 11       │ 1969 ✅     │ First human landing      │
│ 🛰️  Apollo 17      │ 1972 ✅     │ Last manned mission      │
│ 🇨🇳 Chang'e 4       │ 2019 ✅     │ First far side landing   │
│ 🇮🇳 Chandrayaan-3   │ 2023 ✅     │ South pole landing       │
│ 🇺🇸 Artemis Program │ Ongoing 🔄  │ Return humans to Moon    │
│ 🌍 ISRO/ESA        │ Planned 📅  │ Future collaborations    │
└──────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════
  INTERESTING FACTS
════════════════════════════════════════════════════════════════

✨ The Moon is moving away from Earth at ~3.8 cm per year
🌍 Same side always faces Earth (tidally locked)
💎 Contains water ice in permanently shadowed craters
🌡️  Temperature swings 300°C between day and night
👣 12 humans have walked on the lunar surface
🔭 Visible features from Earth: Maria, craters, rays
🌊 Causes Earth's tides through gravitational pull
⏰ Day on Moon: 29.5 Earth days (one lunar day)
```

**Notice:** Every response starts with "SENA 🦁" and includes beautiful tables with emojis, phases, and comprehensive data!

---

## 🧠 MCP Tools Reference

### `sena_brilliant_thinking`
Analyze complex problems using advanced methodologies.

**Parameters:**
- `problem` (string): Problem description
- `methodology` (string): `auto`, `first_principles`, `root_cause`, `systems`, `decision_matrix`

**Example:**
```
Use brilliant thinking to determine the root cause of database deadlocks
```

---

### `sena_verify_truth`
Verify statements with anti-hallucination features.

**Parameters:**
- `statement` (string): Claim to verify
- `require_evidence` (boolean): Demand evidence sources

**Example:**
```
Verify: "TypeScript has better performance than JavaScript"
```

---

### `sena_format_table`
Create beautiful Unicode tables.

**Parameters:**
- `headers` (array): Column headers
- `rows` (array): Data rows
- `title` (string): Optional table title

**Example:**
```
Create table: Framework, Speed, Bundle Size for React, Vue, Svelte
```

---

### `sena_analyze_code`
Comprehensive code quality analysis.

**Parameters:**
- `code` (string): Code to analyze
- `language` (string): Programming language
- `focus` (string): `security`, `performance`, `architecture`, `all`

**Example:**
```typescript
Analyze this code for security:

function login(username, password) {
  return db.query(`SELECT * FROM users WHERE user='${username}'`);
}
```

---

### `sena_get_health`
Get SENA system health status.

**Parameters:** None

**Example:**
```
Show SENA health status
```

**Returns:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "mode": "mcp",
  "components": {
    "brilliant_thinking": "operational",
    "truth_verification": "operational",
    "code_analysis": "operational",
    "formatting": "operational",
    "metrics": "operational"
  }
}
```

---

## 🔧 CLI Hooks Reference

### Hook Scripts

| Hook | Purpose | Location |
|------|---------|----------|
| `user-prompt-submit.sh` | Enforces SENA prefix, detects keywords | Pre-processing |
| `sena-enforcer.sh` | Validates output format | Post-processing |
| `post-tool-use.sh` | Cleans tool execution display | After tool use |
| `permission-request.sh` | Custom permission handling | Permission requests |
| `conversation-progress.sh` | Progress tracking | During execution |
| `auto-progress.sh` | Auto-progress injection | Multi-step tasks |

### Hook Triggers

| User Input | Auto-Applied Format |
|------------|---------------------|
| "why", "how", "explain" | BRILLIANT THINKING format |
| "table", "tabular" | UNICODE TABLE format |
| "is X true", "fact check" | TRUTH VERIFICATION format |
| "analyze code" | CODE ANALYSIS format |
| Multiple operations | PROGRESS BARS |

### SENA Always-On Mode

When `~/.claude/.sena_always_on` exists:
- ✅ **EVERY response** must start with "SENA 🦁"
- ✅ Applies to ALL requests (no exceptions)
- ✅ Enforced by hooks automatically

To disable:
```bash
rm ~/.claude/.sena_always_on
```

---

## 📊 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  SENA CONTROLLER COMPLETE PACKAGE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📦 MCP SERVER                    🔧 CLI HOOKS             │
│  (Universal)                      (Claude Code Only)       │
│                                                             │
│  ├─ Brilliant Thinking            ├─ SENA 🦁 Prefix       │
│  ├─ Truth Verification            ├─ Output Filtering      │
│  ├─ Table Formatting              ├─ Auto-Triggers         │
│  ├─ Code Analysis                 ├─ Git Integration       │
│  └─ Health Metrics                └─ Progress Injection    │
│                                                             │
│  Works:                           Works:                    │
│  ✅ Claude Desktop                ✅ Claude Code CLI       │
│  ✅ Claude Code CLI               ❌ Claude Desktop        │
│                                                             │
│  Protocol: MCP (official)         Protocol: Bash hooks     │
│  Distribution: This repo          Distribution: This repo  │
└─────────────────────────────────────────────────────────────┘
```

### Directory Structure

```
sena-mcp-server/
├── src/
│   └── sena_mcp/
│       ├── __init__.py
│       └── server.py           # Main MCP server
├── hooks/
│   ├── user-prompt-submit.sh   # Pre-processing hook
│   ├── sena-enforcer.sh        # Post-validation hook
│   ├── post-tool-use.sh        # Tool cleanup hook
│   ├── permission-request.sh   # Permission handler
│   ├── conversation-progress.sh # Progress tracking
│   └── auto-progress.sh        # Auto-progress bars
├── tests/
│   └── test_server.py          # MCP server tests
├── install.sh                  # Automated installer
├── pyproject.toml              # Python package config
├── README.md                   # This file
├── LICENSE                     # MIT License
├── DEPLOYMENT_PLAN.md          # Architecture docs
└── .gitignore
```

---

## 🧪 Testing

### Test MCP Server

```bash
# Run tests
uv run pytest

# Test with MCP Inspector
npx @modelcontextprotocol/inspector uv --directory . run sena-mcp-server
```

### Test CLI Hooks

```bash
# Verify hooks installed
ls -la ~/.claude/hooks/

# Test in Claude Code CLI
claude
# Type: "give me moon info in table"
# Should see: SENA 🦁 prefix + beautiful comprehensive table
```

---

## 🔍 Troubleshooting

### MCP Server Issues

**Problem:** Claude Desktop doesn't see SENA tools

**Solution:**
1. Check config path: `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Verify JSON syntax (no trailing commas)
3. Restart Claude Desktop completely
4. Check logs: `~/Library/Logs/Claude/mcp*.log`

**Problem:** MCP server fails to start

**Solution:**
```bash
# Test manually
uv run sena-mcp-server

# Check dependencies
uv sync

# Verify Python version
python3 --version  # Must be 3.10+
```

### Hook Issues

**Problem:** No "SENA 🦁" prefix in terminal

**Solution:**
1. Check always-on flag: `ls ~/.claude/.sena_always_on`
2. Verify hooks exist: `ls ~/.claude/hooks/`
3. Check permissions: `chmod +x ~/.claude/hooks/*.sh`
4. Verify settings: `cat ~/.claude/settings.json`

**Problem:** Hooks not triggering

**Solution:**
```bash
# Re-run installer
./install.sh

# Or manually
cp hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

---

## 🎯 Feature Compatibility Matrix

| Feature | MCP | Hook | Where It Works |
|---------|-----|------|----------------|
| **SENA 🦁 Prefix** | ❌ | ✅ | CLI only |
| **Brilliant Thinking** | ✅ | ✅ | Desktop + CLI |
| **Truth Verification** | ✅ | ✅ | Desktop + CLI |
| **Table Formatting** | ✅ | ✅ | Desktop + CLI |
| **Code Analysis** | ✅ | ✅ | Desktop + CLI |
| **Health Metrics** | ✅ | ❌ | Desktop + CLI (via MCP) |
| **Output Filtering** | ❌ | ✅ | CLI only |
| **Auto-Triggers** | ❌ | ✅ | CLI only |
| **Git Clean Commits** | ❌ | ✅ | CLI only |
| **Progress Bars** | ✅ | ✅ | Desktop + CLI |

**Summary:**
- **22 features** work via MCP (universal)
- **18 features** work via hooks (CLI-specific)
- **12 features** work in both systems

Full details: See [SENA_FEATURE_COMPATIBILITY_TABLE.md](/.claude/SENA_FEATURE_COMPATIBILITY_TABLE.md)

---

## 📚 Knowledge Base

SENA includes persistent knowledge bases accessible via MCP:

- **Reasoning Frameworks** - First principles, root cause, decision matrices, systems thinking
- **Security Patterns** - OWASP Top 10, secure coding, cryptography best practices
- **Performance Patterns** - Algorithmic optimization, caching, database tuning
- **Architecture Patterns** - SOLID, design patterns, DDD, microservices, CQRS

---

## 🚀 Publishing to PyPI (Optional)

To make SENA installable via `uvx sena-mcp-server` globally:

```bash
# Build package
uv build

# Publish to PyPI (requires account)
uv publish

# Or test with TestPyPI first
uv publish --repository testpypi
```

After publishing, users can install with:
```bash
uvx sena-mcp-server
```

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- **Creator**: SENA 🦁
- **MCP Protocol**: [Anthropic PBC](https://www.anthropic.com/)
- **Inspired by**: Claude Code Controller v3.0
- **FastMCP**: Official Python MCP SDK

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Sena1996/sena-mcp-server/issues)
- **MCP Docs**: [Model Context Protocol](https://modelcontextprotocol.io/)
- **Claude Code Docs**: [Claude Code CLI](https://docs.anthropic.com/claude-code)

---

## 🎉 Version History

### v1.0.0 (2025-11-24)
- ✅ Initial release
- ✅ MCP server with 5 core tools
- ✅ CLI hooks system (6 hooks)
- ✅ Automated installer
- ✅ Complete documentation
- ✅ Knowledge base integration
- ✅ Both Desktop + CLI support

---

╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║       🦁 SENA: Complete Intelligence for Claude             ║
║                                                              ║
║       Desktop + CLI • MCP + Hooks • One Package             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
