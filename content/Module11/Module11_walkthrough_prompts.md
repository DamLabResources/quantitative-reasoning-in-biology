# Module 11 walkthrough prompts

Companion to the [Module 11 walkthrough](Module11_walkthrough.ipynb). Use each **Point** to write your own Colab cell-level AI prompt. Run the generated code and check the printed objects before the next step. Open the hint only if you want a short sample prompt.

## Setup

The notebook already installs `applied-biostats-helper` and `gseapy==1.3.2` and imports numpy, pandas, seaborn, matplotlib, scipy.stats, statsmodels BH correction, and gseapy. Do not ask the AI to reinstall those unless an import fails.

---

## Step 1. Load the staged tables

**Point:** Load `gse199911_samples.csv` into `samples` and `gse199911_tpm.csv.gz` into `tpm`. Confirm the design at the **sample** level (PBMC RNA-seq): print `n` samples, `samples['group'].value_counts()`, and `tpm.shape`, then show `tpm.head()`.

<details><summary>Hint</summary>

> Load `samples` and `tpm` from the staged CSVs. Print n, group counts, shape, and `tpm.head()`.

</details>

---

## Step 2. Abundance filter

**Point:** From `tpm`, set gene symbols as the index and keep only columns in `samples['sample_id']`. Keep genes with **TPM > 1 in at least 10 samples**. Store the filtered matrix as `expr_f`. Print gene counts before and after, then `expr_f.head()`.

<details><summary>Hint</summary>

> Index by gene, align to sample IDs, keep genes with TPM > 1 in ≥10 samples as `expr_f`, and print before/after n genes.

</details>

---

## Step 3. Are TPM values normally distributed?

**Point:** On `expr_f`, pick about **five mid-abundance** genes (near one-third of the way down a mean-TPM ranking). For each, run Shapiro–Wilk across samples and print W and p. Histogram the first probe gene with a KDE. Expect clear skew on the raw TPM scale.

<details><summary>Hint</summary>

> Shapiro–Wilk five mid-abundance genes in `expr_f`; histogram the first with KDE.

</details>

---

## Step 4. Log2 transform

**Point:** Create `log2` as **`log2(TPM + 1)`** from `expr_f`. Print shape and `log2.head()`.

<details><summary>Hint</summary>

> Set `log2 = log2(expr_f + 1)`; print shape and head.

</details>

---

## Step 5. Retest normality on the log2 scale

**Point:** Using the **same probe genes** as Step 3, run Shapiro–Wilk on `log2` and print W and p. Histogram the first probe gene on the log2 scale with a KDE. It should look closer to normal than raw TPM, even if not perfect.

<details><summary>Hint</summary>

> Repeat Shapiro–Wilk and the histogram on `log2` for the same probe genes.

</details>

---

## Step 6. Variance filter

**Point:** On `log2`, compute per-gene variance across samples. Drop genes in the **bottom 20%** of variance. Overwrite `log2` with the kept genes. Print the variance cutoff and the number of genes remaining.

<details><summary>Hint</summary>

> Drop the bottom 20% variance genes from `log2`; print cutoff and n remaining.

</details>

---

## Step 7. Gene-wise log2 fold change

**Point:** From `samples`, get `sample_id` lists for **`hiv`** and **`control`**. For each gene in `log2`, compute HIV mean minus control mean. Store the Series as `log2fc`. Print how many genes have a fold change and show the top of `log2fc` sorted descending.

<details><summary>Hint</summary>

> Build `log2fc` as HIV − control means on `log2`; show the top sorted values.

</details>

---

## Step 8. Gene-wise Welch t-test

**Point:** Using the HIV and control columns of `log2`, run a **vectorized** Welch t-test with `scipy.stats.ttest_ind(..., equal_var=False)` along genes (avoid pingouin loops). Store `t_stat` and `p_val`. Print the number of p-values and how many raw p-values are **&lt; 0.05**.

<details><summary>Hint</summary>

> Vectorized Welch `ttest_ind` on `log2` → `t_stat`, `p_val`; count raw p &lt; 0.05.

</details>

---

## Step 9. Benjamini–Hochberg FDR

**Point:** Adjust `p_val` with Benjamini–Hochberg via `statsmodels.stats.multitest.multipletests`. Build DataFrame `results` with columns `gene_symbol`, `log2fc`, `t`, `p`, and `fdr`, sorted by `fdr`. Print how many genes have **FDR &lt; 0.05** and show `results.head(10)`.

<details><summary>Hint</summary>

> BH-adjust `p_val` into `results` (`gene_symbol`, `log2fc`, `t`, `p`, `fdr`); count FDR &lt; 0.05.

</details>

---

## Step 10. Build the Enrichr input list

**Point:** From `results`, make list `sig` of gene symbols with **FDR &lt; 0.05** and **|log2FC| &gt; 1**. Print `len(sig)` and the first 10 symbols.

<details><summary>Hint</summary>

> Make `sig` from FDR &lt; 0.05 and |log2FC| &gt; 1; print length and first 10.

</details>

---

## Step 11. Enrichr (Hallmark)

**Point:** Run `gseapy.enrichr` on `sig` with gene set library **`MSigDB_Hallmark_2020`**, organism **`Human`**, and **`outdir=None`**. Store the table as `enrich_df` sorted by adjusted p-value and show the top 10 rows.

<details><summary>Hint</summary>

> `gseapy.enrichr` on `sig` with Hallmark 2020 → `enrich_df`; show top 10 by adj-p.

</details>
