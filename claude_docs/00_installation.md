# Claude Code Installation Guide

### What You Need Before Starting

**Account**: Claude Pro or Max subscription (you should have access through Vanderbilt)

**Time**: 5-10 minutes (unless other installs are needed)

---

## macOS Installation

### Option A: Homebrew - _Recommended_

```bash
brew install --cask claude-code
```

> If you do not yet have homebrew, it can be installed here: https://brew.sh/

### Option B: Direct Install

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### After Installation

```bash
# Navigate to any project folder
cd ~/your-project

# Launch Claude Code
claude
```

First launch will open your browser for authentication. Sign in with your Claude account.

---

## Windows Installation

Windows has **two options**. Choose based on your setup:

### Option 1: WSL (Windows Subsystem for Linux) — _Recommended_

WSL gives you a Linux environment inside Windows. This is the most reliable way to run Claude Code.

**Step 1: Install WSL (if you don't have it)**

Open PowerShell as Administrator and run:
```powershell
wsl --install
```

Restart your computer when prompted, then choose Ubuntu from the Microsoft Store.

**Step 2: Inside your WSL terminal (Ubuntu)**

```bash
# Update your system
sudo apt update && sudo apt upgrade -y

# Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# Start Claude Code
claude
```

### Option 2: Native Windows (Git Bash)

If you have Git for Windows installed, you can run Claude Code natively.

**PowerShell:**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Command Prompt:**
```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**Note**: For portable Git installations, set the bash path first:
```powershell
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
```

---

## First-Time Authentication

When you first run `claude`, it will:

1. Open your default browser
2. Ask you to sign in to your Claude account
3. Complete the OAuth authorization
4. Return you to the terminal, ready to go

**Pro tip**: If you're using Claude Pro/Max subscription, choose that option when prompted. It gives you unified billing with your web Claude usage.

---

## Verify Your Installation

```bash
# Check version
claude --version

# Run health check
claude doctor
```

The `doctor` command checks your installation and reports any issues.

---

## Troubleshooting

### "command not found: claude"

Your PATH might not be updated. Try:
```bash
# Restart your terminal, or:
source ~/.bashrc   # Linux/WSL
source ~/.zshrc    # macOS
```

### Permission errors on Linux/WSL

Don't use `sudo` for installation. If you get permission errors:
```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Windows: Native install fails

Switch to WSL. Native Windows support exists but WSL is more reliable for complex operations.

### Authentication issues

Try:
```bash
claude logout
claude
```

This will restart the authentication flow.

---

## Quick Start After Installation

```bash
# Go to your project
cd ~/my-project

# Start Claude Code
claude

# Or start with an initial prompt
claude "explain this project structure"
```
