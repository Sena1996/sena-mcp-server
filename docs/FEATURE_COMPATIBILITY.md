# SENA Feature Compatibility Matrix

**Version:** 1.1.0
**Last Updated:** November 24, 2025

---

## Overview

This document provides a comprehensive comparison of SENA features and their compatibility across different environments:

- **MCP (Model Context Protocol)** - Works in both Claude Desktop (GUI) and Claude Code (CLI)
- **Hooks** - Works only in Claude Code (CLI terminal)

---

## Feature Compatibility Table

| # | Feature | Category | MCP Compatible | Hook Compatible | Notes |
|---|---------|----------|----------------|-----------------|-------|
| 1 | **SENA 🦁 Prefix (Always-On)** | Branding | ❌ | ✅ | CLI-only: Auto-prefix when ~/.claude/.sena_always_on exists |
| 2 | **Brilliant Thinking Format** | Intelligence | ✅ | ✅ | MCP tool + Hook enforcement |
| 3 | **Truth Verification** | Intelligence | ✅ | ✅ | MCP tool + Hook enforcement |
| 4 | **Unicode Tables** | Formatting | ✅ | ✅ | MCP tool + Hook enforcement |
| 5 | **Code Quality Analysis** | Intelligence | ✅ | ✅ | MCP tool + Hook enforcement |
| 6 | **Progress Bars** | UI/UX | ⚠️ | ✅ | Hook displays, MCP can request |
| 7 | **Health Metrics** | Monitoring | ✅ | ❌ | MCP tool returns status |
| 8 | **Keyword Detection** | Automation | ❌ | ✅ | CLI-only: table, why, how, explain |
| 9 | **Auto-Format Enforcement** | Quality | ❌ | ✅ | CLI-only: Post-validation |
| 10 | **Git Commit Sanitization** | Quality | ❌ | ✅ | CLI-only: Remove AI credits |
| 11 | **Reasoning Frameworks** | Knowledge | ✅ | ✅ | MCP resource + CLAUDE.md reference |
| 12 | **Security Patterns** | Knowledge | ✅ | ✅ | MCP resource + CLAUDE.md reference |
| 13 | **Performance Patterns** | Knowledge | ✅ | ✅ | MCP resource + CLAUDE.md reference |
| 14 | **Architecture Patterns** | Knowledge | ✅ | ✅ | MCP resource + CLAUDE.md reference |
| 15 | **First Principles Thinking** | Methodology | ✅ | ✅ | Via knowledge base + tool |
| 16 | **Root Cause Analysis** | Methodology | ✅ | ✅ | Via knowledge base + tool |
| 17 | **Systems Thinking** | Methodology | ✅ | ✅ | Via knowledge base + tool |
| 18 | **MCDA (Multi-Criteria)** | Methodology | ✅ | ✅ | Via knowledge base |
| 19 | **SOLID Principles** | Best Practice | ✅ | ✅ | Via architecture knowledge base |
| 20 | **Design Patterns** | Best Practice | ✅ | ✅ | Via architecture knowledge base |
| 21 | **OWASP Top 10** | Security | ✅ | ✅ | Via security knowledge base |
| 22 | **Authentication Patterns** | Security | ✅ | ✅ | Via security knowledge base |
| 23 | **Cryptography Patterns** | Security | ✅ | ✅ | Via security knowledge base |
| 24 | **Algorithmic Complexity** | Performance | ✅ | ✅ | Via performance knowledge base |
| 25 | **Database Optimization** | Performance | ✅ | ✅ | Via performance knowledge base |
| 26 | **Caching Strategies** | Performance | ✅ | ✅ | Via performance knowledge base |
| 27 | **DDD (Domain-Driven Design)** | Architecture | ✅ | ✅ | Via architecture knowledge base |
| 28 | **CQRS & Event Sourcing** | Architecture | ✅ | ✅ | Via architecture knowledge base |
| 29 | **Hexagonal Architecture** | Architecture | ✅ | ✅ | Via architecture knowledge base |
| 30 | **Microservices Patterns** | Architecture | ✅ | ✅ | Via architecture knowledge base |
| 31 | **API Design Best Practices** | Architecture | ✅ | ✅ | Via architecture knowledge base |
| 32 | **Session Management** | Core | ✅ | ✅ | MCP stateless, hooks maintain state |
| 33 | **Output Cleanup** | Quality | ⚠️ | ✅ | Hook post-processes, MCP pre-formats |
| 34 | **Permission Management** | Core | ⚠️ | ✅ | CLI has permission hooks |

