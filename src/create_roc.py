import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from pathlib import Path

PROJECT_ROOT = Path(".")

RUNS = {
    "Naive Bayes": PROJECT_ROOT / "results" / "bayes" / "runs" / "run_03_30000k",
    "SVM": PROJECT_ROOT / "results" / "svm" / "runs" / "run_06_30000k",
    "Logistic Regression": PROJECT_ROOT / "results" / "logistic" / "runs" / "run_07_30000k",
    "Neural Network": PROJECT_ROOT / "results" / "neural" / "runs" / "run_08_30000k",
}

CLASSES = [1, 2, 3, 4, 5]
OUTPUT_PATH = PROJECT_ROOT / "documentation" / "roc_comparison.png"

plt.figure(figsize=(8, 6))

for name, run_dir in RUNS.items():
    y_test = np.load(run_dir / "y_test.npy")
    y_proba = np.load(run_dir / "y_proba.npy")

    y_bin = label_binarize(y_test, classes=CLASSES)

    fpr = {}
    tpr = {}
    roc_auc = {}
    for i, cls in enumerate(CLASSES):
        fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_proba[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(len(CLASSES))]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(len(CLASSES)):
        mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= len(CLASSES)
    macro_auc = auc(all_fpr, mean_tpr)

    plt.plot(all_fpr, mean_tpr, label=f"{name} (AUC = {macro_auc:.4f})")

plt.plot([0, 1], [0, 1], "k--", label="Zufall")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC-Kurven (Macro-Average)")
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig(OUTPUT_PATH, dpi=150)
plt.close()

print(f"Gespeichert: {OUTPUT_PATH}")