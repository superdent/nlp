# Phase 3: Modelltraining – Logistische Regression

## Konfiguration

| Parameter         | Wert                                           |
|-------------------|------------------------------------------------|
| Algorithmus       | LogisticRegression                             |
| C                 | 1.0 (Regularisierungsstärke)                   |
| Max. Iterationen  | 1.000                                          |
| Solver            | saga                                           |
| Vektorisierung    | TF-IDF                                         |
| Max. Features     | 10.000                                         |
| min_df            | 2                                              |
| max_df            | 0.95                                           |
| N-Gramm-Bereich   | (1, 2) – Uni- und Bigramme                     |
| Stoppwörter       | Englisch                                       |
| sublinear_tf      | False                                          |
| Input             | Titel + Text (kombiniert)                      |
| Trainingsdaten    | `train_0_50000_70_15_15.jsonl` (140.000)       |
| Validierungsdaten | `val_0_50000_70_15_15.jsonl` (30.000)          |
| Testdaten         | `test_0_50000_70_15_15.jsonl` (30.000)         |

## Ergebnisse

| Metrik              | Wert   |
|---------------------|--------|
| Validation Accuracy | 0.7178 |
| Test Accuracy       | 0.7299 |

## Artefakte

- Modell: `results/logistic/models/logistic_model.pkl`
- Vektorisierer: `results/logistic/models/logistic_vectorizer.pkl`
- Metriken (JSON): `results/logistic/metrics/logistic_metrics.json`
- Metriken (CSV): `results/logistic/metrics/logistic_results.csv`
- Confusion Matrix: `results/logistic/figures/confusion_matrix_logistic.png`
