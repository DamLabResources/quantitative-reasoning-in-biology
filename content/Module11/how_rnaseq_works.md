# How RNA-seq works

RNA sequencing (RNA-seq) measures how much of each gene’s RNA is present in a sample. For this course you never touch raw FASTQ files. You start from a **gene-by-sample matrix** that someone else already quantified.

## This week’s study (GSE199911)

[Parker et al. (2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10106835/) sequenced PBMCs from people about one month into acute HIV-1 infection and from contemporaneous uninfected controls recruited in the same setting ([GSE199911](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE199911)). The staged course files keep **29 HIV** and **46 control** samples. The scientific claim in the paper is a large early host response (cell cycle, DNA repair, immune activation). Your job is to recover a similar story with a transparent teaching pipeline: log2 TPM, Welch t-tests, Benjamini–Hochberg FDR, then Enrichr.

## From cells to a matrix

1. **Isolate RNA** from a biological sample (here, peripheral blood mononuclear cells, PBMCs).
2. **Make a sequencing library**: convert RNA to complementary DNA (cDNA), fragment it, and add adapters.
3. **Sequence** millions of short reads on an Illumina instrument.
4. **Align or pseudo-align** those reads to a reference transcriptome or genome.
5. **Count** how many reads (or fragments) map to each gene in each sample.

The product is a table: rows are genes, columns are samples, and values are abundances. That table is what Module 11 analyzes.

## What is a TPM?

**TPM** means *transcripts per million* (for bulk RNA-seq you can read it as “length-normalized abundance scaled to one million”).

Longer genes and deeper libraries collect more reads even when the biological concentration is the same. TPM adjusts for:

1. **Gene length** — divide by length (in kilobases) so long genes are not automatically “higher.”
2. **Sequencing depth** — scale each sample so the abundances sum to one million.

After that, a TPM of 10 in sample A and a TPM of 10 in sample B are on a comparable relative scale *within* typical bulk RNA-seq experiments. They are still not absolute molecules per cell.

### Why `log2(TPM + 1)`?

TPM values are skewed: many genes sit near zero, a few are huge. Taking `log2(TPM + 1)`:

- Compresses the dynamic range
- Makes differences closer to fold changes (a difference of 1 on the log2 scale is a 2-fold change)
- Softens zeros with the `+ 1` pseudocount

## Differential expression across sample groups

**Differential expression (DE)** asks, gene by gene: does abundance differ between groups of samples (here, acute HIV vs uninfected controls)? You get an effect size (fold change or log2 fold change) and a p-value per gene, then adjust for testing thousands of genes at once.

### What you will do this week

A **Welch two-sample t-test** on `log2(TPM + 1)` for each gene, followed by Benjamini–Hochberg FDR. That keeps the pipeline simple. 

### What production RNA-seq DE usually looks like

Published analyses usually start from **integer counts** (not TPM) and use models built for over-dispersed count data, often with covariates (batch, sex, age) in the design:

- **Negative-binomial GLMs** — [DESeq2](https://bioconductor.org/packages/DESeq2/) and [edgeR](https://bioconductor.org/packages/edgeR/) estimate a mean–variance relationship per gene (or shared across genes) and test coefficients in a generalized linear model.
- **Linear models on variance-stabilized or voom-weighted data** — [limma](https://bioconductor.org/packages/limma/) (often with [voom](https://bioconductor.org/packages/release/bioc/vignettes/limma/inst/doc/usersguide.pdf)) fits a gene-wise linear model and borrows strength for variance estimation across genes (empirical Bayes).
- **Resampling** — permutation or bootstrap of sample labels (or residuals) can build an empirical null when parametric assumptions worry you; they are slower at genome scale and less common as the primary DE engine than DESeq2/edgeR/limma, but they appear in robustness checks and some specialized designs.

Those tools shine when library sizes differ, many genes are near zero, and you need a design matrix—not only a two-group mean difference. For Module 11, the Welch + FDR path is enough to learn the biostatistics story: effect size, multiple testing, then gene-set summarization with Enrichr.



