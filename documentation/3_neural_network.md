# Phase 3: Modelltraining – Neuronales Netz

## Konfiguration

| Parameter         | Wert                                           |
|-------------------|------------------------------------------------|
| Algorithmus       | Feedforward Neural Network (Dense)             |
| Hidden Units      | 256 (je Hidden Layer)                          |
| Hidden Layers     | 2                                              |
| Dropout-Rate      | 0.3                                            |
| Aktivierung       | ReLU (Hidden), Softmax (Output)                |
| Optimierer        | Adam                                           |
| Lernrate          | 0.001                                          |
| Verlustfunktion   | Sparse Categorical Crossentropy                |
| Batch-Größe       | 128                                            |
| Epochen (trainiert) | 4 (Early Stopping)                           |
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
| Validation Accuracy | 0.7196 |
| Test Accuracy       | 0.7304 |

## Artefakte

- Modell: `results/neural/models/neural_model.keras`
- Vektorisierer: `results/neural/models/neural_vectorizer.pkl`
- Metriken (JSON): `results/neural/metrics/neural_metrics.json`
- Metriken (CSV): `results/neural/metrics/neural_results.csv`
- Confusion Matrix: `results/neural/figures/confusion_matrix_neural.png`
