# Module 11 data: GSE199911

## Source

- **GEO:** [GSE199911](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE199911)
- **Paper:** Parker et al. (2023), *Frontiers in Cellular and Infection Microbiology* (PubMed [37077524](https://pubmed.ncbi.nlm.nih.gov/37077524/))
- **Design:** 29 people about one month into acute HIV-1 infection and 46 contemporaneous uninfected controls (PBMC RNA-seq)

## What we ship

| File | Contents |
| --- | --- |
| `gse199911_samples.csv` | One row per sample: `sample_id`, `group` (`hiv` / `control`), `sex`, `age` |
| `gse199911_tpm.csv.gz` | Gene symbols × samples, TPM |
| `gse199911_log2tpm.csv.gz` | Same matrix after `log2(TPM + 1)`, genes with TPM > 1 in at least 10 samples |
| `gse199911_de_results.csv` | Per-gene `log2fc` (HIV − control), Welch `t`, `p`, Benjamini–Hochberg `fdr` |

Rebuild with:

```bash
python prepare_gse199911.py
```

## Processing notes

NCBI’s browser download for precomputed TPM matrices is behind a reCAPTCHA wall, so the prep script uses the **submitter gene-count matrix** on GEO FTP (`GSE199911_processeddata_genecounts.csv.gz`) and converts counts to TPM.

1. Strip Ensembl version suffixes (`ENSG….10` → `ENSG…`).
2. Map Ensembl IDs to gene symbols with Ensembl BioMart (cached as `_ensembl_gene_annot.tsv`).
3. Approximate gene length as the genomic span (`end − start + 1`). This is not exon-sum effective length; it is good enough for a teaching contrast on log2 scale.
4. Compute TPM within each sample.
5. If two Ensembl IDs share a symbol, keep the ID with the **higher mean TPM**.
6. Differential expression uses genes with TPM > 1 in ≥ 10 samples, `log2(TPM + 1)`, drop the bottom 20% of genes by variance across samples, then a Welch two-sample t-test and BH-FDR.

These TPMs are **not** NCBI’s pipeline TPMs and may not match the authors’ published count-based DE results gene-for-gene. They are staged so students can practice log scaling, multiple testing, and Enrichr without fighting GEO downloads.

## Counts after staging

Re-check by re-running the prep script. At last build: 75 samples (29 HIV, 46 control), ~13k genes in the filtered log2 matrix (abundance + variance filters), thousands of genes with FDR < 0.05 (large acute-HIV signature).