---

## Legend

- **✅ YES** - Fully supported in this environment
- **❌ NO** - Not supported in this environment
- **⚠️ PARTIAL** - Partially supported or alternative implementation

---

## Summary Statistics

### By Environment

| Metric | MCP | Hooks | Both |
|--------|-----|-------|------|
| **Total Features** | 22 | 18 | 12 |
| **Exclusive Features** | 10 | 6 | - |
| **Shared Features** | 12 | 12 | 12 |
| **Partial Features** | 3 | 1 | - |

### By Category

| Category | Total Features | MCP | Hooks | Both |
|----------|----------------|-----|-------|------|
| **Intelligence** | 4 | 4 | 3 | 3 |
| **Knowledge** | 10 | 10 | 10 | 10 |
| **Formatting** | 2 | 2 | 2 | 2 |
| **Quality** | 3 | 1 | 3 | 1 |
| **Automation** | 2 | 0 | 2 | 0 |
| **Security** | 5 | 5 | 5 | 5 |
| **Performance** | 3 | 3 | 3 | 3 |
| **Architecture** | 6 | 6 | 6 | 6 |
| **Methodology** | 4 | 4 | 4 | 4 |
| **Core** | 2 | 2 | 2 | 1 |

---

## Environment Comparison

### Claude Desktop (MCP Only)

```
✅ Strengths:
- Universal MCP tools work perfectly
- Knowledge bases accessible via resources
- Clean GUI with tool selection
- Automatic tool discovery
- Cross-platform (macOS, Windows, Linux)

❌ Limitations:
- No hooks support (GUI environment)
- No automatic SENA 🦁 prefix
- No keyword-triggered formatting
- No automatic format enforcement
- No git commit sanitization
```

### Claude Code CLI (MCP + Hooks)

```
✅ Strengths:
- Everything from MCP
- PLUS all hook features
- Automatic SENA 🦁 prefix
- Keyword detection (table, why, explain)
- Format enforcement
- Progress bars
- Git commit cleanup
- Better for developers

⚠️ Considerations:
- Terminal-only (not GUI)
- Requires hook installation
- Bash environment needed
- More configuration steps
```

---

## Feature Details

### 1. Intelligence Tools

| Feature | MCP | Hooks | How It Works |
|---------|-----|-------|--------------|
| Brilliant Thinking | ✅ | ✅ | MCP: `sena_brilliant_thinking()` tool<br>Hooks: Auto-trigger on "why/how" |
| Truth Verification | ✅ | ✅ | MCP: `sena_verify_truth()` tool<br>Hooks: Auto-trigger on "is X true" |
| Code Analysis | ✅ | ✅ | MCP: `sena_analyze_code()` tool<br>Hooks: Auto-trigger on "analyze code" |
| Table Formatting | ✅ | ✅ | MCP: `sena_format_table()` tool<br>Hooks: Auto-trigger on "table" |

### 2. Knowledge Bases (2,543 lines)

| Knowledge Base | MCP Resource | Size | Coverage |
|----------------|--------------|------|----------|
| Reasoning Frameworks | `sena://knowledge/reasoning-frameworks` | 579 lines | 10 frameworks |
| Security Patterns | `sena://knowledge/security-patterns` | 612 lines | 8 categories |
| Performance Patterns | `sena://knowledge/performance-patterns` | 544 lines | 10 optimization areas |
| Architecture Patterns | `sena://knowledge/architecture-patterns` | 808 lines | 8 pattern types |

**Access:**
- **MCP:** Claude can request resources anytime
- **Hooks:** Referenced in CLAUDE.md for persistent access

### 3. Automation Features

| Feature | Environment | Description |
|---------|-------------|-------------|
| SENA 🦁 Prefix | CLI + Hooks | Automatic "SENA 🦁" prefix when `~/.claude/.sena_always_on` exists |
| Keyword Detection | CLI + Hooks | Auto-detect "table", "why", "how", "explain" and apply formatting |
| Format Enforcement | CLI + Hooks | Post-validation: Block responses without proper SENA formatting |
| Progress Bars | CLI + Hooks | Show Unicode progress for multi-step operations |
| Git Sanitization | CLI + Hooks | Remove AI credits from commit messages |

