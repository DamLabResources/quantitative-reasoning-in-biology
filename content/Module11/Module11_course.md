# Module 11: RNA-seq, multiple testing, and Enrichr

## Overview

This week you analyze a staged PBMC RNA-seq table from acute HIV infection versus uninfected controls (GSE199911). You will work on a log2 TPM scale, run a gene-wise t-test with Benjamini–Hochberg FDR, and interpret the result with Enrichr gene-set enrichment. The walkthrough and lab use Colab’s cell-level AI: you write plain-English prompts, run the generated code, and check the objects. Read [Three styles of AI-assisted programming](../part4/ai_programming_styles.md) first if you have not yet.

## Learning resources

### Background pages (short videos)

**Technology and this study**

- [How RNA-seq works](how_rnaseq_works.md) — quantification, TPM, and differential expression

**Multiple testing and enrichment**

- [Multiple testing](multiple_testing.md)
- [Gene-set enrichment and Enrichr](gene_set_enrichment.md)

### Having trouble with syntax or errors?

- [Python Syntax Quick Reference](../misc/python_syntax_guide.md)
- [Troubleshooting Common Errors](../misc/troubleshooting_errors.md)

## Learning activities

### Read

Review the three background pages above before the walkthrough.

### Participate: Walkthrough

Complete the Module 11 walkthrough notebook. Use the [walkthrough prompts](Module11_walkthrough_prompts.md) page for Colab cell-level AI prompts, one step at a time.

### Complete: Lab

Open the Module 11 lab notebook. The differential-expression table is already loaded. Use the [lab prompts](Module11_lab_prompts.md) page for the point of each step, then write your own Colab AI prompts for the volcano plot and Enrichr gene plot.

## Getting help

- **Office Hours**: Thursday 8 PM at the course Zoom link
- **Discussion Board**: Post conceptual questions
- **For coding help**: Attend office hours or TA sessions

## Tips for success

1. Read the background pages before prompting the AI
2. Name the objects the next cell will need (`results`, `sig_genes`, …)
3. Check `n` and group sizes before trusting a p-value
4. Enrichr needs network access in Colab
