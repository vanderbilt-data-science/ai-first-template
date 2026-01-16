# Claude Code Demos: The Agentic Loop in Action
> Feel free to try and practice with these examples on your own!

## Demo Overview

This demo will show what makes Claude Code special: **it doesn't just write code—it runs it, sees the output, and iteratively fixes problems itself.**

**Time**: ~15-20 minutes
**Goal**: We'll see Claude reading files, writing code, executing it, seeing errors, and self-correcting

---

## Demo 1: The Classic "Build Something From Scratch"

### Setup
Create an empty folder before the demo:
```bash
mkdir demo-project && cd demo-project
claude
```

### The 1st Prompt
```
Build me a Python script that:
1. Fetches the current weather for Nashville from a free API
2. Parses the temperature and conditions
3. Prints a friendly message like "It's currently 72°F and sunny in Nashville!"

Use the wttr.in API (it's free, no key needed).
Test it to make sure it works.
```

### What We Will See

Claude will:
1. **Plan** what it needs to do
2. **Write** the Python file (`weather.py`)
3. **Ask permission** to create the file (discuss permission model here!)
4. **Run** the script: `python weather.py`
5. **See the output** or error
6. **Fix any issues** automatically
7. **Re-run** until it works

**Key moment**: When Claude reads its own output and decides what to do next. This is the "agentic loop" — it's not just generating text, it's acting on feedback.

### Try Next
- Open the files in VSCode
- Ask for an edit
- See changes in real time

### Connecting to AI-First Workflow
Notice what just happened:

- We asked for something specific and bounded (one script, one API, one output)
- Claude made decisions we didn't ask about (error handling, extra features?)
- The code works — but is it what you needed?

> **Try** looking at the code Claude wrote. Ask yourself: Did I ask for all of this? Could this be simpler?
> 
> **Practice** pushing back. "This is more than I need. Can you simplify..."

---

## Demo 2: Debug Something Broken (Shows Self-Correction)

### Setup
Create a file with a deliberate bug:

```python
# broken_math.py
def calculate_average(numbers):

    total = sum(numbers)
    return total / len(number)  # typo: 'number' instead of 'numbers'

def main():
    grades = [85, 92, 78, 96, 88]
    avg = calculate_average(grades)
    print(f"Class average: {avg}")
    
if __name__ == "__main__":
    main()
```

### The Prompt
```
Run broken_math.py and fix any errors you find.
```

### What We Will See

Claude will:
1. **Run** the file
2. **See** the NameError
3. **Read** the file to understand context
4. **Identify** the typo
5. **Fix** it (using str_replace or editing)
6. **Run again** to verify
7. **Report** success

**Key moment**: Claude doesn't just pattern-match "NameError" → generic fix. It reads the actual code, understands the intent, and makes a contextual fix.

### Try Next
- Have Claude make a second code (median)
- Run + confirm it works
- Exit Claude code and delete the file
- Try to restore the session and get it back

### Connecting to AI-First Workflow
This is the agentic loop you'll rely on:

- Claude runs → sees error → reads code → fixes → runs again
- You didn't have to interpret the error yourself
- But you _do_ need to verify the fix makes sense

> **Try** looking at the fix. Did Claude fix the root cause or just the symptom?
> 
> **Practice** checking if the fix matches what you intended. Brainstorm how you could verify.
> 
> (This example is simple, so it'll be obvious that it works well. But get used to looking deeply at every error fix it makes and why)


---

## Demo 3: Explore and Understand (Great for Onboarding)

### The Prompt (in any real project folder)
```
What does this project do? Give me a quick overview.
```

Then follow up with:
```
/init
```
See what the CLAUDE.md file is for a project that already has significant work done

### What We Will See

Claude will:
- List directory contents
- Read key files (README, package.json, main scripts)
- Synthesize an explanation
- Find and explain run commands

**Key moment**: This is incredibly useful for onboarding to unfamiliar codebases. Claude becomes your guide. The /init file is a great example of what is crucial for claude to know about this.

### Try Next
- Make an edit to the CLAUDE.md file with #
- Make an edit to the CLAUDE.md file with \memory

### Connecting to AI-First Workflow
This is "ask Claude to propose an approach" in action:

- Before writing code, understand what exists
- Let Claude read and synthesize for you
- Then you decide what to do with that information

The /init command is powerful but imperfect:

> **Try** to review this for a project you know well - what's missing? What's wrong?
> 
> **Practice** editing it to reflect what _you_ know about the project

---

## Demo 4: The Multi-Step Task (Shows Extended Agency)

### The Prompt
```
Create a simple Flask web app that has:
1. A homepage that shows the current time
2. An /about page with some placeholder text
3. Run it on port 5001 and test both routes work

Install any dependencies you need.
```

### What We Will See

Claude will:
1. Check if Flask is installed
2. Install it if needed (`pip install flask`)
3. Create `app.py`
4. Start the server
5. Test the routes (using curl or similar)
6. Report results

**Key moments**:
- Claude handles dependencies itself
- It verifies its own work
- It can run background processes

### Try Next
- Allow this directory to see the weather one as well (claude --add-dir )
- Show the results of weather.py in your flask website

### Connecting to AI-First Workflow
This is where scope creep happens. We asked for 3 things, Claude might add 5. It will design the UI for you if you don't specify. That "About" page will be different every time we try

> **Try** running this prompt again (in a clean folder) and investigating it's plan before accepting. How much code is it trying to write at once? Is the amount a lot or difficult to read through?
>
>**Practice** scoping down. How can a task like this be broken into fewer and done step by step. What else did you need to specify before it started coding?

---

## Interactions to Pay Attention to as You Go

### The Permission System
When Claude asks for permission to do something:
- You'll see three options: **Allow once**, **Allow for session**, **Deny**
- Use `arrow` to change acceptance scope

### Show Extended Thinking (if using Opus)
Press `Tab` during a response to toggle "extended thinking" visibility.

### Recovery
If something goes wrong during any demos, **don't panic**. You can:
- Use `/clear` to start fresh
- Use `Esc Esc` (double-escape) to rewind
- Just ask Claude to try a different approach
