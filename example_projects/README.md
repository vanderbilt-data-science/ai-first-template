# example-project

A simple example project to see and test Claude Code in action.

Includes a few files from the get-go, and then some suggested tasks to ask Claude Code about to see how it works in practice on a real codebase, real tasks, without needing to put in (yet!) on any real work you're doing.

---

Suggested things to try: 

In `broken_math.py`:
1. Ask Claude Code to debug. Watch it run to find the error, fix it, and check that it works.


In `ml-tracker`:
1. Open the directory in the terminal. Inspect the CLAUDE.md. Note what kinds of things are in there.
2. Look at .claude/skills/visualization.md. Only the name and first line are loaded upfron, but the full content injects when Claude decides it's relevant.
3. Hit `Shift+Tab` until you enter plan mode. Try: "Build a dashboard to visualize the experiment results."
4. Watch Claude: it reads `tracker.py` to understand the data structures, reads `experiments.csv`, triggers the visualization skill (you'll see it load), then proposes a plan. `Ctrl+o` to expand what it's reading. Review it's plan. Try to add or edit something.
5. Approve the plan and allow edits. Watch it execute — install packages, write app.py, run streamlit run app.py.
6. Inspect the dashboard that shows up. Feel free to try iterating and tweaking anything you want!
