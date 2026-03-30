# ML Experiment Tracker

## What this is
A lightweight tool for tracking fine-tuning experiments on text classification.
We're comparing BERT variants (bert-base, distilbert, roberta-base) on a
document classification task. Goal: find the best accuracy/compute tradeoff
before scaling up.

## Current status
Running ablations on learning rate and epoch count. RoBERTa is winning on
accuracy but distilbert is the efficiency leader. Decision pending on which
to use for production — see notes in experiments.csv.

## Key decisions made
- Using val_accuracy as primary metric (not F1) — class balance is acceptable
- Training time measured in minutes on a single A100
- Batch size 16 is our default; only vary it intentionally
- We are NOT using the test set yet — that's reserved for the final model

## Commands
- Run tracker: `python tracker.py`
- Add new results: append a row to results/experiments.csv (match the header exactly)
- View full JSON: `python tracker.py > output.json`

## What we've ruled out
- Learning rates above 3e-5 are consistently unstable for all model types
- Batch size 8 is not worth it — marginal accuracy gain, huge compute cost
- bert-large: too slow for our A100 allocation, not in scope

## Next steps
- Build a dashboard to visualize results (see visualization skill)
- Run roberta_tuned config 3 more times to confirm it's not a lucky seed
- Write up efficiency comparison for the team meeting

## Notes for Claude
- The results/ directory may have multiple CSV files eventually — tracker.py
  currently only reads experiments.csv. Don't assume there's only one.
- efficiency_score = val_accuracy / train_time_mins. Higher is better.
- Do not touch results/experiments.csv unless explicitly asked — it's our
  source of truth and not auto-generated.
