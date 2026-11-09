#!/usr/bin/env python3
"""Download and stage the Depresjon actigraphy dataset for Module 12.

Writes depresjon_minute.csv.gz with one row per person-minute after trimming
each file to the first `days` listed in scores.csv (the paper analysis window).
"""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import pandas as pd
import urllib.request

OUTDIR = Path(__file__).resolve().parent
ZIP_URL = "https://zenodo.org/records/1219550/files/depresjon-dataset.zip?download=1"


def download(url: str) -> bytes:
    print(f"Downloading {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "Module12-prep/1.0"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        return resp.read()


def main() -> None:
    raw = download(ZIP_URL)
    zf = zipfile.ZipFile(io.BytesIO(raw))
    names = zf.namelist()
    print(f"zip entries: {len(names)}")

    # Locate scores.csv and condition/control folders across possible nestings
    score_name = next(n for n in names if n.endswith("scores.csv") and not n.endswith("/"))
    scores = pd.read_csv(zf.open(score_name))
    scores["number"] = scores["number"].astype(str)
    days_map = scores.set_index("number")["days"].to_dict()
    print(f"scores rows: {len(scores)}")

    rows = []
    for name in names:
        if not name.endswith(".csv"):
            continue
        if name.endswith("scores.csv"):
            continue
        lower = name.lower()
        if "/condition/" in lower or lower.startswith("condition/"):
            group = "condition"
        elif "/control/" in lower or lower.startswith("control/"):
            group = "control"
        else:
            continue
        person_id = Path(name).stem  # e.g. condition_1 or control_1
        # Match scores number field: files are often named condition_1.csv
        key = person_id
        # scores uses number like "condition_1" or sometimes just numeric — try both
        if key not in days_map:
            # try without prefix
            alt = person_id.split("_")[-1]
            if person_id in days_map:
                pass
            elif f"{group}_{alt}" in days_map:
                key = f"{group}_{alt}"
            else:
                # scores 'number' column may already equal the filename stem
                key = person_id

        df = pd.read_csv(zf.open(name))
        # expected columns: timestamp, date, activity
        df.columns = [c.strip().lower() for c in df.columns]
        if "activity" not in df.columns:
            raise RuntimeError(f"No activity column in {name}: {df.columns.tolist()}")

        n_days = days_map.get(key)
        if n_days is None:
            # fuzzy: scores number might be "1" with separate folders
            num = person_id.split("_")[-1]
            # scores often stores number as condition_1 / control_1
            candidates = [k for k in days_map if k.endswith(f"_{num}") or k == num]
            if len(candidates) == 1:
                key = candidates[0]
                n_days = days_map[key]
            else:
                raise RuntimeError(f"No days entry for {person_id} / {key}")

        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")
        start = df["timestamp"].iloc[0]
        end = start + pd.Timedelta(days=float(n_days))
        df = df.loc[df["timestamp"] < end].copy()

        df["person_id"] = person_id
        df["group"] = group
        # attach score fields for this person
        score_row = scores.loc[scores["number"] == key]
        if score_row.empty:
            # try match on stem equality already used
            score_row = scores.loc[scores["number"].astype(str) == str(key)]
        if not score_row.empty:
            for col in scores.columns:
                if col == "number":
                    continue
                df[col] = score_row.iloc[0][col]
        rows.append(df)

    out = pd.concat(rows, ignore_index=True)
    # tidy column order
    front = ["person_id", "group", "timestamp", "date", "activity"]
    other = [c for c in out.columns if c not in front]
    out = out[front + other]

    path = OUTDIR / "depresjon_minute.csv.gz"
    out.to_csv(path, index=False, compression="gzip")
    n_people = out["person_id"].nunique()
    print(f"Wrote {path}")
    print(f"people={n_people} minutes={len(out)}")
    print(out["group"].value_counts())
    print("Done.")


if __name__ == "__main__":
    main()
