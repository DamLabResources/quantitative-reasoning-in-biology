#!/usr/bin/env python3
"""Download and stage GSE199911 for Module 11.

NCBI's interactive rnaseq-counts download is reCAPTCHA-gated, so this script
uses the submitter gene-count matrix on GEO FTP and converts counts to TPM
with Ensembl gene lengths (median transcript length per gene).

Writes:
  - gse199911_samples.csv
  - gse199911_tpm.csv.gz
  - gse199911_log2tpm.csv.gz
  - gse199911_de_results.csv

Rules:
  - Map Ensembl gene IDs to symbols.
  - On duplicate symbols, keep the ID with the higher mean TPM.
  - Filter genes with TPM > 1 in at least 10 samples before DE.
  - Two-sample t-test (HIV vs control) on log2(TPM + 1); BH-FDR.
"""

from __future__ import annotations

import io
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

OUTDIR = Path(__file__).resolve().parent
ACC = "GSE199911"
MIN_SAMPLES_TPM_GT1 = 10
VARIANCE_QUANTILE_DROP = 0.20  # drop bottom 20% variance on log2 scale

COUNTS_URL = (
    f"https://ftp.ncbi.nlm.nih.gov/geo/series/GSE199nnn/{ACC}/suppl/"
    f"{ACC}_processeddata_genecounts.csv.gz"
)
SERIES_URL = (
    f"https://ftp.ncbi.nlm.nih.gov/geo/series/GSE199nnn/{ACC}/matrix/"
    f"{ACC}_series_matrix.txt.gz"
)
BIOMART_URL = "https://www.ensembl.org/biomart/martservice"


