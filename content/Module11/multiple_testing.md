# Multiple testing

A single hypothesis test at α = 0.05 expects a false positive about 5% of the time when the null is true. RNA-seq runs **thousands** of tests—one per gene. The family-wise error explodes unless you adjust.

## A numeric sketch

Suppose 20,000 genes are truly null (no expression difference) and you call anything with p < 0.05 “significant.”

- Expected false positives ≈ 20,000 × 0.05 = **1,000** genes
- That list is mostly noise

Real data mix null and non-null genes, but the same logic holds: unadjusted p-values overstate how special each hit is.

## Three policies you will see

### 1. No adjustment

Report raw p-values. Fine for one pre-planned test. Misleading as a genome-wide discovery list.

### 2. Bonferroni

For *m* tests, use threshold α / *m*, or multiply each p by *m* and cap at 1.

- Controls the **family-wise error rate** (probability of *any* false positive)
- Very conservative when *m* is ~20,000
- You will miss many real genes

### 3. Benjamini–Hochberg FDR

Controls the **false discovery rate**: among the genes you call significant, what fraction are expected to be false?

- Sort p-values ascending
- Find the largest *k* such that p₍ₖ₎ ≤ (k / m) × α
- Reject that gene and all more significant ones

BH is the default compromise in genomics discovery screens. Module 11 stores the BH-adjusted values in a column named `fdr`.

## How to read results

- **Raw p** answers: “If this single gene were the only test, how surprising is the difference?”
- **FDR** answers: “If I take the whole significant list at this cutoff, what fraction of that list is expected to be wrong?”

For Enrichr you will pass genes with FDR below a cutoff (and often a fold-change floor). That list is still imperfect; enrichment is a second layer of summarization, not proof that every gene is causal.
