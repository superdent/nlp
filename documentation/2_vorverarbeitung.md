# Phase 2: Vorverarbeitung

## EDA

EDA-Report per `src/raw_data_analysis.py` erstellt: documentation/2_eda_result.md

Analysiert wurden alle Datensätze je Kategorie (kein Limit):

| Kategorie       | Datensätze | Ø Textlänge (Zeichen) | Ø Wörter |
|-----------------|------------|----------------------|----------|
| Movies & TV     | 17.328.314 | 237                  | 42       |
| All Beauty      | 701.528    | 173                  | 33       |
| Office Products | 12.845.712 | 175                  | 33       |

Ungültige Ratings: 1 (Office Products). Keine JSON-Fehler, keine fehlenden Werte.

## Split-Script

Split-Script `src/split.py` lässt sich über folgende Parameter konfigurieren:

- `N_RECORDS_PER_FILE`: Anzahl der Datensätze pro Kategorie
- `SPLIT_RATIOS`: Verhältnis Train / Validation / Test
- `INPUT_FILES`: Pfade zu den Rohdaten
- `OUTPUT_DIR`: Ausgabeverzeichnis (`data/splits/`)

Namenskonvention der Splitdateien: `{split}_0_{n}_{ratio}.jsonl`, z. B. `train_0_100000_70_15_15.jsonl`.

All Beauty enthält nur 701.528 valide Records. Bei N_RECORDS_PER_FILE > 701.528 wird die Kategorie vollständig verwendet.

## Erzeugte Splits

### 100.000 pro Kategorie

| Split      | 70/15/15   | 80/0/20   |
|------------|------------|-----------|
| Train      | 210.000    | 240.000   |
| Validation | 45.000     | —         |
| Test       | 45.000     | 60.000    |

### 2.000.000 pro Kategorie (Beauty: 701.528)

| Split      | 70/15/15     | 80/0/20      |
|------------|-------------|-------------|
| Train      | 3.291.069   | 3.761.222   |
| Validation | 705.229     | —           |
| Test       | 705.230     | 940.306     |

### 30.000.000 pro Kategorie (alle Datensätze)

| Split      | 70/15/15      | 80/0/20       |
|------------|--------------|--------------|
| Train      | 21.612.885   | 24.700.442   |
| Validation | 4.631.332    | —            |
| Test       | 4.631.336    | 6.175.111    |