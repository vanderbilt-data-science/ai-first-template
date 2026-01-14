# Claude Code Quick Reference

If you've already read through the other docs here and just want a quick reference guide, this is meant to serve as a "reminder" of the essential ways of interacting with claude code!

## Install
```bash
# macOS
brew install --cask claude-code
# or: curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
# Recommended: Use WSL instead for best experience
```

## Start
```bash
claude                    # Start interactive session
claude "your prompt"      # Start with initial prompt
claude -c                 # Continue last session
```

## Essential Commands
| Command | Action |
|---------|--------|
| `/help` | List all commands |
| `/clear` | Clear conversation |
| `/compact` | Compress context |
| `/context` | Show token usage |
| `/memory` | Edit CLAUDE.md |
| `/init` | Generate CLAUDE.md |

## Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `Esc Esc` | **Rewind** (undo) |
| `Tab` | Toggle thinking |
| `Ctrl+C` | Cancel |
| `Ctrl+R` | Search history |

## Quick Input
| Prefix | What it does |
|--------|--------------|
| `#` | Add to memory |
| `@` | Reference file |
| `!` | Run shell command |

## CLAUDE.md (Project Memory)
```bash
/init              # Auto-generate from project
/memory            # Edit directly
# My note here     # Quick-add during chat
```

**Location**: `./CLAUDE.md` (project) or `~/.claude/CLAUDE.md` (global)

## Permissions
When Claude asks permission:
- `y` = allow once
- `n` = deny  
- `Tab` = change scope

## Troubleshooting
```bash
claude doctor      # Health check
claude --version   # Check version
```

---
**Docs**: code.claude.com/docs
