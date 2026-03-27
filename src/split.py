import json
from pathlib import Path
from typing import Tuple, List, Dict

INPUT_FILES = {
    "Movies & TV": "data/raw/Movies_and_TV.jsonl",
    "All Beauty": "data/raw/All_Beauty.jsonl",
    "Office Products": "data/raw/Office_Products.jsonl",
    "Books": "data/raw/Books.jsonl"
}

N_RECORDS_PER_FILE = 1250000
SPLIT_RATIOS = (0.7, 0.15, 0.15)
OUTPUT_DIR = "data/splits"
BUFFER_PERCENT = 1.01


def load_jsonl(filepath: str, max_records: int) -> List[Dict]:
    data = []
    target_with_buffer = int(max_records * BUFFER_PERCENT)

    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if len(data) >= target_with_buffer:
                break
            try:
                record = json.loads(line)
                if record.get('rating') in [1, 2, 3, 4, 5]:
                    data.append(record)
            except json.JSONDecodeError:
                print(f"JSON-Fehler in Zeile {i}: {line[:100]}")

    data = data[:max_records]
    print(f"  Geladen und gefiltert: {len(data)} Datensätze")
    return data


def split_data(
        data: List[Dict],
        ratios: Tuple[float, float, float]
) -> Tuple[List[Dict], List[Dict], List[Dict]]:
    assert abs(sum(ratios) - 1.0) < 1e-9

    n = len(data)
    train_size = int(n * ratios[0])
    val_size = int(n * ratios[1])

    train = data[:train_size]
    val = data[train_size:train_size + val_size]
    test = data[train_size + val_size:]

    return train, val, test


def save_jsonl(data: List[Dict], filepath: str):
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")
    print(f"  Gespeichert: {filepath} ({len(data)} Zeilen)")


def main():
    ratio_str = f"{int(SPLIT_RATIOS[0] * 100)}_{int(SPLIT_RATIOS[1] * 100)}_{int(SPLIT_RATIOS[2] * 100)}"

    all_train: List[Dict] = []
    all_val: List[Dict] = []
    all_test: List[Dict] = []

    total_target = N_RECORDS_PER_FILE * len(INPUT_FILES)

    for category_name, filepath in INPUT_FILES.items():

        current_total = len(all_train) + len(all_val) + len(all_test)
        if current_total >= total_target:
            print(f"\nZieldatenmenge erreicht. Beende Verarbeitung.")
            break

        print(f"\n{'=' * 60}")
        print(f"Verarbeite: {category_name}")
        print(f"{'=' * 60}")

        data = load_jsonl(filepath, N_RECORDS_PER_FILE)

        train, val, test = split_data(data, SPLIT_RATIOS)

        print(f"  Split – Train: {len(train):,}  Val: {len(val):,}  Test: {len(test):,}")

        all_train.extend(train)
        all_val.extend(val)
        all_test.extend(test)

        current_total = len(all_train) + len(all_val) + len(all_test)
        print(f"  Kumulativ: {current_total:,} / {total_target:,}")

    print(f"\n{'=' * 60}")
    print("GESAMT")
    print(f"{'=' * 60}")
    print(f"Train: {len(all_train):,}")
    print(f"Val:   {len(all_val):,}")
    print(f"Test:  {len(all_test):,}")
    print(f"Total: {len(all_train) + len(all_val) + len(all_test):,} (Ziel: {total_target:,})")

    train_file = f"{OUTPUT_DIR}/train_0_{N_RECORDS_PER_FILE}_{ratio_str}.jsonl"
    val_file = f"{OUTPUT_DIR}/val_0_{N_RECORDS_PER_FILE}_{ratio_str}.jsonl"
    test_file = f"{OUTPUT_DIR}/test_0_{N_RECORDS_PER_FILE}_{ratio_str}.jsonl"

    save_jsonl(all_train, train_file)
    save_jsonl(all_val, val_file)
    save_jsonl(all_test, test_file)


if __name__ == "__main__":
    main()