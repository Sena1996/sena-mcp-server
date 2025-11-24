#!/bin/bash

# SENA Controller - Complete Installation Script
# Installs both MCP server and CLI hooks

set -e

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║              SENA 🦁 CONTROLLER INSTALLER                    ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Detect OS
OS="$(uname -s)"
case "$OS" in
    Darwin*)    PLATFORM="macos";;
    Linux*)     PLATFORM="linux";;
    *)          echo "❌ Unsupported OS: $OS"; exit 1;;
esac

echo "📊 Platform: $PLATFORM"
echo ""

# Check for required tools
echo "🔍 Checking dependencies..."

# Check for uv (Python package manager)
if ! command -v uv &> /dev/null; then
    echo "⚠️  uv not found. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

echo "✅ uv installed"
echo ""

# Installation mode selection
echo "📦 Select installation mode:"
echo "  1) Full (MCP Server + CLI Hooks)"
echo "  2) MCP Server Only (Claude Desktop)"
echo "  3) CLI Hooks Only (Claude Code Terminal)"
echo ""
read -p "Enter choice [1-3]: " INSTALL_MODE

case "$INSTALL_MODE" in
    1) INSTALL_MCP=true; INSTALL_HOOKS=true; echo "✅ Installing: Full package";;
    2) INSTALL_MCP=true; INSTALL_HOOKS=false; echo "✅ Installing: MCP Server only";;
    3) INSTALL_MCP=false; INSTALL_HOOKS=true; echo "✅ Installing: CLI Hooks only";;
    *) echo "❌ Invalid choice"; exit 1;;
esac
echo ""

# ============================================================================
# MCP SERVER INSTALLATION
# ============================================================================

if [ "$INSTALL_MCP" = true ]; then
    echo "════════════════════════════════════════════════════════════════"
    echo "  MCP SERVER INSTALLATION"
    echo "════════════════════════════════════════════════════════════════"
    echo ""

    # Determine Claude Desktop config path
    if [ "$PLATFORM" = "macos" ]; then
        CLAUDE_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
    else
        CLAUDE_CONFIG="$HOME/.config/Claude/claude_desktop_config.json"
    fi

    echo "📝 Claude Desktop config: $CLAUDE_CONFIG"

    # Create config directory if it doesn't exist
    mkdir -p "$(dirname "$CLAUDE_CONFIG")"

    # Check if config exists
    if [ ! -f "$CLAUDE_CONFIG" ]; then
        echo "📄 Creating new Claude Desktop config..."
        echo '{"mcpServers":{}}' > "$CLAUDE_CONFIG"
    fi

    # Add SENA MCP server to config
    echo "🔧 Adding SENA MCP server to Claude Desktop config..."

    REPO_PATH="$(cd "$(dirname "$0")" && pwd)"

    # Use Python to safely update JSON
    python3 - <<EOF
import json
import sys

config_path = "$CLAUDE_CONFIG"
repo_path = "$REPO_PATH"

try:
    with open(config_path, 'r') as f:
        config = json.load(f)
except:
    config = {"mcpServers": {}}

if "mcpServers" not in config:
    config["mcpServers"] = {}

config["mcpServers"]["sena"] = {
    "command": "uv",
    "args": [
        "--directory",
        repo_path,
        "run",
        "sena-mcp-server"
    ],
    "env": {
        "SENA_MODE": "full"
    }
}

with open(config_path, 'w') as f:
    json.dump(config, f, indent=2)

print("✅ SENA MCP server added to config")
EOF

    echo ""
fi

# ============================================================================
# CLI HOOKS INSTALLATION
# ============================================================================

if [ "$INSTALL_HOOKS" = true ]; then
    echo "════════════════════════════════════════════════════════════════"
    echo "  CLI HOOKS INSTALLATION"
    echo "════════════════════════════════════════════════════════════════"
    echo ""

    HOOKS_DIR="$HOME/.claude/hooks"
    CONTROLLER_DIR="$HOME/.claude/sena_controller_v3.0"

    echo "📁 Installing hooks to: $HOOKS_DIR"
    echo "📁 Installing controller modules to: $CONTROLLER_DIR"

    # Create directories
    mkdir -p "$HOOKS_DIR"
    mkdir -p "$CONTROLLER_DIR"

    # Copy hooks
    echo "Copying hooks..."
    cp -v hooks/*.sh "$HOOKS_DIR/"

    # Make executable
    chmod +x "$HOOKS_DIR"/*.sh

    # Copy controller modules
    echo "Copying controller modules..."
    cp -v controller/*.py "$CONTROLLER_DIR/"
    cp -v controller/VERSION "$CONTROLLER_DIR/" 2>/dev/null || true
    cp -v controller/README.md "$CONTROLLER_DIR/" 2>/dev/null || true

    echo "✅ Hooks installed"
    echo "✅ Controller modules installed"
    echo ""

    # Update Claude Code settings
    CLAUDE_SETTINGS="$HOME/.claude/settings.json"

    if [ ! -f "$CLAUDE_SETTINGS" ]; then
        echo "📄 Creating Claude Code settings..."
        cat > "$CLAUDE_SETTINGS" <<'SETTINGS'
{
  "userPromptSubmitHook": "~/.claude/hooks/user-prompt-submit.sh",
  "assistantResponseSubmitHook": "~/.claude/hooks/sena-enforcer.sh",
  "postToolUseHook": "~/.claude/hooks/post-tool-use.sh"
}
SETTINGS
    else
        echo "⚠️  Claude Code settings exist. Hooks configured at:"
        echo "    $HOOKS_DIR"
        echo ""
        echo "    Add to ~/.claude/settings.json:"
        echo '    "userPromptSubmitHook": "~/.claude/hooks/user-prompt-submit.sh",'
        echo '    "assistantResponseSubmitHook": "~/.claude/hooks/sena-enforcer.sh",'
        echo '    "postToolUseHook": "~/.claude/hooks/post-tool-use.sh"'
    fi
    echo ""

    # Create SENA always-on flag
    touch "$HOME/.claude/.sena_always_on"
    echo "✅ SENA always-on mode enabled"
    echo ""
fi

# ============================================================================
# COMPLETION
# ============================================================================

echo "════════════════════════════════════════════════════════════════"
echo "  🎉 INSTALLATION COMPLETE!"
echo "════════════════════════════════════════════════════════════════"
echo ""

if [ "$INSTALL_MCP" = true ]; then
    echo "📦 MCP Server:"
    echo "   ✅ Installed to: $REPO_PATH"
    echo "   ✅ Added to Claude Desktop config"
    echo "   🔄 Restart Claude Desktop to activate"
    echo ""
fi

if [ "$INSTALL_HOOKS" = true ]; then
    echo "🔧 CLI Hooks:"
    echo "   ✅ Hooks installed to: $HOOKS_DIR"
    echo "   ✅ Controller modules installed to: $CONTROLLER_DIR"
    echo "   ✅ SENA always-on mode enabled"
    echo "   💡 Use in terminal: claude"
    echo ""
fi

echo "📚 Documentation: $REPO_PATH/README.md"
echo "🧪 Test MCP: npx @modelcontextprotocol/inspector uv --directory $REPO_PATH run sena-mcp-server"
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║         SENA 🦁 is ready to enhance your Claude!            ║"
echo "╚══════════════════════════════════════════════════════════════╝"
