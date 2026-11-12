# Module 11 lab prompts

Companion to the [Module 11 lab](Module11_lab.ipynb). The load cells in the lab notebook are already filled. Use Colab’s cell-level AI for Q1–Q2B only. Do **not** recompute the gene-wise t-tests or FDR from the walkthrough—the saved `results` table is the input.

You write your own prompts. Below is the point of each step so you know what “done” looks like.

---

## Load (already in the notebook)

**Point:** Confirm you have `samples`, `log2`, and `results`, with n per group and a non-empty significant gene count.

---

## Q1. Volcano plot

**Point:** Visualize genome-wide effect size (log2 fold change) against statistical confidence (`-log10` FDR), and see how many genes clear FDR &lt; 0.05.

---

## Q2A. Enrichr on the significant list

**Point:** Turn the significant gene list (FDR &lt; 0.05 and |log2FC| &gt; 1) into Hallmark enrichment with `gseapy.enrichr` (`MSigDB_Hallmark_2020`, `outdir=None`) and inspect the top terms.

---

## Q2B. Plot the top |log2FC| genes from one Hallmark term

**Point:** For one significant Enrichr term, take the 10 overlap genes with largest absolute log2FC and show their log2 expression across samples by group—so the pathway hit is tied back to the people in the study.
