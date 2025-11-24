# SENA v3.3.1 Phase 2 Setup Guide

**Phase 2: Access Expansion - MCP Server Configuration**

This guide walks through setting up all Phase 2 MCP servers for SENA v3.3.1.

---

## Overview

Phase 2 adds 4 new MCP servers to SENA:

1. **SENA Metrics** - Custom health monitoring and metrics (✅ INSTALLED)
2. **PostgreSQL** - Database access for data persistence
3. **GitHub** - Repository access, PR automation, issue tracking
4. **Brave Search** - Real-time web search capabilities

---

## Prerequisites

### Required Software

```bash
# Node.js (for MCP servers)
node --version  # Should be 18+ or 20+

# Python 3 (for SENA Metrics)
python3 --version  # Should be 3.8+

# PostgreSQL (optional, if using database)
psql --version  # Should be 12+

# pip packages for SENA Metrics
pip3 install mcp
```

### Required Accounts/Keys

- **GitHub Personal Access Token** (for GitHub MCP server)
- **Brave Search API Key** (for Brave Search MCP server)
- **PostgreSQL Database** (optional, for database access)

---

## Setup Instructions

### 1. SENA Metrics MCP Server (✅ Complete)

**Status:** Installed and configured

**Location:** `/Users/sena/.claude/sena_controller_v3.0/sena_metrics_mcp.py`

**Tools Provided:**
- `get_sena_health()` - Complete health monitoring
- `get_innovation_metrics()` - Feature and quality metrics
- `get_test_results()` - Test coverage and results
- `check_sena_config()` - Configuration status
- `get_phase_status()` - Implementation phase tracking

**No additional setup required.**

---

### 2. PostgreSQL MCP Server

**Purpose:** Provides database access for SENA data persistence and querying.

#### Setup Steps:

**Step 1: Install PostgreSQL** (if not already installed)

```bash
# macOS
brew install postgresql@15
brew services start postgresql@15

# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql
```

**Step 2: Create SENA Database**

```bash
# Create database
createdb sena_db

# Or using psql
psql -U postgres
CREATE DATABASE sena_db;
\q
```

**Step 3: Configure Environment Variables**

```bash
# Copy template
cp ~/.claude/.env.example ~/.claude/.env

# Edit .env and set:
DATABASE_URL=postgresql://localhost/sena_db
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=sena_db
```

**Step 4: Test Connection**

```bash
# Test with psql
psql -d sena_db -c "SELECT version();"
```

**Step 5: Restart Claude Code**

The PostgreSQL MCP server will auto-install via `npx` on first use.

#### Available Tools:

Once configured, you'll have access to:
- `query` - Execute SQL queries
- `list_tables` - List all tables
- `describe_table` - Show table schema
- `create_table` - Create new tables

---

### 3. GitHub MCP Server

**Purpose:** Provides GitHub integration for repository access, PR automation, and issue tracking.

#### Setup Steps:

**Step 1: Create GitHub Personal Access Token**

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Set description: "SENA v3.3.1 MCP Server"
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read organization data)
   - ✅ `read:user` (Read user profile data)
   - ✅ `workflow` (Update GitHub Actions workflows) [optional]
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)

**Step 2: Configure Environment Variables**

```bash
# Edit ~/.claude/.env
echo "GITHUB_TOKEN=ghp_your_actual_token_here" >> ~/.claude/.env
```

**Step 3: Restart Claude Code**

The GitHub MCP server will auto-install via `npx` on first use.

#### Available Tools:

Once configured, you'll have access to:
- `create_or_update_file` - Create or update files in repos
- `search_repositories` - Search GitHub repositories
- `create_repository` - Create new repositories
- `get_file_contents` - Read file contents
- `push_files` - Push multiple files
- `create_issue` - Create GitHub issues
- `create_pull_request` - Create PRs
- `fork_repository` - Fork repositories
- `create_branch` - Create branches

---

### 4. Brave Search MCP Server

**Purpose:** Provides real-time web search capabilities for up-to-date information.

#### Setup Steps:

**Step 1: Get Brave Search API Key**

1. Go to https://brave.com/search/api/
2. Click "Get Started" or "Sign Up"
3. Create an account / log in
4. Navigate to API Dashboard
5. Create a new API key
6. Copy the API key

**Step 2: Configure Environment Variables**

```bash
# Edit ~/.claude/.env
echo "BRAVE_API_KEY=your_actual_api_key_here" >> ~/.claude/.env
```

**Step 3: Restart Claude Code**

The Brave Search MCP server will auto-install via `npx` on first use.

#### Available Tools:

Once configured, you'll have access to:
- `brave_web_search` - Search the web with Brave
- `brave_local_search` - Search for local businesses/places

---

## Verification

### Check MCP Server Configuration

```bash
# View current configuration
cat ~/.claude/.mcp.json

# Should show 5 servers:
# - sena-controller
# - sena-metrics
# - postgres
# - github
# - brave-search
```

### Test SENA Metrics

After restarting Claude Code, try:

```
Get SENA health status
```

Claude will use the `get_sena_health()` tool from sena-metrics MCP server.

### Test GitHub (after token setup)

```
Search for repositories related to "fastmcp"
```

### Test Brave Search (after API key setup)

```
Search the web for "SENA controller architecture patterns"
```

---

## Environment Variables Summary

Required environment variables in `~/.claude/.env`:

```bash
# GitHub Integration
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Brave Search
BRAVE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# PostgreSQL (optional)
DATABASE_URL=postgresql://localhost/sena_db
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
```

**Security Note:**
- Never commit `.env` file to version control
- Keep API keys secure
- Rotate tokens periodically
- Use environment-specific tokens (dev vs prod)

---

## Troubleshooting

### MCP Server Not Starting

```bash
# Check Node.js version
node --version  # Should be 18+

# Test manual installation
npx -y @modelcontextprotocol/server-github
```

### GitHub Token Issues

```bash
# Test token validity
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```

### PostgreSQL Connection Issues

```bash
# Test connection
psql -d sena_db -c "SELECT 1;"

# Check PostgreSQL status
brew services list | grep postgresql  # macOS
systemctl status postgresql           # Linux
```

### Environment Variables Not Loading

```bash
# Check .env file exists
ls -la ~/.claude/.env

# Restart Claude Code completely
# Environment variables are loaded on startup
```

---

## Next Steps

Once Phase 2 is complete:

- ✅ All 5 MCP servers configured
- ✅ Environment variables set
- ✅ Connections tested

**Proceed to Phase 3: Autonomous Capabilities**

- Autonomous skills (auto-activation)
- Advanced reasoning hooks
- Proactive assistance patterns

---

## MCP Server Status Summary

| Server | Status | Description |
|--------|--------|-------------|
| sena-controller | ✅ Active | Core SENA formats and presentation |
| sena-metrics | ✅ Active | Health monitoring and metrics |
| postgres | ⚙️ Setup Required | Database access (optional) |
| github | ⚙️ Setup Required | GitHub integration (token needed) |
| brave-search | ⚙️ Setup Required | Web search (API key needed) |

---

**Phase 2 Configuration:** Complete (infrastructure ready)
**Phase 2 Activation:** Requires API keys and database setup
**Next Phase:** Phase 3 - Autonomous Capabilities

---

*Updated: November 23, 2025*
*Version: 3.3.1*
*Status: Phase 2 Infrastructure Complete*
