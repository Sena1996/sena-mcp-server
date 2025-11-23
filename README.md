# 🦁 SENA MCP Server

**Official Model Context Protocol server for SENA Controller intelligence features**

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue)](https://modelcontextprotocol.io/)
[![Version](https://img.shields.io/badge/version-1.0.0-green)](https://github.com/yourusername/sena-mcp-server)

## Overview

SENA MCP Server brings enterprise-grade AI intelligence features to Claude Desktop through the Model Context Protocol. Access brilliant thinking methodologies, truth verification, code analysis, and more directly in Claude Desktop.

## Features

### 🧠 Brilliant Thinking
- First principles analysis
- Root cause analysis (5 Whys, Fishbone)
- Multi-criteria decision making
- Systems thinking
- Lateral thinking techniques

### 🔍 Truth Verification
- Anti-hallucination fact checking
- Evidence-based analysis
- Confidence scoring
- Source validation

### 📊 Beautiful Formatting
- Unicode table generation
- Progress bars with SENA branding
- Structured output formatting
- Professional presentation

### 💻 Code Analysis
- Quality metrics (clarity, performance, security)
- SOLID principles validation
- Architecture pattern detection
- Security vulnerability scanning

### 📈 SENA Metrics
- Health monitoring
- Component status tracking
- Version verification
- Memory system integration

## Installation

### Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`
- Claude Desktop app

### Quick Start

```bash
# Using uv (recommended)
uvx sena-mcp-server

# Or install globally
uv pip install sena-mcp-server

# Or using pip
pip install sena-mcp-server
```

### Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sena": {
      "command": "uvx",
      "args": ["sena-mcp-server"],
      "env": {
        "SENA_MODE": "full"
      }
    }
  }
}
```

## Available Tools

### `sena_brilliant_thinking`
Analyze complex problems using advanced thinking methodologies.

**Parameters:**
- `problem` (string): Problem to analyze
- `methodology` (string, optional): Specific methodology (auto, first_principles, root_cause, systems, etc.)

**Example:**
```
Use brilliant thinking to analyze why our API response time increased
```

### `sena_verify_truth`
Verify the truth of statements with anti-hallucination features.

**Parameters:**
- `statement` (string): Statement to verify
- `require_evidence` (boolean, optional): Require evidence sources

**Example:**
```
Verify: "React 18 introduced automatic batching for better performance"
```

### `sena_format_table`
Create beautiful Unicode tables.

**Parameters:**
- `headers` (array): Table column headers
- `rows` (array): Table data rows
- `title` (string, optional): Table title

**Example:**
```
Create a table comparing Next.js, React, and Vue performance metrics
```

### `sena_analyze_code`
Comprehensive code quality analysis.

**Parameters:**
- `code` (string): Code to analyze
- `language` (string): Programming language
- `focus` (string, optional): Analysis focus (security, performance, architecture, all)

**Example:**
```
Analyze this TypeScript code for security vulnerabilities
```

### `sena_get_health`
Get SENA system health and metrics.

**Parameters:** None

**Example:**
```
Show SENA health status
```

### `sena_progress_bar`
Generate beautiful progress indicators.

**Parameters:**
- `tasks` (array): List of tasks with status
- `style` (string, optional): Progress bar style

**Example:**
```
Show progress for: database migration, API testing, deployment
```

## Architecture

```
sena-mcp-server/
├── src/
│   ├── server.py          # Main MCP server
│   ├── tools/
│   │   ├── thinking.py    # Brilliant thinking tools
│   │   ├── verification.py # Truth verification
│   │   ├── formatting.py  # Table & progress bars
│   │   ├── code_analysis.py # Code quality analysis
│   │   └── metrics.py     # Health & metrics
│   ├── knowledge/
│   │   ├── reasoning_frameworks.py
│   │   ├── security_patterns.py
│   │   ├── performance_patterns.py
│   │   └── architecture_patterns.py
│   └── utils/
│       ├── unicode_tables.py
│       └── formatters.py
├── tests/
├── pyproject.toml
├── README.md
└── LICENSE
```

## Knowledge Base Integration

SENA includes persistent knowledge bases:

- **Reasoning Frameworks**: First principles, root cause analysis, decision matrices
- **Security Patterns**: OWASP Top 10, secure coding, cryptography
- **Performance Patterns**: Algorithmic optimization, caching, database tuning
- **Architecture Patterns**: SOLID, design patterns, DDD, microservices

## Development

```bash
# Clone repository
git clone https://github.com/yourusername/sena-mcp-server
cd sena-mcp-server

# Install dependencies
uv sync

# Run tests
uv run pytest

# Run server locally
uv run sena-mcp-server
```

## Testing with MCP Inspector

```bash
# Install MCP Inspector
npm install -g @modelcontextprotocol/inspector

# Test SENA server
mcp inspector uvx sena-mcp-server
```

## Version History

### v1.0.0 (2025-11-23)
- Initial release
- Brilliant thinking methodologies
- Truth verification system
- Beautiful formatting (tables, progress bars)
- Code quality analysis
- Health metrics monitoring
- Knowledge base integration

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

MIT License - see [LICENSE](LICENSE) file

## Credits

- **Creator**: SENA Team
- **MCP Protocol**: Anthropic PBC
- **Inspired by**: Claude Code Controller v3.0

## Support

- **Issues**: https://github.com/yourusername/sena-mcp-server/issues
- **Documentation**: https://github.com/yourusername/sena-mcp-server/wiki
- **MCP Docs**: https://modelcontextprotocol.io/

---

**🦁 Bringing SENA intelligence to Claude Desktop through MCP!**
