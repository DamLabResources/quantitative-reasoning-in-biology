# Module 11 walkthrough prompts

Companion to the [Module 11 walkthrough](Module11_walkthrough.ipynb). Use these as Colab cell-level AI prompts, one step at a time. Run the generated code and check the printed objects before the next prompt.

## Setup

The notebook already installs `applied-biostats-helper` and `gseapy==1.3.2` and imports numpy, pandas, seaborn, matplotlib, scipy.stats, statsmodels BH correction, and gseapy. Do not ask the AI to reinstall those unless an import fails.

---

## Step 1. Load the staged tables

**Point:** Get the expression matrix and sample sheet into named objects, and confirm the HIV vs control design (n per group).

**Sample prompt:**

> Load `gse199911_samples.csv` into `samples` and `gse199911_tpm.csv.gz` into `tpm`. Print the unit of analysis as sample-level PBMC RNA-seq, the number of samples, the value counts of `group`, and the shape of `tpm`. Show `tpm.head()`.

---

## Step 2. Abundance filter

**Point:** Remove genes that are essentially off in most samples so later tests are not dominated by near-zero noise.

**Sample prompt:**

> From `tpm`, set the gene symbol as the index and keep only the sample columns listed in `samples['sample_id']`. Keep genes with TPM greater than 1 in at least 10 samples. Store the filtered matrix as `expr_f`. Print the number of genes before and after filtering and show `expr_f.head()`.

---

## Step 3. Are TPM values normally distributed?

**Point:** See that raw TPM is skewed—motivation for a log transform before t-tests.

**Sample prompt:**

> Using `expr_f`, pick about five mid-abundance genes (near one-third of the way down a mean-TPM ranking). For each gene, run a Shapiro–Wilk test on the TPM values across samples and print W and p. Histogram the first of those genes with a KDE. Expect clear skew, not normality.

---

## Step 4. Log2 transform

**Point:** Put abundances on a fold-change-friendly scale for group means and t-tests.

**Sample prompt:**

> Create `log2` as `log2(TPM + 1)` from `expr_f`. Print its shape and show `log2.head()`.

---

## Step 5. Retest normality on the log2 scale

**Point:** Check whether the log transform improved the shape for the same probe genes.

**Sample prompt:**

> Using the same probe genes as before, run Shapiro–Wilk on the `log2` values and print W and p. Histogram the first probe gene on the log2 scale with a KDE. Comment that it should look closer to normal, even if not perfect.

---

## Step 6. Variance filter

**Point:** Drop nearly constant genes that add tests without information.

**Sample prompt:**

> On `log2`, compute per-gene variance across samples. Drop genes in the bottom 20% of variance. Overwrite `log2` with the kept genes. Print the variance cutoff and the number of genes remaining.

---

## Step 7. Gene-wise log2 fold change

**Point:** Summarize direction and size of the HIV vs control difference per gene.

**Sample prompt:**

> From `samples`, get the `sample_id` lists for `hiv` and `control`. For each gene in `log2`, compute HIV mean minus control mean. Store the Series as `log2fc`. Print how many genes have a fold change and show the top of `log2fc` sorted descending.

---

## Step 8. Gene-wise Welch t-test

**Point:** Get a raw p-value for each gene without looping in pingouin (too slow at this size).

**Sample prompt:**

> Using the HIV and control sample columns of `log2`, run a vectorized Welch t-test with `scipy.stats.ttest_ind` (`equal_var=False`) along genes. Store `t_stat` and `p_val`. Print the number of p-values and how many raw p-values are less than 0.05.

---

## Step 9. Benjamini–Hochberg FDR

**Point:** Control the false-discovery rate across thousands of tests and assemble a results table.

**Sample prompt:**

> Adjust `p_val` with Benjamini–Hochberg via `statsmodels.stats.multitest.multipletests`. Build a DataFrame `results` with columns `gene_symbol`, `log2fc`, `t`, `p`, and `fdr`, sorted by `fdr`. Print how many genes have FDR less than 0.05 and show `results.head(10)`.

---

## Step 10. Build the Enrichr input list

**Point:** Choose a discovery list that is both statistically and practically filtered before pathway testing.

**Sample prompt:**

> From `results`, make a list `sig` of gene symbols with FDR less than 0.05 and absolute log2 fold change greater than 1. Print the length of `sig` and the first 10 symbols.

---

## Step 11. Enrichr (Hallmark)

**Point:** Ask whether the significant genes over-represent coherent Hallmark programs.

**Sample prompt:**

> Run `gseapy.enrichr` on `sig` with gene set library `MSigDB_Hallmark_2020`, organism `Human`, and `outdir=None`. Store the results table as `enrich_df` sorted by adjusted p-value and show the top 10 rows.
