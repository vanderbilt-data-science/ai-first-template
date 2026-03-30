---
name: visualization
description: Build a Streamlit dashboard to visualize ML experiment results from this tracker project. Use when asked to add a dashboard, UI, visualization, or chart for experiment results.
---

# Visualization skill: Streamlit dashboard for ml-tracker

## When to use this skill
Use this skill any time the user asks to visualize, chart, display, or build a
UI for the experiment results. This skill is specific to this project's data
structure and tracker.py interface.

## Dependencies
Install before building:
```bash
pip install streamlit plotly pandas
```
Update requirements.txt to uncomment the streamlit and plotly lines.

## File to create
Create `app.py` in the project root. Do not modify tracker.py.

## How to import tracker data
Import directly from tracker.py — do not re-implement the CSV loading logic:
```python
from tracker import load_experiments, summarize

experiments = load_experiments()
summary = summarize(experiments)
```
Convert experiments to a DataFrame for Plotly/Streamlit:
```python
import pandas as pd
df = pd.DataFrame([vars(e) for e in experiments])
df["efficiency"] = df["val_accuracy"] / df["train_time_mins"]
```

## Required dashboard sections
Build these four sections in order:

### 1. Header metrics row
Three `st.metric` cards side by side:
- Best accuracy (and which experiment)
- Most efficient run (accuracy/min, and which experiment)  
- Total experiments run

### 2. Accuracy vs. training time scatter plot
Use `plotly.express.scatter`:
- x = train_time_mins, y = val_accuracy
- color = model_type (use the model_type column)
- size = epochs (to show effect of training longer)
- hover_data = ["name", "learning_rate", "notes"]
- Title: "Accuracy vs. training time"

### 3. Rankings table
Use `st.dataframe` with these columns only (in this order):
name, model_type, val_accuracy, val_loss, train_time_mins, efficiency
Sort by val_accuracy descending. Format val_accuracy and val_loss to 3 decimal places.

### 4. Per-model-type bar chart
Use `plotly.express.bar`:
- x = model_type, y = val_accuracy
- color = model_type
- Show only best run per model type (not all runs)
- Title: "Best accuracy by model type"

## Streamlit layout pattern to follow
```python
import streamlit as st

st.set_page_config(page_title="ML Experiment Tracker", layout="wide")
st.title("ML Experiment Tracker")

# metrics row
col1, col2, col3 = st.columns(3)
# ... metrics here

# scatter plot
st.subheader("Accuracy vs. training time")
# ... chart here

# two columns for table + bar chart
left, right = st.columns([2, 1])
with left:
    st.subheader("All experiments")
    # ... table here
with right:
    st.subheader("Best by model type")
    # ... bar chart here
```

## How to run
```bash
streamlit run app.py
```
Runs on localhost:8501 by default.

## What NOT to do
- Do not hardcode any values from experiments.csv — always load via tracker.py
- Do not recreate the CSV parsing logic
- Do not add authentication, database connections, or file upload features
- Keep it to one file (app.py) unless there's a strong reason to split
