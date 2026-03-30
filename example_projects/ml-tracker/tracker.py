"""
ML Experiment Tracker
Loads experiment results from CSV files in results/ and provides
summary statistics, rankings, and efficiency metrics.
"""

import csv
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional


RESULTS_DIR = Path(__file__).parent / "results"


@dataclass
class Experiment:
    name: str
    model_type: str
    learning_rate: float
    epochs: int
    batch_size: int
    val_accuracy: float
    val_loss: float
    train_time_mins: float
    notes: str

    @property
    def efficiency_score(self) -> float:
        """Accuracy per minute of training — higher is better."""
        return self.val_accuracy / self.train_time_mins if self.train_time_mins > 0 else 0.0


def load_experiments(csv_path: Optional[Path] = None) -> list[Experiment]:
    """Load all experiments from a CSV file."""
    path = csv_path or RESULTS_DIR / "experiments.csv"
    if not path.exists():
        raise FileNotFoundError(f"No results file found at {path}")

    experiments = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            experiments.append(Experiment(
                name=row["experiment_name"],
                model_type=row["model_type"],
                learning_rate=float(row["learning_rate"]),
                epochs=int(row["epochs"]),
                batch_size=int(row["batch_size"]),
                val_accuracy=float(row["val_accuracy"]),
                val_loss=float(row["val_loss"]),
                train_time_mins=float(row["train_time_mins"]),
                notes=row["notes"],
            ))
    return experiments


def summarize(experiments: list[Experiment]) -> dict:
    """Return a summary dict: best model, per-model-type stats, rankings."""
    if not experiments:
        return {}

    best = max(experiments, key=lambda e: e.val_accuracy)
    most_efficient = max(experiments, key=lambda e: e.efficiency_score)

    by_model = {}
    for exp in experiments:
        by_model.setdefault(exp.model_type, []).append(exp)

    model_summary = {}
    for model_type, exps in by_model.items():
        best_in_group = max(exps, key=lambda e: e.val_accuracy)
        model_summary[model_type] = {
            "run_count": len(exps),
            "best_accuracy": best_in_group.val_accuracy,
            "best_run": best_in_group.name,
            "avg_train_time_mins": round(sum(e.train_time_mins for e in exps) / len(exps), 1),
        }

    ranked = sorted(experiments, key=lambda e: e.val_accuracy, reverse=True)

    return {
        "total_experiments": len(experiments),
        "best_model": asdict(best),
        "most_efficient": asdict(most_efficient),
        "by_model_type": model_summary,
        "rankings": [
            {"rank": i + 1, "name": e.name, "val_accuracy": e.val_accuracy,
             "val_loss": e.val_loss, "train_time_mins": e.train_time_mins,
             "efficiency": round(e.efficiency_score, 4)}
            for i, e in enumerate(ranked)
        ],
    }


def print_summary(summary: dict) -> None:
    """Pretty-print the summary to stdout."""
    print(f"\n{'='*50}")
    print(f"  ML Experiment Summary")
    print(f"{'='*50}")
    print(f"  Total experiments: {summary['total_experiments']}")
    print(f"\n  Best model:")
    best = summary["best_model"]
    print(f"    {best['name']} ({best['model_type']})")
    print(f"    Accuracy: {best['val_accuracy']:.3f}  Loss: {best['val_loss']:.3f}")
    print(f"    Training time: {best['train_time_mins']} mins")

    print(f"\n  Most efficient (accuracy/min):")
    eff = summary["most_efficient"]
    print(f"    {eff['name']} — {eff['val_accuracy']:.3f} acc in {eff['train_time_mins']} mins")

    print(f"\n  By model type:")
    for model_type, stats in summary["by_model_type"].items():
        print(f"    {model_type}: {stats['run_count']} runs, "
              f"best={stats['best_accuracy']:.3f} ({stats['best_run']})")

    print(f"\n  Top 5 by accuracy:")
    for r in summary["rankings"][:5]:
        print(f"    #{r['rank']} {r['name']}: {r['val_accuracy']:.3f}")
    print()


if __name__ == "__main__":
    experiments = load_experiments()
    summary = summarize(experiments)
    print_summary(summary)
    print("Full JSON output:")
    print(json.dumps(summary, indent=2))
