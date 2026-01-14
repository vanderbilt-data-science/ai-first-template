# Claude Code Commands & Features Cheat Sheet

## Starting Claude Code

```bash
# Start interactive session in current directory
claude

# Start with an initial prompt
claude "explain this codebase"

# Continue last session
claude -c

# Resume a specific session
claude -r
```

---

## Essential Slash Commands

| Command | What It Does |
|---------|--------------|
| `/help` | List all available commands |
| `/clear` | Clear conversation history (start fresh) |
| `/compact` | Compress context to save tokens |
| `/context` | Show current context/token usage |
| `/cost` | Show token usage and cost for session |
| `/status` | Show model, settings, connection status |
| `/memory` | Open CLAUDE.md files for editing |
| `/init` | Generate a CLAUDE.md from project analysis |
| `/permissions` | View/manage tool permissions |
| `/review` | Request a code review |
| `/model` | Switch between models (Sonnet/Opus) |

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel current operation |
| `Ctrl+R` | Search command history |
| `Ctrl+L` | Clear screen (keeps conversation) |
| `Tab` | Toggle extended thinking mode |
| `Shift+Tab` | Toggle permission modes |
| `Esc Esc` | **Rewind** — undo to previous point |
| `Ctrl+B` | Run bash in background |

**Rewind is powerful**: Double-tap Escape to undo Claude's changes and go back to a previous state in the conversation.

---

## Quick Input Shortcuts

| Prefix | What It Does |
|--------|--------------|
| `#` | Add to memory (CLAUDE.md) |
| `@` | Reference a file/path |
| `!` | Run shell command directly |
| `/` | Slash command |

**Examples:**
```
# Always use TypeScript strict mode    → Saves to memory
@src/utils/auth.ts                      → References this file
!git status                             → Runs git status directly
/compact                                → Compresses context
```

---

## Session Management

### Continue Previous Sessions

```bash
# Continue the most recent session
claude -c

# Resume and select from recent sessions
claude -r
```

### Managing Context

```
# Check how much context you've used
/context

# Compress the conversation (keeps important info)
/compact

# Or with a hint about what to preserve
/compact "keep the database schema discussion"

# Nuclear option: clear everything
/clear
```

---

## Permission System

Claude asks before performing sensitive actions. When prompted:

- **y** — Allow this once
- **n** — Deny
- **Tab** — Cycle through scope options:
  - Allow once
  - Allow for this session
  - Always allow (for this project)

---

## Custom Slash Commands

Create your own commands as markdown files:

### Project Commands (shared with team)
```bash
# Create the commands directory
mkdir -p .claude/commands

# Create a command
echo "Review this code for security issues:" > .claude/commands/security.md
```

Now `/security` works in this project!

### Personal Commands (all your projects)
```bash
mkdir -p ~/.claude/commands
echo "Explain this code like I'm a beginner:" > ~/.claude/commands/eli5.md
```

### With Arguments
Commands can accept arguments using `$ARGUMENTS`:

```markdown
<!-- .claude/commands/test.md -->
Run tests for the following component and fix any failures:
$ARGUMENTS
```

Usage: `/test Button.tsx`

---

## Multi-Directory Access

```bash
# Add additional directories Claude can access
claude --add-dir ../shared-libs --add-dir ../common
```

---

## Headless / Scripting Mode

Run Claude non-interactively for scripts and CI:

```bash
# Single prompt, exit after response
claude -p "summarize this project's README"

# Pipe input
cat error.log | claude -p "what's the root cause?"

# JSON output for scripting
claude -p "list all TODO comments" --output-format json
```

---

## Skills vs. Custom Commands

| Feature | Custom Commands | Skills |
|---------|-----------------|--------|
| Triggered by | You type `/command` | Claude decides automatically |
| Complexity | Simple prompts | Multi-file, scripts, complex workflows |
| Location | `.claude/commands/` | `.claude/skills/` |

Skills are more advanced—Claude loads them when it recognizes a relevant task.

---