def download(url: str) -> bytes:
    print(f"Downloading {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "Module11-prep/1.0"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        return resp.read()


def fetch_ensembl_annot() -> pd.DataFrame:
    """Gene symbol + approximate length (gene span) from Ensembl BioMart.

    Uses a local cache file when present so prep can run offline after the
    first successful BioMart pull.
    """
    cache = OUTDIR / "_ensembl_gene_annot.tsv"
    if not cache.exists():
        print("Downloading Ensembl BioMart gene annotation")
        xml_span = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Query>
<Query virtualSchemaName="default" formatter="TSV" header="1" uniqueRows="1"
      count="" datasetConfigVersion="0.6">
  <Dataset name="hsapiens_gene_ensembl" interface="default">
    <Attribute name="ensembl_gene_id"/>
    <Attribute name="external_gene_name"/>
    <Attribute name="start_position"/>
    <Attribute name="end_position"/>
  </Dataset>
</Query>
"""
        url = BIOMART_URL + "?" + urllib.parse.urlencode({"query": xml_span})
        # curl follows Ensembl's 308 redirects more reliably than urllib.
        import subprocess

        subprocess.run(
            ["curl", "-fsSL", "--max-time", "300", "-o", str(cache), url],
            check=True,
        )
    else:
        print(f"Using cached Ensembl annotation: {cache.name}")

    annot = pd.read_csv(cache, sep="\t")
    annot = annot.rename(
        columns={
            "Gene stable ID": "ensembl_id",
            "Gene name": "gene_symbol",
            "Gene start (bp)": "start",
            "Gene end (bp)": "end",
        }
    )
    if "ensembl_id" not in annot.columns:
        # fall back when header names differ
        cols = list(annot.columns)
        rename = {cols[0]: "ensembl_id", cols[1]: "gene_symbol"}
        # start/end are the last two numeric position columns when biotype is present
        if "start" not in annot.columns:
            rename[cols[-2]] = "start"
            rename[cols[-1]] = "end"
        annot = annot.rename(columns=rename)
    annot["gene_symbol"] = annot["gene_symbol"].astype(str).str.strip()
    annot = annot[annot["gene_symbol"].ne("") & annot["gene_symbol"].ne("nan")]
    annot["start"] = pd.to_numeric(annot["start"], errors="coerce")
    annot["end"] = pd.to_numeric(annot["end"], errors="coerce")
    annot = annot.dropna(subset=["start", "end"])
    annot["length_bp"] = (annot["end"] - annot["start"] + 1).clip(lower=1.0)
    length = annot[["ensembl_id", "gene_symbol", "length_bp"]].drop_duplicates(
        subset=["ensembl_id"], keep="first"
    )
    print(f"Ensembl genes with length: {len(length)}")
    return length


def counts_to_tpm(counts: pd.DataFrame, length_bp: pd.Series) -> pd.DataFrame:
    """counts: genes x samples; length_bp indexed like counts.index."""
    rate = counts.div(length_bp / 1e3, axis=0)
    scale = rate.sum(axis=0) / 1e6
    return rate.div(scale, axis=1)


def main() -> None:
    counts_raw = download(COUNTS_URL)
    download(SERIES_URL)  # confirm series is reachable; sample table comes from counts file

    wide = pd.read_csv(io.BytesIO(counts_raw), compression="gzip", index_col=0)
    meta_cols = ["sample", "studygroup", "sex", "age"]
    samples = wide[meta_cols].copy()
    samples = samples.rename(columns={"sample": "sample_id"})
    samples["sample_id"] = samples["sample_id"].astype(str).str.strip().str.rstrip(".")
    # studygroup: 1 = acute HIV, 2 = uninfected control (A* vs N* sample IDs)
    samples["group"] = samples["studygroup"].map({1: "hiv", 2: "control"})
    if samples["group"].isna().any():
        raise RuntimeError("Unexpected studygroup values")
    samples = samples[["sample_id", "group", "sex", "age"]].reset_index(drop=True)

    n_hiv = int((samples["group"] == "hiv").sum())
    n_ctrl = int((samples["group"] == "control").sum())
    print(f"Samples: {n_hiv} hiv, {n_ctrl} control (expected 29 vs 46)")
    if n_hiv != 29 or n_ctrl != 46:
        raise RuntimeError(f"Unexpected design: {n_hiv} hiv / {n_ctrl} control")

    gene_cols = [c for c in wide.columns if c.startswith("ENSG")]
    counts = wide[gene_cols].copy()
    counts.index = samples["sample_id"].to_numpy()
    counts.columns = [c.split(".")[0] for c in counts.columns]  # strip version
    # genes x samples
    counts = counts.T.groupby(level=0).sum()
    counts = counts[samples["sample_id"]]

    annot = fetch_ensembl_annot()
    annot = annot.drop_duplicates(subset=["ensembl_id"], keep="first")
    merged = counts.join(annot.set_index("ensembl_id"), how="inner")
    length = merged["length_bp"]
    symbols = merged["gene_symbol"]
    counts_m = merged.drop(columns=["length_bp", "gene_symbol"])

    tpm = counts_to_tpm(counts_m, length)
    tpm["gene_symbol"] = symbols
    tpm["mean_tpm"] = tpm[samples["sample_id"]].mean(axis=1)
    tpm = tpm.sort_values("mean_tpm", ascending=False)
    tpm = tpm.drop_duplicates(subset=["gene_symbol"], keep="first")
    tpm = tpm.set_index("gene_symbol")
    expr = tpm[samples["sample_id"]]

    tpm_out = expr.reset_index()
    tpm_path = OUTDIR / "gse199911_tpm.csv.gz"
    tpm_out.to_csv(tpm_path, index=False, compression="gzip")
    print(f"Wrote {tpm_path} shape={tpm_out.shape}")

    samples_path = OUTDIR / "gse199911_samples.csv"
    samples.to_csv(samples_path, index=False)
    print(f"Wrote {samples_path} n={len(samples)}")

    keep = (expr > 1).sum(axis=1) >= MIN_SAMPLES_TPM_GT1
    log2 = np.log2(expr.loc[keep] + 1.0)
    gene_var = log2.var(axis=1)
    var_cut = float(gene_var.quantile(VARIANCE_QUANTILE_DROP))
    log2 = log2.loc[gene_var > var_cut]
    log2_path = OUTDIR / "gse199911_log2tpm.csv.gz"
    log2.reset_index().to_csv(log2_path, index=False, compression="gzip")
    print(
        f"Wrote {log2_path} genes={log2.shape[0]} "
        f"(TPM>1 in >={MIN_SAMPLES_TPM_GT1}; drop bottom "
        f"{int(VARIANCE_QUANTILE_DROP * 100)}% variance, cut={var_cut:.4g})"
    )

    hiv_cols = samples.loc[samples["group"] == "hiv", "sample_id"].tolist()
    ctrl_cols = samples.loc[samples["group"] == "control", "sample_id"].tolist()
    hiv = log2[hiv_cols].to_numpy()
    ctrl = log2[ctrl_cols].to_numpy()
    log2fc = hiv.mean(axis=1) - ctrl.mean(axis=1)
    t_stat, p_val = stats.ttest_ind(hiv, ctrl, axis=1, equal_var=False, nan_policy="omit")
    _, fdr, _, _ = multipletests(p_val, method="fdr_bh")

    de = pd.DataFrame(
        {
            "gene_symbol": log2.index,
            "log2fc": log2fc,
            "t": t_stat,
            "p": p_val,
            "fdr": fdr,
        }
    ).sort_values("fdr")
    de_path = OUTDIR / "gse199911_de_results.csv"
    de.to_csv(de_path, index=False)
    print(f"Wrote {de_path} genes={len(de)} fdr<0.05={int((de['fdr'] < 0.05).sum())}")
    print("Done.")


if __name__ == "__main__":
    main()
