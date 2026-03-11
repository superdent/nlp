"""
export_results.py
Liest alle Modell-Ergebnisse ein und schreibt sie in eine gemeinsame Excel-Datei.
Ablegen im Root des Projekts und von dort ausführen.
"""

from pathlib import Path
import pandas as pd

# ============================================================
# KONFIGURATION
# ============================================================
PROJECT_ROOT = Path(".")          # Root des Projekts (Ablageort dieses Scripts)
OUTPUT_FILE  = PROJECT_ROOT / "results" / "model_comparison.xlsx"
# ============================================================

# Modelle: Name -> Pfad zur CSV
MODELS = {
    "Naive Bayes":         PROJECT_ROOT / "results" / "bayes"    / "metrics" / "naive_bayes_results.csv",
    "SVM":                 PROJECT_ROOT / "results" / "svm"      / "metrics" / "svm_results.csv",
    "Logistic Regression": PROJECT_ROOT / "results" / "logistic" / "metrics" / "logistic_results.csv",
    "Neural Network":      PROJECT_ROOT / "results" / "neural"   / "metrics" / "neural_results.csv",
}

# ============================================================

rows = []
for model_name, path in MODELS.items():
    if path.exists():
        # Separator automatisch erkennen (komma oder semikolon)
        df = pd.read_csv(path, sep=None, engine='python')
        if "Model" not in df.columns:
            df.insert(0, "Model", model_name)
        rows.append(df)
        print(f"✓ {model_name}: {path}")
    else:
        print(f"✗ {model_name}: {path} nicht gefunden, wird übersprungen")

if not rows:
    print("Keine Dateien gefunden. Abbruch.")
else:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    pd.concat(rows, ignore_index=True).to_excel(OUTPUT_FILE, index=False)
    print(f"\n✓ Gespeichert: {OUTPUT_FILE.resolve()}")
