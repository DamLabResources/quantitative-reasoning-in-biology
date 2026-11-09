# Gene-set enrichment and Enrichr

A table of significant genes is hard to read. **Gene-set enrichment** asks whether those genes pile into known pathways, Hallmark programs, or other curated sets more than you’d expect by chance.

## Two common styles

### Over-representation (Enrichr)

1. Build a list of “interesting” genes (for example FDR < 0.05 and |log2FC| > 1).
2. Compare that list to a library of gene sets (Hallmark, GO, KEGG, …).
3. Test whether the overlap with each set is larger than expected under a hypergeometric (or Fisher) model.

This is what **`gseapy.enrichr`** does. It sends your symbol list to the Enrichr server and returns overlap statistics and adjusted p-values for each set.

### Rank-based GSEA (not used this week)

Every gene gets a score (fold change, t-statistic, …). The algorithm walks the ranked list and asks whether members of a set appear toward the top or bottom. No hard cutoff. Module 11 does **not** run preranked GSEA; Enrichr is enough for the learning goals.

## What Enrichr is and is not

**Is:** a fast way to attach biological themes to a differential-expression list.

**Is not:** proof that a pathway is activated in every cell, or that every gene in the set moved for the same reason. Gene symbols must match the library (HGNC symbols). Entrez IDs will silently drop.

## This module’s library

Walkthrough and lab use **`MSigDB_Hallmark_2020`**: about fifty coherent gene programs (interferon response, cell cycle, …) that are easier to narrate than thousands of GO terms.

## Practical notes for Colab

- Install once: `pip install gseapy==1.3.2`
- Pass `outdir=None` unless you want Enrichr to write a folder of files into the runtime
- Needs network access
- After Enrichr returns, pick **one** significant set and look at the leading genes’ expression across samples—that is the lab’s second figure
