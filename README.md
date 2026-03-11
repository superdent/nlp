# Sentimentanalyse von Produktrezensionen

Textklassifizierungssystem zur numerischen Bewertung (1-5) von Produktrezensionen.

**Kurs:** DLBAIPNLP01_D – Projekt: NLP

---

## Datensätze

Quelle: [McAuley Lab Amazon Reviews 2023](https://amazon-reviews-2023.github.io/)

---

## Verzeichnisstruktur

```
data/raw/              # Rohdaten (JSONL-Dateien)
data/splits/           # Aufgeteilte Datensätze (Train/Validation/Test)
src/                   # Python-Scripts
notebooks/             # Jupyter Notebooks
results/               # Modelle, Metriken, Visualisierungen
documentation/         # Dokumentation der Projektphasen
```

---

## Python Version

3.11.4

---

## Dokumentation

- `documentation/1_vorbereitung.md` – Setup, Repository, Datenbeschaffung
- `documentation/phase1_eda_report.md` – Explorative Datenanalyse
- `documentation/2_vorverarbeitung.md` – EDA, Splits
- `documentation/modellauswahl.md` – Modellauswahl und Begründung
- `documentation/3_naive_bayes.md` – Training und Evaluierung Naive Bayes
- `documentation/3_svm.md` – Training und Evaluierung SVM
- `documentation/3_logistic_regression.md` – Training und Evaluierung Logistische Regression
- `documentation/3_neural_network.md` – Training und Evaluierung Neuronales Netz
