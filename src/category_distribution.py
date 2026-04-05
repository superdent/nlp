from pathlib import Path
from collections import Counter
import gc

PROJECT_ROOT = Path(".")
SPLITS_DIR = PROJECT_ROOT / "data" / "splits"

files = sorted(SPLITS_DIR.glob("*.jsonl"))

for filepath in files:
    counts = Counter()
    total = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            # rating steht am Anfang: {"rating": 3.0, ...
            pos = line.find('"rating":')
            if pos == -1:
                continue
            start = pos + 10
            end = line.index(",", start)
            rating = int(float(line[start:end].strip()))
            counts[rating] += 1
            total += 1

    print(f"\n{filepath.name}  (n={total:,})")
    for star in sorted(counts.keys()):
        pct = counts[star] / total * 100
        print(f"  {star} Stern: {counts[star]:>10,}  ({pct:5.1f}%)")

    del counts
    gc.collect()