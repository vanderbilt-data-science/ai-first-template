# The CLAUDE.md File: Teaching Claude Your Project

## What is CLAUDE.md?

`CLAUDE.md` is a markdown file that gets loaded into Claude's context **every time** you start a session in that directory. Think of it as persistent memory and instructions for your project.

It's onboarding documentation specifically for Claude.

---

## Where Does It Go?

Claude Code uses a **hierarchy** of memory files:

| Location | Scope | Use Case |
|----------|-------|----------|
| `~/.claude/CLAUDE.md` | All projects | Your personal preferences |
| `./CLAUDE.md` | This project | Team-shared project context |
| `./.claude/CLAUDE.md` | This project | Alternative project location |
| `./CLAUDE.local.md` | This project | Personal project notes (gitignored) |

**Loading order**: User-level → Project-level (later files have higher priority)

---

## Starting a New Project

### If You have Existing Code: Use `/init`

If you already have some project files in a directory, you can use the `/init` command to have claude analyze your codebase and generate a starter `CLAUDE.md`:

```
/init
```

Claude will:
1. Scan your project structure
2. Read package.json, README, configs
3. Identify key patterns and conventions
4. Generate a CLAUDE.md with what it found

**Important**: The generated file is a starting point. Review and refine it based on your actual workflow, and edit it as the project matures.

---

### For an Empty Repo

If you're starting fresh, don't use `/init` on an empty folder. Instead:

**Option 1: Write it yourself**
Create `CLAUDE.md` manually with basic project info:

```markdown
# Project: My App

## Overview
A web application that [does X].

## Tech Stack
- Python 3.11 + Flask
- SQLite for development
- Tailwind CSS

## Commands
- Run dev server: `python app.py`
- Run tests: `pytest`

## Conventions
- Use type hints for all functions
- Keep functions under 50 lines
```

**Option 2: Have Claude write it from a conversation**
```
Create a CLAUDE.md file for this project. 
It's a [describe your project].
We're using [your tech stack].
Our testing approach is [your approach].
```

Then review and commit the result.

---

## What Should Go in CLAUDE.md?

The content depends on your project type and goals. Research projects, for instance, will need different context than software projects. In practice, many data science projects are a mix of both!

More so in the research case, where project knowledge is constantly evolving, but even in the software case, work on the project should pair with updates to the CLAUDE.md file.
The more that you learn, explore, rule out, etc, the more critical context there is for every new session to know.

---

### Research-Focused CLAUDE.md Decriptions

Research work benefits from **goal and context-heavy** CLAUDE.md files. Claude needs to understand *what you're trying to accomplish* and *why*, not just how to run scripts. 

**Project Goals & Research Questions**
```markdown
## Research Goal
We're investigating whether fine-tuned small language models can match 
GPT-4 performance on dialogic reading question generation for preschoolers,
at a fraction of the inference cost.

## Key Questions
1. What's the minimum model size that achieves acceptable quality?
2. Does DPO training improve pedagogical appropriateness over SFT alone?
3. How do we measure "quality" for this use case? (accuracy vs. engagement)
```

**Important Decisions & Rationale**
```markdown
## Key Choices
- Base model: Granite-3B (IBM's model, licensed for commercial use via our collaboration)
- Training approach: SFT first, then DPO — we tried RLHF but reward model was unstable
- Evaluation: Human eval + automated metrics (BLEU is not meaningful here, using custom rubric)

## What We've Tried (and why we moved on)
- LLaMA-7B: Better quality but too slow for real-time generation
- Prompt-only approach: Inconsistent output format, couldn't control reading level
```

**Deliverables & Timeline**
```markdown
## Deliverables
1. Fine-tuned model checkpoint (target: end of month)
2. Evaluation dataset with human annotations
3. Short paper for EMNLP workshop submission (deadline: March 15)

## Current Phase
Training pipeline is working. Currently running ablations on DPO hyperparameters.
```

**Domain Background** (if Claude needs it)
```markdown
## Background
Dialogic reading is a technique where adults ask children questions during 
read-alouds to promote engagement. Questions follow the PEER sequence:
Prompt, Evaluate, Expand, Repeat. Our model generates the Prompt step.
```

**Data & Constraints**
```markdown
## Data
- Training: 12k book-question pairs from [source]
- Eval: 500 held-out pairs with human quality ratings
- NOT included: Any data from copyrighted children's books post-1927

## Constraints
- Must run on single A100 (our allocation limit)
- Model must be <7B params for deployment on partner's infrastructure
```

---

### Software-Focused CLAUDE.md Decriptions

Software projects need **how-to-run** context more than research rationale.

**Build/Run Commands**
```markdown
## Commands
- Start dev server: `npm run dev`
- Run tests: `npm test`
- Build for production: `npm run build`
```

**Project Architecture** (brief)
```markdown
## Structure
- `/src/api` - Backend endpoints
- `/src/components` - React components  
- `/src/utils` - Shared utilities
```

**Critical Conventions**
```markdown
## Code Style
- We use TypeScript strict mode
- All API responses use the Result<T, E> pattern
- Tests go next to source files as `.test.ts`
```

### Useful (Medium Value)

**Environment Setup**
```markdown
## Setup
Requires Node 18+. Run `npm install` then `cp .env.example .env`
```

**Common Gotchas**
```markdown
## Warnings
- Don't edit files in /generated - they're auto-created
- The auth service must be running for tests to pass
```

