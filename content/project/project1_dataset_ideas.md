# Picking a dataset

Finding the right dataset is a crucial first step in any data analysis project. This guide will help you locate appropriate datasets from popular repositories and understand what makes a dataset suitable for statistical analysis.

## Where to Find Datasets

### TidyTuesday GitHub Repository

**TidyTuesday** is an excellent source for high-quality, real-world datasets. It's a weekly data project organized by the R for Data Science online learning community.

- **Location**: [https://github.com/rfordatascience/tidytuesday](https://github.com/rfordatascience/tidytuesday)
- **How to browse**: Navigate to the `data` folder, where you'll find weekly datasets organized by year
- **Advantages**: 
  - All datasets are real-world data from reputable sources
  - Datasets are well-documented with clear data dictionaries
  - Many datasets include event-level observations
  - Community discussions provide context and analysis examples

**Example datasets to explore**:
- `2024/2024-01-09/` - Various datasets from different weeks
- Look for datasets with individual records (e.g., individual animals, patients, transactions, measurements)

### Kaggle

**Kaggle** is a popular platform for data science competitions and datasets, but requires careful evaluation.

- **Location**: [https://www.kaggle.com/datasets](https://www.kaggle.com/datasets)
- **How to browse**: Use the search function and filter by topic, file type, or license
- **Advantages**:
  - Large variety of datasets across many domains
  - Many datasets include detailed descriptions
  - Download options for different formats (CSV, JSON, etc.)
- **Cautions**:
  - **Many datasets are synthetic** - Always check the dataset description carefully
  - Some datasets may be pre-aggregated or summary statistics rather than raw data
  - Verify data provenance and source information

**Important**: Before using a Kaggle dataset, read our guide on [synthetic data](synthetic_data.md) to understand the risks and how to identify synthetic datasets.

## What Makes a Good Dataset for Statistical Analysis?

### Event-Level Data vs. Pre-Aggregated Data

**Event-level data** (also called "raw" or "transactional" data) contains individual observations or records. Each row represents a single event, measurement, or entity. This is what you want for statistical analysis.

**Examples of event-level data**:
- Individual patient records with measurements (one row per patient)
- Daily weather observations (one row per day per location)
- Individual animal sightings or captures (one row per observation)
- Individual transactions or purchases (one row per transaction)
- Individual experimental measurements (one row per replicate)

**Pre-aggregated data** contains summary statistics or already-computed aggregations. This is **not suitable** for statistical analysis because:
- You cannot perform your own statistical tests
- You cannot explore relationships between variables
- You cannot assess variability or uncertainty
- The data has already been processed, losing important information

**Examples of pre-aggregated data to avoid**:
- Tables showing only means, medians, or summary statistics
- Data where each row represents a group average (e.g., "average height by country")
- Datasets described as "summary" or "aggregated"
- Data that has been "pre-processed" or "cleaned" to the point where individual observations are lost

### How to Identify Event-Level Data

When evaluating a dataset, ask yourself:

1. **What does each row represent?**
   - Good: Each row is an individual observation (patient, animal, measurement, event)
   - Bad: Each row is a summary or aggregate (average, total, percentage)

2. **Can you see variability in the data?**
   - Good: Multiple rows with different values for the same variable
   - Bad: Only one value per category or group

3. **Does the dataset description mention individual records?**
   - Good: "Contains 1,000 patient records" or "Individual measurements from experiments"
   - Bad: "Summary statistics" or "Aggregated by region"

4. **Can you perform statistical tests?**
   - Good: You can calculate means, standard deviations, run t-tests, etc.
   - Bad: The data is already summarized, leaving no room for analysis

### Example: Good vs. Bad Dataset Structure

**Good (Event-Level)**:
```
patient_id | age | height | weight | diagnosis
-----------|-----|--------|--------|----------
001        | 45  | 165    | 70     | Type A
002        | 32  | 172    | 68     | Type B
003        | 28  | 158    | 65     | Type A
...
```

**Bad (Pre-Aggregated)**:
```
diagnosis | avg_age | avg_height | avg_weight | n_patients
----------|---------|------------|------------|------------
Type A    | 38.5    | 162.3      | 68.2       | 150
Type B    | 42.1    | 170.8      | 72.5       | 120
```

## Checklist for Dataset Selection

Before committing to a dataset, verify:

- [ ] **Event-level data**: Each row represents an individual observation
- [ ] **Real-world data**: Not synthetic or artificially generated (see [synthetic data guide](synthetic_data.md))
- [ ] **Clear data dictionary**: You understand what each column represents
- [ ] **Reasonable size**: Not too small (< 30 observations) or too large to work with comfortably
- [ ] **Interesting to you**: You have genuine curiosity about the research questions
- [ ] **Appropriate for your analysis goals**: The variables match what you want to explore

## Red Flags to Avoid

- ⚠️ **Synthetic data**: Datasets explicitly labeled as "synthetic," "simulated," or "generated"
- ⚠️ **Pre-aggregated summaries**: Data that's already been summarized or aggregated
- ⚠️ **Missing provenance**: No clear source or data collection method described
- ⚠️ **Too "perfect"**: Data that looks suspiciously clean or has unrealistic patterns
- ⚠️ **Vague descriptions**: Dataset descriptions that lack concrete details about data collection

For more information on identifying and avoiding synthetic data, see our [synthetic data primer](synthetic_data.md).

## Getting Help

If you're unsure whether a dataset is appropriate:
1. Check the dataset description carefully
2. Look at the first few rows of data
3. Read community discussions (especially on TidyTuesday and Kaggle)
4. Ask your instructor or peers for feedback
5. When in doubt, choose a different dataset

Remember: The goal is to work with real, event-level data that allows you to perform meaningful statistical analysis. Taking time to find the right dataset will make your project much more rewarding!
