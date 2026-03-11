# Phase 3: Modelltraining – Naive Bayes

## Konfiguration

| Parameter       | Wert                                      |
|-----------------|-------------------------------------------|
| Algorithmus     | MultinomialNB                             |
| Alpha           | 1.0 (Laplace-Smoothing)                   |
| Vektorisierung  | TF-IDF                                    |
| Max. Features   | 5.000                                     |
| min_df          | 2                                         |
| max_df          | 0.95                                      |
| Stoppwörter     | Englisch                                  |
| Input           | Titel + Text (kombiniert)                 |
| Trainingsdaten  | `train_0_50000_80_0_20.jsonl` (160.000)   |
| Testdaten       | `test_0_50000_80_0_20.jsonl` (40.000)     |

## Ergebnisse

| Metrik   | Wert     |
|----------|----------|
| Accuracy | 0.605875 |

## Artefakte

- Modell: `results/models/naive_bayes_model.pkl`
- Vektorisierer: `results/models/vectorizer.pkl`
- Metriken (JSON): `results/metrics/naive_bayes_metrics.json`
- Metriken (CSV): `results/metrics/naive_bayes_results.csv`
