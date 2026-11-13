#!/usr/bin/env python3
"""Check structure and SHA-256 of the S6E11 CSV without claiming model authorship."""
import csv
import hashlib
import math
import sys
from pathlib import Path

def main(filename: str) -> None:
    path = Path(filename)
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    n = 0
    previous = None
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["id", "is_fraud"], reader.fieldnames
        for row in reader:
            identifier = int(row["id"])
            probability = float(row["is_fraud"])
            assert math.isfinite(probability) and 0 <= probability <= 1
            if previous is not None:
                assert identifier == previous + 1
            previous = identifier
            if n == 0:
                assert identifier == 699960
            n += 1
    assert n == 299984, n
    assert previous == 999943, previous
    print("Rows:", n)
    print("CSV SHA-256:", digest.hexdigest())
    print("Structure: valid")
    print("Note: this does not verify leaderboard score or model authorship.")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "submission.csv")
