import json
from pathlib import Path
from datetime import datetime

INPUT_FILES = {
    "Movies & TV": "data/raw/Movies_and_TV.jsonl",
    "All Beauty": "data/raw/All_Beauty.jsonl",
    "Office Products": "data/raw/Office_Products.jsonl"
}

N_RECORDS_PER_FILE = 30000000
SPLIT_RATIOS = (0.7, 0.15, 0.15)
OUTPUT_DIR = "data/splits"
BUFFER_PERCENT = 1.01
PROJECT_ROOT = Path(".")


def count_valid(filepath, max_records):
    target_with_buffer = int(max_records * BUFFER_PERCENT)
    count = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if count >= target_with_buffer:
                break
            try:
                record = json.loads(line)
                if record.get('rating') in [1, 2, 3, 4, 5]:
                    count += 1
            except json.JSONDecodeError:
                continue
    return min(count, max_records)


def split_and_write(filepath, max_records, train_f, val_f, test_f):
    target_with_buffer = int(max_records * BUFFER_PERCENT)
    valid_count = 0
    train_size = int(max_records * SPLIT_RATIOS[0])
    val_size = int(max_records * SPLIT_RATIOS[1])
    counts = {'train': 0, 'val': 0, 'test': 0}

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if valid_count >= max_records:
                break
            try:
                record = json.loads(line)
                if record.get('rating') not in [1, 2, 3, 4, 5]:
                    continue
            except json.JSONDecodeError:
                continue

            json_line = json.dumps(record) + "\n"

            if valid_count < train_size:
                train_f.write(json_line)
                counts['train'] += 1
            elif valid_count < train_size + val_size:
                val_f.write(json_line)
                counts['val'] += 1
            else:
                test_f.write(json_line)
                counts['test'] += 1

            valid_count += 1

            if valid_count % 5_000_000 == 0:
                print(f"    {valid_count:,} Records geschrieben... {datetime.now().strftime('%H:%M:%S')}")

    return counts


def main():
    ratio_str = f"{int(SPLIT_RATIOS[0] * 100)}_{int(SPLIT_RATIOS[1] * 100)}_{int(SPLIT_RATIOS[2] * 100)}"

    output_dir = PROJECT_ROOT / OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    train_path = output_dir / f"train_nobooks_{N_RECORDS_PER_FILE}_{ratio_str}.jsonl"
    val_path = output_dir / f"val_nobooks_{N_RECORDS_PER_FILE}_{ratio_str}.jsonl"
    test_path = output_dir / f"test_nobooks_{N_RECORDS_PER_FILE}_{ratio_str}.jsonl"

    total_train = 0
    total_val = 0
    total_test = 0

    with open(train_path, "w", encoding="utf-8") as train_f, \
         open(val_path, "w", encoding="utf-8") as val_f, \
         open(test_path, "w", encoding="utf-8") as test_f:

        for category_name, filepath in INPUT_FILES.items():
            full_path = PROJECT_ROOT / filepath

            print(f"\n{'='*60}")
            print(f"Verarbeite: {category_name}")
            print(f"{'='*60}")

            print(f"  Durchlauf 1: Zaehle valide Records...")
            valid_total = count_valid(full_path, N_RECORDS_PER_FILE)
            print(f"  Valide Records: {valid_total:,}")

            train_size = int(valid_total * SPLIT_RATIOS[0])
            val_size = int(valid_total * SPLIT_RATIOS[1])
            test_size = valid_total - train_size - val_size
            print(f"  Geplanter Split: Train={train_size:,} Val={val_size:,} Test={test_size:,}")

            print(f"  Durchlauf 2: Schreibe Splits...")
            counts = split_and_write(full_path, valid_total, train_f, val_f, test_f)
            print(f"  Geschrieben: Train={counts['train']:,} Val={counts['val']:,} Test={counts['test']:,}")

            total_train += counts['train']
            total_val += counts['val']
            total_test += counts['test']

    total = total_train + total_val + total_test
    print(f"\n{'='*60}")
    print("GESAMT")
    print(f"{'='*60}")
    print(f"Train: {total_train:,}")
    print(f"Val:   {total_val:,}")
    print(f"Test:  {total_test:,}")
    print(f"Total: {total:,}")
    print("\nDateien:")
    print(f"  {train_path}")
    print(f"  {val_path}")
    print(f"  {test_path}")


if __name__ == "__main__":
    main()