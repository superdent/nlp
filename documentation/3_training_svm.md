# Phase 3: Modelltraining – SVM

## Konfiguration

| Parameter       | Wert                                           |
|-----------------|------------------------------------------------|
| Algorithmus     | LinearSVC                                      |
| C               | 1.0 (Regularisierungsstärke)                   |
| Max. Iterationen| 2.000                                          |
| Vektorisierung  | TF-IDF                                         |
| Max. Features   | 10.000                                         |
| min_df          | 2                                              |
| max_df          | 0.95                                           |
| N-Gramm-Bereich | (1, 2) – Uni- und Bigramme                     |
| Stoppwörter     | Englisch                                       |
| sublinear_tf    | False                                          |
| Input           | Titel + Text (kombiniert)                      |
| Trainingsdaten  | `train_0_50000_70_15_15.jsonl` (140.000)       |
| Validierungsdaten | `val_0_50000_70_15_15.jsonl` (30.000)        |
| Testdaten       | `test_0_50000_70_15_15.jsonl` (30.000)         |

## Ergebnisse

| Metrik              | Wert   |
|---------------------|--------|
| Validation Accuracy | 0.7104 |
| Test Accuracy       | 0.7244 |

## Artefakte

- Modell: `results/svm/models/svm_model.pkl`
- Vektorisierer: `results/svm/models/svm_vectorizer.pkl`
- Metriken (JSON): `results/svm/metrics/svm_metrics.json`
- Metriken (CSV): `results/svm/metrics/svm_results.csv`
- Confusion Matrix: `results/svm/figures/confusion_matrix_svm.png`
