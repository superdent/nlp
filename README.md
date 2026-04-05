# Sentimentanalyse von Produktrezensionen

Textklassifizierungssystem zur numerischen Bewertung (1–5) von Amazon-Produktrezensionen.

**Kurs:** DLBAIPNLP01_D – Projekt: NLP

## Datensatz

Quelle: [McAuley Lab Amazon Reviews 2023](https://amazon-reviews-2023.github.io/)

Format: JSONL. Die Rohdaten sind nicht im Repository enthalten. JSONL-Dateien herunterladen und unter `data/raw/` ablegen.

Produktkategorien:
- Movies & TV
- All Beauty
- Office Products

## Installation

Python 3.11.4

```
pip install -r requirements.txt
```

## Verzeichnisstruktur

```
data/raw/              # Rohdaten (JSONL)
data/splits/           # Train/Validation/Test-Splits
src/                   # Python-Scripts
notebooks/             # Jupyter Notebooks (Training)
results/               # Modelle, Metriken, Konfusionsmatrizen
documentation/         # EDA-Report, Diagramme
```

## Scripts

| Script | Beschreibung |
|--------|-------------|
| split.py | Rohdaten in Train/Validation/Test aufteilen |
| raw_data_analysis.py | EDA-Report erzeugen |
| category_distribution.py | Bewertungsverteilung in Split-Dateien zählen |
| export_results.py | Metriken aller Runs in overview.csv zusammenfassen |
| create_appendix_a.py | Excel-Export für Anhang A des Projektberichts |
| three_three_matrix.py | 3-Klassen-Konfusionsmatrix aus 5-Klassen-Ergebnissen ableiten |
| create_roc.py | Erzeugt ein ROC-Diagramm für alle vier Modelle |

## Notebooks

| Notebook | Modell |
|----------|--------|
| train_naive_bayes.ipynb | Naive Bayes (MultinomialNB) |
| train_svm.ipynb | Support Vector Machine (LinearSVC) |
| train_logistic_regression.ipynb | Logistische Regression |
| train_neural_network.ipynb | Neuronales Netz (Keras Sequential) |