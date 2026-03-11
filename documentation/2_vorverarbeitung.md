# Phase 2: Vorverarbeitung

## EDA

EDA-Report per `src/raw_data_analysis.py` erstellt: documentation/phase1_eda_report.md

Analysiert wurden bis zu 5.000.000 Datensätze je Kategorie:

| Kategorie       | Datensätze | Ø Textlänge (Zeichen) | Ø Wörter |
|-----------------|------------|----------------------|----------|
| Movies & TV     | 5.000.000  | 264                  | 47       |
| All Beauty      | 701.528    | 173                  | 33       |
| Office Products | 5.000.000  | 183                  | 34       |
| Books           | 5.000.000  | 434                  | 77       |

## Split-Script

Split-Script `src/split.py` lässt sich über folgende Parameter konfigurieren:

- `N_RECORDS_PER_FILE`: Anzahl der Datensätze pro Kategorie
- `SPLIT_RATIOS`: Verhältnis Train / Validation / Test
- `INPUT_FILES`: Pfade zu den Rohdaten
- `OUTPUT_DIR`: Ausgabeverzeichnis (`data/splits/`)

Namenskonvetion der Splitdateien: `{split}_0_{n}_{ratio}.jsonl`, z. B. `train_0_50000_80_0_20.jsonl`.

## Erzeugte Splits

### Naive Bayes: 80/0/20

| Split | Datensätze |
|-------|------------|
| Train | 160.000    |
| Test  | 40.000     |

### SVM / Logistic Regression / Neural Network: 70/15/15

| Split      | Datensätze |
|------------|------------|
| Train      | 140.000    |
| Validation | 30.000     |
| Test       | 30.000     |
