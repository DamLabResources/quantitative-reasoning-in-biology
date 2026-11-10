# Gene-set enrichment and Enrichr

A table of significant genes is hard to read. **Over-representation analysis** asks whether those genes pile into known biological programs more than you’d expect by chance.

## How the test works (this module)

1. Build a list of “interesting” genes (here: FDR &lt; 0.05 and |log2FC| &gt; 1).
2. Compare that list to a library of curated gene sets.
3. For each set, ask whether the overlap is larger than expected under a hypergeometric (or Fisher) model, then adjust p-values across sets.

That is what **`gseapy.enrichr`** does: it sends your HGNC gene symbols to the [Enrichr](https://maayanlab.cloud/Enrichr/) server and returns overlap statistics and adjusted p-values. [gseapy](https://gseapy.readthedocs.io/) is the Python client you call from Colab.

## MSigDB

The [Molecular Signatures Database (MSigDB)](https://www.gsea-msigdb.org/gsea/msigdb) is a curated catalog of gene sets used across transcriptomics. Each set is a named list of genes that prior work associated with a process, pathway, or transcriptional program. Enrichr hosts many MSigDB collections as libraries you can query by name.

## Hallmark gene sets

This module uses the Enrichr library **`MSigDB_Hallmark_2020`**: the [MSigDB Hallmark collection](https://www.gsea-msigdb.org/gsea/msigdb/human/collections.jsp#H) (about fifty sets).

Hallmark sets were built to reduce redundancy in older MSigDB collections. Liberzon and colleagues refined overlapping pathway and process signatures into a smaller panel of coherent programs (for example interferon response, cell cycle, inflammatory signaling). Each Hallmark set keeps genes that consistently cohere across related source signatures, so a hit is easier to narrate than a long list of near-duplicate pathway names. Browse the individual sets and gene membership on the [Hallmark collection page](https://www.gsea-msigdb.org/gsea/msigdb/human/collections.jsp#H).

## What Enrichr is and is not

**Is:** a fast way to attach Hallmark themes to your differential-expression list.

**Is not:** proof that a program is active in every cell, or that every gene in the set moved for the same reason. Symbols must match the library (HGNC). Entrez IDs will silently drop.

## Practical notes for Colab

- Install once: `pip install gseapy==1.3.2`
- Call `gseapy.enrichr` with `gene_sets='MSigDB_Hallmark_2020'`, `organism='Human'`, and `outdir=None` (unless you want Enrichr to write a folder into the runtime)
- Needs network access
- After Enrichr returns, pick **one** significant set and look at those genes’ expression across samples—that is the lab’s second figure

## Links

- [Enrichr](https://maayanlab.cloud/Enrichr/)
- [gseapy documentation](https://gseapy.readthedocs.io/)
- [MSigDB](https://www.gsea-msigdb.org/gsea/msigdb)
- [MSigDB Hallmark collection](https://www.gsea-msigdb.org/gsea/msigdb/human/collections.jsp#H)
