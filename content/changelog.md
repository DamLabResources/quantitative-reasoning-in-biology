# Change Log

This page notes all of the major changes introduced since the initial launch of this book.

- 2026-11-09 - **Modules 11 and 12 (AI-assisted analysis):**
  - Module 11: staged GSE199911 TPM / DE tables, background pages (RNA-seq, TPM, multiple testing, Enrichr; RNA-seq page links the Parker et al. PMC full text), student and INTENDED walkthrough/lab notebooks, and book pages for walkthrough/lab Colab AI prompts.
  - Module 12: staged Depresjon minute actigraphy (`depresjon_minute.csv.gz`, CC BY-NC), dataset / datetime / agent-vs-codegen pages, and skeletal walkthrough/lab notebooks for the Data Science Agent.
  - Added Part 4 to the book TOC. Module 12 prompt materials wait on the recording.
  - Added Colab stub test folders and `tests/Module11_files.zip` / `tests/Module12_files.zip` (data + stubs) so `setup_environment` works when pushed.
  - Module 11 walkthrough prompts: moved names/thresholds into Point; concise sample prompts behind hint tags.
  - Expanded gene-set enrichment page: MSigDB, Hallmark construction, Enrichr/gseapy/MSigDB links; removed unused methods.
  - Merged TPM into `how_rnaseq_works.md`, added DE context (Welch vs DESeq2/edgeR/limma/resampling), removed `what_is_a_tpm.md`.
  - Part 4 opener: `part4/ai_programming_styles.md` (cell-by-cell natural-language programming vs agentic coding).
- 2026-10-26 - Fixed broken Pingouin documentation links in Module 8 and Module 10 walkthroughs (docs moved off `/build/html/` to root paths like `/api.html`, `/generated/…`, `/_images/…`).
- 2026-10-26 - Removed leftover due-date reminders from Module 1 lab, Module 1 walkthrough book, and Module 8 lab.
- 2026-01-18 - **Testing Improvements and project ideas**
  - Adjusted the Module 5 testing to ask questions about figures instead of prescribing particular figures.
  - Created [Project Ideas](project/project1_dataset_ideas.md) to describe how to pick projects.
  - Created a [Synthetic Data Explanation](project/synthetic_data.md) to describe synthetic data, its uses, and drawbacks.
  - Fixed course-wide copy-paste typo of 'Hidden Testss'.
  - Added Github Readme re-direct incase students land in the wrong place.

- 2025-10-24 - **Enhanced all lab notebooks with clearer expectations:**
  - Added "Checked variables" sections with detailed format expectations and types to all lab questions (Modules 2-10).
  - Added collapsible hints linking to relevant walkthrough sections.
  - Created [Python Types Reference](misc/python_types_reference.md) guide for common data types.
  - Created [Python Syntax Guide](misc/python_syntax_guide.md) guide for language syntax issues.
  - Created [Troubleshooting Errors](misc/troubleshooting_errors.md) which describes how to read an error and common causes.
  - Combined "Checked variables" and "Expected Output Format" sections in Modules 8-10 for clarity.
  - Fixed minor heading inconsistencies in notebook structure.
- 2025-08-11 - Added section on installing Jupyter locally through Anaconda.
- 2025-07-22 - Added real landing page and back-matter _about_ pages.
- 2025-07-17 - Adjusted assignments to use `applied-biostats-helper` module to simplify environmental setup.
- 2025-03-06 - Adding a 'Checked variables' section to Lab questions with the names and structure of variables the grader expects.
- 2025-02-12 - Added an additional section in Module 4 with examples on grouping and pivoting.
- 2025-02-06 - Otter rendering issue caused some Lab instructions to get removed from student and website versions. Now fixed.
- 2025-01-01 - New Year Launch
