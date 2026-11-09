# How RNA-seq works

RNA sequencing (RNA-seq) measures how much of each gene’s RNA is present in a sample. For this course you never touch raw FASTQ files. You start from a **gene-by-sample matrix** that someone else already quantified.

## From cells to a matrix

1. **Isolate RNA** from a biological sample (here, peripheral blood mononuclear cells, PBMCs).
2. **Make a sequencing library**: convert RNA to complementary DNA (cDNA), fragment it, and add adapters.
3. **Sequence** millions of short reads on an Illumina instrument.
4. **Align or pseudo-align** those reads to a reference transcriptome or genome.
5. **Count** how many reads (or fragments) map to each gene in each sample.

The product is a table: rows are genes, columns are samples, and values are abundances. That table is what Module 11 analyzes.

## What this module does *not* do

- No FASTQ download
- No alignment
- No genome indexing
- No batch-effect modeling beyond a simple two-group design

Those steps matter in a methods course. Here the biostatistics question is: given a ready matrix, how do you compare two groups of people across thousands of genes without drowning in false positives?

## This week’s study (GSE199911)

[Parker et al. (2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10106835/) sequenced PBMCs from people about one month into acute HIV-1 infection and from contemporaneous uninfected controls recruited in the same setting ([GSE199911](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE199911)). The staged course files keep **29 HIV** and **46 control** samples. The scientific claim in the paper is a large early host response (cell cycle, DNA repair, immune activation). Your job is to recover a similar story with a transparent teaching pipeline: log2 TPM, Welch t-tests, Benjamini–Hochberg FDR, then Enrichr.