## Troubleshooting Commands

```bash
# Health check
claude doctor

# Verbose logging
claude --verbose

# Debug MCP connections
claude --mcp-debug

# Check what tools/permissions are available
/permissions
```

---

## Settings Files

| File | Purpose |
|------|---------|
| `~/.claude/settings.json` | User-level settings |
| `.claude/settings.json` | Project-level settings |
| `~/.claude/CLAUDE.md` | Personal memory (all projects) |
| `./CLAUDE.md` | Project memory |
| `./CLAUDE.local.md` | Personal project notes (gitignored) |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│  STARTING                                                │
│  claude              Start session                       │
│  claude -c           Continue last session               │
│  claude "prompt"     Start with initial prompt           │
├─────────────────────────────────────────────────────────┤
│  DURING SESSION                                          │
│  /help               Show commands                       │
│  /clear              Fresh start                         │
│  /compact            Save context tokens                 │
│  /context            Check token usage                   │
│  /memory             Edit CLAUDE.md                      │
│  Esc Esc             Rewind changes                      │
├─────────────────────────────────────────────────────────┤
│  QUICK INPUT                                             │
│  # text              Add to memory                       │
│  @file               Reference file                      │
│  !cmd                Run shell directly                  │
├─────────────────────────────────────────────────────────┤
│  SCRIPTING                                               │
│  claude -p "..."     Headless single prompt              │
│  cat x | claude -p   Pipe input                          │
└─────────────────────────────────────────────────────────┘
```

---

## Advanced

These features are powerful but typically not needed for smaller projects or most data science work. 
Feel free to skip this section entirely! These are some additional extra features that are good to know about, but that most likely you won't find yourself needing.

### Useful Environment Variables

You can set environment variables to change Claude Code's default behavior.

**When you'd use this:** You have very specific settings you want to be the default. The two below are really the only potentially relevant.

```bash
# Disable auto-updates
export DISABLE_AUTOUPDATER=1 #if updates are really disruptive, probably wouldn't use

# Use a specific model
export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929" # only if a very specific model is best for your use case, otherwise /model
```


### Pre-configure Permissions
You can set a configuration for the general permissions (allow, deny) for specific commands in the `settings.json` file.

**When you'd use this:** You're tired of typing "y" to approve the same commands over and over. Or you want to make sure Claude *never* touches certain files.

In `~/.claude/settings.json` or `.claude/settings.json`:
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(pytest *)",
      "Read(*)"
    ],
    "deny": [
      "Read(.env*)",
      "Bash(rm -rf *)"
    ]
  }
}
```

**Practical examples:**
- `"allow": ["Bash(pytest *)"]` — Stop approving every test run
- `"deny": ["Read(.env*)"]` — Protect files with API keys or secrets

For a shared project, you can put these in `.claude/settings.json` and commit it so the whole team has the same guardrails.

### MCP (Model Context Protocol)

MCP extends Claude Code with external tools—databases, APIs, services.

**When you'd use this:** You want Claude Code to interact with an external service directly — like querying a database, creating GitHub issues, or accessing an API.

```bash
# List configured MCP servers
claude mcp list

# Add an MCP server
claude mcp add <name> <command>

# Add with environment variables
claude mcp add --transport stdio myserver \
  --env API_KEY=xxx -- npx my-mcp-server

# Remove a server
claude mcp remove <name>
```

#### Examples

```bash
# GitHub integration
claude mcp add github -- npx @modelcontextprotocol/server-github
```

### Hooks (Automated Actions)

Hooks run a set scripts when Claude does certain things.

**When you'd use this:** You want something to happen automatically every time Claude does a specific action — like auto-formatting code or running a test after Claude writes a file.

In `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.py)",
        "hooks": [
          {
            "type": "command",
            "command": "black \"$file\""
          }
        ]
      }
    ]
  }
}
```

This one is usually only useful if you're working on a team with *strict* code formatting requirements, or *heavy, specific* testing is needed. It's not typically used for individuals or small projects.