### Avoid (Low Value, High Cost)

- Exhaustive style guides - some guidance is great, long guides waste context.
- Things that change frequently - it can be difficult to constantly track and edit those changes. CLAUDE.md should be something mostly *added* to, if possible.
- Sensitive information (API keys, credentials) - the CLAUDE.md is meant to be shared, API keys are not
- Generic advice Claude already knows - it might take some experimentation to see what this is!
- Duplicating what's in the README — if it's already documented elsewhere, link to it instead of copying

---

## The # Quick-Add Shortcut

During any conversation, you can add to memory on the fly:

```
# Always use async/await instead of .then() chains
```

Claude will ask which memory file to save it to:
1. Project memory (`./CLAUDE.md`)
2. Personal memory (`~/.claude/CLAUDE.md`)

This is great for capturing conventions as you discover them.

---

## Critical Habit: Capture As You Go

**This is important and not obvious**: Claude Code doesn't remember your past conversations. When a session ends, everything you discussed is gone — unless you saved it to CLAUDE.md.

You might spend an hour debugging and discover:
- "The model doesn't reload properly at testing time if it was quantized for training"
- "That model was super overfit, we're going to need to try different hyperparameters"
- "I need to move a bunch of code to `legacy` since I might need it later, but want to rewrite for now"

If you don't capture these insights, they're lost. Next session, you (or Claude) will rediscover them the hard way.

**The fix**: Build a habit of using `#` whenever you learn something important:

```
# [Model} doesn't reload properly when quanitized on training

# LoRA rank 64, overfit for all learning rates tries (5e-6, 2e-5, 2e-4)

# /legacy if just old tests - don't use any parts of it in any new codes
```

### Why /init Doesn't Solve This

You might think "I'll just re-run `/init` later and it'll figure everything out." 

**It won't.** `/init` analyzes your *code* — file structure, configs, READMEs, patterns it can detect. It doesn't know:
- Decisions you made in past conversations
- Gotchas you discovered through debugging
- Context about why code is the way it is
- Your preferences for how Claude should work

`/init` is great for bootstrapping. But the real value of CLAUDE.md comes from the knowledge you accumulate as you work on a project — and that only gets there if you capture it in the moment. 

### End-of-Session Habit

If you forget to `#` things during a session, take 30 seconds at the end:

```
Before we wrap up, add to the project CLAUDE.md anything important 
we learned this session — gotchas, conventions, or decisions we made.
```

Claude will suggest additions based on the current conversation. Review them and approve what's useful.

---

## The /memory Command

Open your memory files directly for editing:

```
/memory
```

This opens your CLAUDE.md in your system editor for bulk updates.

---

## Importing Other Files

CLAUDE.md can reference other files with `@` syntax:

```markdown
# Project Instructions

See @README.md for project overview.
See @docs/api.md for API documentation.
```

This keeps CLAUDE.md concise while making detailed docs available.

---

## Organizing Larger Projects

For big projects, using a `.claude/rules/` directory can be helpful to avoid the CLAUDE.md getting massive:

```
.claude/
├── CLAUDE.md           # Main project instructions
└── rules/
    ├── code-style.md   # Style guidelines
    ├── testing.md      # Testing conventions
    └── api.md          # API patterns
```

All `.md` files in `rules/` are automatically loaded.

---

## Best Practices Summary

1. **Keep it concise** — Every word costs context tokens
2. **Be specific** — "Use 2-space indentation" beats "Format code properly"
3. **Focus on what's unique** — Don't repeat things Claude knows
4. **Update iteratively** — Add rules as you discover patterns
5. **Commit to version control** — Share with your team
6. **Use .local.md for personal notes** — Keep private preferences separate
7. **Don't repeat things evident in the code or README.md** - Remember, claude can see *everything* in the directory. If something is self-evident in the code or stated already in the README, you don't need to say it again!

---

## Example: Minimal but Effective

### Research Project Example

```markdown
# GW Event Classification

## Goal
Build a classifier that distinguishes binary black hole mergers from 
neutron star mergers using only the first 0.5s of gravitational wave signal.
Target: >90% accuracy on O4 data.

## Current Status
Feature extraction pipeline complete. Training XGBoost baselines now.
Next: test CNN on raw spectrograms.

## Key Choices
- Using O3 data for training (O4 reserved for final eval)
- SNR threshold: 8 (below this, signals too noisy)
- NOT using matched filtering — too slow for real-time detection goal

## Commands
- Extract features: `python extract_features.py --run O3`
- Train model: `python train.py --model xgboost`
- Evaluate: `python eval.py --checkpoint models/latest.pkl`

## Data
- Training: /data/O3_events/ (1,247 confirmed events)
- Test: /data/O4_events/ (DO NOT use until final eval)
```

A starting CLAUDE.md can be effective in only ~15-20 lines. Enough context to be useful, concise enough to not waste tokens.

---

## Anti-Pattern: The Kitchen Sink

Don't do this:

```markdown
# Project

## Code Style
- Use 4 spaces for indentation
- Use single quotes for strings
- Add a newline at end of files
- Keep lines under 80 characters
- Use snake_case for variables
- Use PascalCase for classes
- ... [50 more rules]

## Git Workflow  
- Always create a branch
- Use conventional commits
- ... [20 more rules]
```

This wastes context on things Claude knows or can infer. It also leads to instruction fatigue - Claude can ignore rules buried in walls of text if it has too much information.
