# What is a TPM?

**TPM** means *transcripts per million* (for bulk RNA-seq you can read it as “length-normalized abundance scaled to one million”).

## Why not raw counts?

Longer genes and deeper libraries collect more reads even when the biological concentration is the same. TPM adjusts for:

1. **Gene length** — divide by length (in kilobases) so long genes are not automatically “higher.”
2. **Sequencing depth** — scale each sample so the abundances sum to one million.

After that, a TPM of 10 in sample A and a TPM of 10 in sample B are on a comparable relative scale *within* typical bulk RNA-seq experiments. They are still not absolute molecules per cell.

## Why `log2(TPM + 1)`?

TPM values are skewed: many genes sit near zero, a few are huge. Taking `log2(TPM + 1)`:

- Compresses the dynamic range
- Makes differences closer to fold changes (a difference of 1 on the log2 scale is a 2-fold change)
- Softens zeros with the `+ 1` pseudocount

Module 11 runs the gene-wise t-test on that log scale. The mean difference between HIV and control is reported as **log2 fold change**.