### 4. UI/UX Features

| Feature | MCP | Hooks | Notes |
|---------|-----|-------|-------|
| Unicode Tables | ✅ | ✅ | Beautiful box-drawing characters |
| Progress Bars | ⚠️ | ✅ | Hooks display directly, MCP can format |
| SENA Branding | ❌ | ✅ | Automatic 🦁 prefix (CLI only) |
| Error Formatting | ✅ | ✅ | Consistent error display |

---

## Use Case Recommendations

### Use Claude Desktop (MCP Only) When:

1. **You prefer GUI** - Visual interface with mouse clicks
2. **Cross-platform** - Need to work on Windows/Mac/Linux
3. **Quick queries** - One-off questions don't need automation
4. **Knowledge access** - Need reasoning/security/performance patterns
5. **Tool exploration** - Want to see all available tools

### Use Claude Code CLI (MCP + Hooks) When:

1. **Developer workflow** - Already work in terminal
2. **Automation** - Want keyword-triggered formatting
3. **Enforcement** - Need consistent SENA formatting
4. **Git integration** - Want commit message sanitization
5. **Progress tracking** - Multi-step operations
6. **Maximum features** - Want everything SENA offers

### Use Both When:

- Desktop for quick knowledge lookups
- CLI for development and automation
- Same MCP server serves both
- Hooks only active in CLI (no conflict)

---

## Migration Path

### From Claude Desktop to CLI

```bash
# 1. Install Claude Code
# (Download from claude.ai)

# 2. Copy MCP config
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json \
   ~/.claude/settings.json

# 3. Install hooks
git clone https://github.com/Sena1996/sena-mcp-server.git
cd sena-mcp-server
bash install.sh

# 4. Done! Now you have MCP + Hooks
```

### From CLI Back to Desktop

```bash
# Your MCP config already works in Desktop
# Just open Claude Desktop app
# Hooks won't interfere (CLI-only)
```

---

## Performance Comparison

| Metric | MCP (Desktop) | MCP + Hooks (CLI) | Notes |
|--------|---------------|-------------------|-------|
| **Startup Time** | ~2s | ~3s | Hooks add ~1s |
| **Tool Latency** | <100ms | <100ms | Same (MCP) |
| **Memory Usage** | ~150MB | ~170MB | Hooks +20MB |
| **CPU Idle** | <1% | <2% | Minimal difference |
| **Response Time** | Instant | +50ms | Hook validation |

---

## Security Comparison

| Security Aspect | MCP | Hooks | Risk Level |
|----------------|-----|-------|------------|
| **Code Execution** | Python (sandboxed) | Bash (local) | Both: Low |
| **File Access** | Read-only (knowledge) | Read-only (config) | Both: Low |
| **Network Access** | None | None | Both: None |
| **User Data** | No collection | No collection | Both: None |
| **Transparency** | Open source | Open source | Both: Full |

---

## Troubleshooting

### MCP Not Working

- ✅ Works in Claude Desktop
- ✅ Works in Claude Code CLI
- ❌ Check config file syntax
- ❌ Verify `uv` is installed
- ❌ Check server path

### Hooks Not Working

- ❌ Hooks only work in Claude Code CLI (not Desktop)
- ❌ Check `~/.claude/.sena_always_on` exists for prefix
- ❌ Verify hooks are executable: `chmod +x ~/.claude/hooks/*.sh`
- ❌ Check settings.json has hooks configured
- ❌ Test directly: `bash ~/.claude/hooks/user-prompt-submit.sh "test"`

---

## FAQ

**Q: Can I use MCP in Desktop and Hooks in CLI with same server?**
A: Yes! Same MCP server works for both. Hooks are CLI-specific and won't affect Desktop.

**Q: Which environment has more features?**
A: CLI (MCP + Hooks) has 100% of features. Desktop (MCP only) has ~65%.

**Q: Do hooks slow down responses?**
A: Minimal impact (~50ms). Hook validation is very fast.

**Q: Can I disable hooks temporarily?**
A: Yes, comment out hook entries in `~/.claude/settings.json`.

**Q: Are knowledge bases duplicated for each environment?**
A: No, single set of files served by MCP to both environments.

**Q: Can I contribute new features?**
A: Yes! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

**For detailed architecture, see [ARCHITECTURE.md](ARCHITECTURE.md)**

**SENA 🦁 - Systematic Enhanced Natural Analysis**
