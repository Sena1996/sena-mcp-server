# 🦁 SENA Controller - Complete Package

**Universal AI intelligence system for Claude Desktop + Claude Code CLI**

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue)](https://modelcontextprotocol.io/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Hooks-green)](https://github.com/Sena1996/sena-mcp-server)
[![Version](https://img.shields.io/badge/version-1.3.0-brightgreen)](https://github.com/Sena1996/sena-mcp-server)

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

**Total: 5 MCP tools**

### ✅ Knowledge Bases (MCP Resources - Works: Desktop + CLI)
Persistent intelligence accessible across all sessions:
- 📚 **Reasoning Frameworks** (579 lines) - 10 thinking methodologies
- 🔒 **Security Patterns** (612 lines) - OWASP Top 10, auth, crypto
- ⚡ **Performance Patterns** (544 lines) - Optimization strategies
- 🏗️ **Architecture Patterns** (808 lines) - SOLID, DDD, design patterns

**Total: 2,543 lines of persistent intelligence**

### ✅ Phase 3 Autonomous Skills (Works: Desktop + CLI)
Proactive code analysis and suggestions via MCP tools:
- 🤖 **Auto Code Review** (262 lines) - Quality metrics, best practices
- ⚡ **Auto Optimize** (387 lines) - Performance optimization suggestions
- 🛡️ **Auto Security Scan** (479 lines) - OWASP Top 10 vulnerability detection

**Total: 3 MCP tools + 3 MCP resources (1,128 lines of autonomous intelligence)**

### ✅ CLI Hooks (Works: Claude Code Only)
Terminal-specific behavior enhancements via 6 Bash hooks (20.7KB total):
- 🦁 **SENA Prefix** - Mandatory "SENA 🦁" branding on every response
- 🎨 **Output Filtering** - Clean, beautiful terminal display
- ⚡ **Auto-Triggers** - Automatic formatting for keywords (table, why, how)
- 🔧 **Git Integration** - Clean commit messages (no AI credits)
- 📊 **Progress Injection** - Auto-progress bars for multi-step tasks
- 🔐 **Permission Control** - Dynamic tool permissions without restart

**Detailed Documentation:** [hooks/README.md](hooks/README.md)

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

**Complete Hook System Documentation:** [hooks/README.md](hooks/README.md)

### Hook Scripts (6 files, 20.7KB total)

| Hook | Size | Purpose | Type |
|------|------|---------|------|
| **user-prompt-submit.sh** | 12.2KB | Enforces SENA prefix, detects keywords | Pre-Hook |
| **sena-enforcer.sh** | 4.5KB | Validates output format compliance | Post-Hook |
| **post-tool-use.sh** | 1.1KB | Suppresses verbose tool output | Post-Hook |
| **permission-request.sh** | 1.7KB | Dynamic tool permissions control | Permission |
| **conversation-progress.sh** | 0.7KB | Conversation-level progress bars | Progress |
| **auto-progress.sh** | 0.6KB | Auto-progress injection | Progress |

### Hook Triggers (Automatic Format Detection)

| User Input | Auto-Applied Format | Hook |
|------------|---------------------|------|
| "why", "how", "explain" | BRILLIANT THINKING format | user-prompt-submit.sh |
| "table", "tabular" | UNICODE TABLE format | user-prompt-submit.sh |
| "is X true", "fact check" | TRUTH VERIFICATION format | user-prompt-submit.sh |
| "analyze code" | CODE ANALYSIS format | user-prompt-submit.sh |
| Multiple operations | PROGRESS BARS | user-prompt-submit.sh + sena-enforcer.sh |

### SENA Always-On Mode

When `~/.claude/.sena_always_on` exists:
- ✅ **EVERY response** must start with "SENA 🦁"
- ✅ Applies to ALL requests (no exceptions)
- ✅ Enforced by hooks automatically (pre + post validation)
- ✅ Responses blocked if prefix missing

**Enable:**
```bash
touch ~/.claude/.sena_always_on
```

**Disable:**
```bash
rm ~/.claude/.sena_always_on
```

**How It Works:**
1. `user-prompt-submit.sh` injects reminder before Claude sees message
2. `sena-enforcer.sh` validates response has prefix, blocks if missing

See [hooks/README.md](hooks/README.md) for detailed configuration, troubleshooting, and testing.

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
│       └── server.py           # Main MCP server (5 tools + 4 resources)
├── knowledge/                  # NEW in v1.1.0
│   ├── README.md              # Knowledge base guide
│   ├── reasoning-frameworks.md # 579 lines - 10 methodologies
│   ├── security-patterns.md    # 612 lines - OWASP Top 10
│   ├── performance-patterns.md # 544 lines - Optimization
│   └── architecture-patterns.md# 808 lines - SOLID, DDD
├── skills/                      # NEW in v1.3.0 - Phase 3 Skills
│   ├── README.md              # Skills framework guide
│   ├── auto-code-review.md     # 262 lines - Code quality
│   ├── auto-optimize.md        # 387 lines - Performance
│   └── auto-security-scan.md   # 479 lines - Security
├── docs/                       # NEW in v1.1.0
│   ├── ARCHITECTURE.md        # System architecture
│   ├── FEATURE_COMPATIBILITY.md # MCP vs Hooks matrix
│   ├── CLAUDE_CLI_RULES.md    # CLI rules documentation
│   └── examples/              # Reference implementations
├── hooks/                       # NEW in v1.2.0 - Documented
│   ├── README.md              # Complete hook system guide
│   ├── user-prompt-submit.sh   # Pre-processing hook (12.2KB)
│   ├── sena-enforcer.sh        # Post-validation hook (4.5KB)
│   ├── post-tool-use.sh        # Tool cleanup hook (1.1KB)
│   ├── permission-request.sh   # Permission handler (1.7KB)
│   ├── conversation-progress.sh # Progress tracking (0.7KB)
│   └── auto-progress.sh        # Auto-progress bars (0.6KB)
├── tests/
│   └── test_server.py          # MCP server tests
├── install.sh                  # Automated installer
├── pyproject.toml              # Python package config
├── README.md                   # This file
├── LICENSE                     # MIT License
├── DEPLOYMENT_PLAN.md          # Deployment guide
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
- **26 features** work via MCP (universal - includes 4 knowledge base resources)
- **18 features** work via hooks (CLI-specific)
- **16 features** work in both systems

Full details: See [docs/FEATURE_COMPATIBILITY.md](docs/FEATURE_COMPATIBILITY.md)

---

## 📚 Knowledge Bases (MCP Resources)

SENA includes **2,543 lines of persistent intelligence** accessible via MCP resources:

### Available Knowledge Bases

| Knowledge Base | MCP Resource | Lines | Coverage |
|----------------|--------------|-------|----------|
| **Reasoning Frameworks** | `sena://knowledge/reasoning-frameworks` | 579 | 10 frameworks |
| **Security Patterns** | `sena://knowledge/security-patterns` | 612 | 8 categories |
| **Performance Patterns** | `sena://knowledge/performance-patterns` | 544 | 10 optimization areas |
| **Architecture Patterns** | `sena://knowledge/architecture-patterns` | 808 | 8 pattern types |

### How to Access

**Claude Desktop:**
```
Ask Claude: "Show me SENA security patterns for authentication"
Claude will access: sena://knowledge/security-patterns
```

**Claude Code CLI:**
```
Claude can access MCP resources automatically when needed
Also referenced in ~/.claude/CLAUDE.md for persistent access
```

**Detailed Information:**
- [knowledge/README.md](knowledge/README.md) - Complete knowledge base guide
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - System architecture
- [docs/FEATURE_COMPATIBILITY.md](docs/FEATURE_COMPATIBILITY.md) - Feature matrix

---

## 🤖 Phase 3 Autonomous Skills

SENA includes **3 autonomous skills** that proactively analyze code and provide suggestions:

### Available Skills (MCP Tools + Resources)

| Skill | Triggers | Purpose | Lines |
|-------|----------|---------|-------|
| **Auto Code Review** | >50 lines written, git commit | Automatic quality analysis | 262 |
| **Auto Optimize** | O(n²)+ complexity detected | Performance suggestions | 387 |
| **Auto Security Scan** | User input, SQL, file ops | Vulnerability detection | 479 |

**Total: 1,128 lines of autonomous intelligence**

### Skill Details

#### 1. Auto Code Review (`sena_auto_code_review`)

**Automatic Activation:**
- After writing >50 lines of code
- When creating/modifying programming files
- On git commit with code changes

**Analysis Includes:**
- Code quality metrics (readability, maintainability)
- Language-specific anti-patterns
- Performance review (complexity analysis)
- Security check (OWASP guidelines)
- Actionable improvement suggestions

**Example Usage:**
```
Use Auto Code Review on this Python function:

def process_data(items):
    result = []
    for item in items:
        if item['value'] > 0:
            result.append(item)
    return result
```

#### 2. Auto Optimize (`sena_auto_optimize`)

**Automatic Activation:**
- Nested loops detected (O(n²) or worse)
- Inefficient algorithms identified
- Performance-critical code

**Optimization Strategies:**
- Algorithm replacement (O(n²) → O(n))
- Data structure selection (list → set for O(1) lookup)
- Code-level optimizations
- Performance improvement estimates

**Example Usage:**
```
Optimize this code for performance:

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == arr[j] and i != j:
            print("Duplicate found")
```

#### 3. Auto Security Scan (`sena_auto_security_scan`)

**Automatic Activation:**
- User input handling
- Database queries (SQL, NoSQL)
- File operations
- Authentication/authorization code
- Cryptographic operations

**Security Checks:**
- OWASP Top 10 vulnerabilities
- SQL injection prevention
- XSS vulnerability detection
- Command injection risks
- Weak cryptography identification

**Example Usage:**
```
Security scan this database query:

query = f"SELECT * FROM users WHERE id = {user_id}"
db.execute(query)
```

### How Skills Work

1. **Detection:** MCP tools analyze code patterns
2. **Trigger:** When conditions match, skill activates
3. **Execution:** Comprehensive analysis performed
4. **Recommendations:** Actionable suggestions with code examples

### Accessing Skills

**Via MCP Tools:**
```
Use sena_auto_code_review to analyze my code
Run sena_auto_optimize on this function
Execute sena_auto_security_scan on this API endpoint
```

**Via MCP Resources:**
```
Access sena://skills/auto-code-review for documentation
View sena://skills/auto-optimize for optimization patterns
Read sena://skills/auto-security-scan for security guidelines
```

**Complete Documentation:**
- [skills/README.md](skills/README.md) - Skills framework overview
- [skills/auto-code-review.md](skills/auto-code-review.md) - Code review skill
- [skills/auto-optimize.md](skills/auto-optimize.md) - Optimization skill
- [skills/auto-security-scan.md](skills/auto-security-scan.md) - Security skill

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

### v1.3.0 (2025-11-24) - **Phase 3 Autonomous Skills**
- ✅ Added 3 MCP tools for autonomous code analysis
  - sena_auto_code_review() - Quality metrics and best practices
  - sena_auto_optimize() - Performance optimization suggestions
  - sena_auto_security_scan() - OWASP Top 10 vulnerability detection
- ✅ Added 3 MCP resources for skill documentation (1,128 lines total)
  - sena://skills/auto-code-review (262 lines)
  - sena://skills/auto-optimize (387 lines)
  - sena://skills/auto-security-scan (479 lines)
- ✅ Created skills/ directory with complete skill files
- ✅ Enhanced README with Phase 3 Skills section
- ✅ Updated health endpoint to include autonomous_skills feature
- ✅ Updated directory structure showing skills folder
- ✅ Coverage increased from 37% to 57% (+20%)

### v1.2.0 (2025-11-24) - **Hook System Documentation**
- ✅ Added comprehensive hooks/README.md (complete hook system guide)
- ✅ Documented all 6 hooks with examples and troubleshooting
- ✅ Installation instructions for hook system
- ✅ Configuration guide for SENA Always-On Mode
- ✅ Testing procedures and validation steps
- ✅ Hook architecture diagram and workflow
- ✅ Security considerations and best practices
- ✅ Enhanced main README with detailed hooks section
- ✅ CLI-only features fully documented and accessible
- ✅ Updated directory structure showing all hook files

### v1.1.0 (2025-11-24) - **Knowledge Integration**
- ✅ Added 4 knowledge bases as MCP resources (2,543 lines total)
  - reasoning-frameworks.md (579 lines)
  - security-patterns.md (612 lines)
  - performance-patterns.md (544 lines)
  - architecture-patterns.md (808 lines)
- ✅ Created comprehensive docs/ directory
  - ARCHITECTURE.md (system architecture)
  - FEATURE_COMPATIBILITY.md (34-feature matrix)
  - CLAUDE_CLI_RULES.md (CLI rules documentation)
- ✅ Updated MCP server with 4 resource endpoints
- ✅ Enhanced README with knowledge base guide
- ✅ 85% feature coverage from SENA v3.3.1

### v1.0.0 (2025-11-23) - **Initial Release**
- ✅ MCP server with 5 core tools
- ✅ CLI hooks system (6 hooks)
- ✅ Automated installer
- ✅ Complete documentation
- ✅ Both Desktop + CLI support
- ✅ GitHub repository published

---

╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║       🦁 SENA: Complete Intelligence for Claude             ║
║                                                              ║
║       Desktop + CLI • MCP + Hooks • One Package             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
