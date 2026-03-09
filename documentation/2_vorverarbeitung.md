# Phase 2: Vorverarbeitung

## EDA

Der EDA-Report wurde mit `src/raw_data_analysis.py` erstellt und ist unter `documentation/phase1_eda_report.md` abgelegt.

Analysiert wurden je bis zu 5.000.000 Datensätze pro Kategorie:

| Kategorie       | Datensätze | Ø Textlänge (Zeichen) | Ø Wörter |
|-----------------|------------|----------------------|----------|
| Movies & TV     | 5.000.000  | 264                  | 47       |
| All Beauty      | 701.528    | 173                  | 33       |
| Office Products | 5.000.000  | 183                  | 34       |
| Books           | 5.000.000  | 434                  | 77       |

## Split-Script

Das Split-Script `src/split.py` ist konfigurierbar über folgende Parameter:

- `N_RECORDS_PER_FILE`: Anzahl der Datensätze pro Kategorie
- `SPLIT_RATIOS`: Verhältnis Train / Validation / Test
- `INPUT_FILES`: Pfade zu den Rohdaten
- `OUTPUT_DIR`: Ausgabeverzeichnis (`data/splits/`)

Die erzeugten Dateien werden nach dem Schema `{split}_0_{n}_{ratio}.jsonl` benannt, z.B. `train_0_50000_80_0_20.jsonl`.

## Erzeugte Splits

### Naive Bayes: 80/0/20

| Split | Datensätze |
|-------|------------|
| Train | 160.000    |
| Test  | 40.000     |

Dateien:
- `data/splits/train_0_50000_80_0_20.jsonl`
- `data/splits/test_0_50000_80_0_20.jsonl`

### SVM / Logistic Regression / Neural Network: 70/15/15

| Split      | Datensätze |
|------------|------------|
| Train      | <!-- TODO: Wert eintragen --> |
| Validation | <!-- TODO: Wert eintragen --> |
| Test       | <!-- TODO: Wert eintragen --> |

Dateien:
- `data/splits/train_0_50000_70_15_15.jsonl`
- `data/splits/val_0_50000_70_15_15.jsonl`
- `data/splits/test_0_50000_70_15_15.jsonl`
