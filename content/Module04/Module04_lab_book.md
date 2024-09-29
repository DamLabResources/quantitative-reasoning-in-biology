# Lab

## Introduction

In this session, we will delve into the relationship between the microbiome of the sinus system and the severity and duration of sinus infections.
We have classified our patients into three groups: those with typical infections that resolve without complications on standard therapy, those with severe infections that require aggressive medical intervention, and those with persistent infections that relapse shortly after initial symptoms resolve.
Using pivot tables we will compare the microbiomes of these different groups and explore the clinical implications of our findings.
Throughout this lab, you will have the opportunity to practice adding data to a `DataFrame`, employing pivot tables to compare microbiomes, describing biostatistical results, and formulating clinical uses for your analysis.

Let's get started!

In this learning activity you will:
  - Practice adding data into a `DataFrame`
  - Employ pivot tables to compare microbiomes across disease outcomes
  - Describe biostatistical results in "paragraph form"
  - Formulate a clinical use for your analysis


```python
import numpy as np
import pandas as pd
```


```python
data = pd.read_csv('microbiome_phylum_data.tsv', delimiter = '\t')
data
```

### Q1: Merge the `biome_data` table with the sample information

We are interested in exploring the relationship between the microbiome of the sinus system and the severity and duration of a sinus infection.
To do this, we need to first classify each patient into one of three groups:
 - those with a `typical` infection that resolved without complications on standard therapy
 - those with a `severe` infection that required aggressive medical intervention
 - those with a `persistent` infection that relapsed shortly after the initial symptoms resolved

By assigning each row of our table with the appropriate outcome, we can begin to compare the microbiomes of these different groups and consider the potential clinical implications of our analysis.

This step is crucial because it allows us to accurately analyze and interpret the data, and is a necessary foundation for the rest of the lab.

Use Pandas to load the `sample_info.csv` file and merge it with the `biome_data`.


```python

# Load the sample information from sample_info.csv
# Merge that information with the biome_data

merged_data = ...


```


```python
grader.check("q1_add_outcomes")
```

### Q2: Determine the predomininant phylum across regions.

Use a pivot table to count the number of unique patients that have `Actinobacteria` or `Firmicutes` as the `Predominant` phylum at each body site.


```python

# Create the pivot table described in the question.
# Pay attention to using the correct `index`, `columns`, `values`, and `aggfunc` parameters
# It expects the rows to be body-sites
# The columns to be phylumns
# And the values to number of unique patients with that predominant phylum at that body-site

q2_pivot = ...

```


```python
q2_pivot.head()
```


```python
# Which regions have at least twice as many patients with Firmicutes as predominant relative to Actinobacteria
# This should be a subset of the q2_pivot DataFrame
q2_firmi_regions = ...
q2_firmi_regions
```


```python
grader.check("q2_count_pivot")
```

### Q3: Which body site has the largest increase in Actinobacteria when comparing typical and severe disease outcomes?

Find which body site has the largest increase in Actinobacteria when comparing typical and severe disease outcomes.
Utilize pivot tables to compare the relative abundances of Actinobacteria across disease states and body sites.

|               |    |
| --------------|----|
| Points        | 5  |
| Public Checks | 8  |
| Hidden Testss | 1  |

_Points:_ 5


```python
# Create a pivot table which averages the count of Actinobacteria across each patient
# for each body-site and disease type
q3_pivot = ...

```


```python
# Add a relative_abundance column
# This should be the difference between the severe and typical columns
q3_pivot['relative_abundance'] = ...
```


```python
# Which body site has the largest *increase* in Actinobacteria in those with *severe* disease?

# Display the table above (optionally with sorting)
# Or use programatically https://pandas.pydata.org/docs/search.html?q=idxmax
# Answer as a text string.

q3_ans = ...
```


```python
grader.check("q3_mean_pivot")
```

The above analysis describes a population level result.
A _sample_ of people with severe disease have more Actinobacteria in some regions than those that have typical disease.
However, that tells us little about the impact on an _individual_.
Let's reframe this into a clinical application.

Can you use the amount of Actinobacteria as a predictor of disease?

### Q4: Which tissues are "swabbable"?

If we would like to use microbiome sampling as a clinical assay to detect severe infections, it would be helpful if those areas are "easy to access".
This dataset is a collection of samples that came from both biopsies and swabs.
Create a subset of the data that only contains `Swab` samples.

|               |    |
| --------------|----|
| Points        | 2  |
| Public Checks | 6  |
| Hidden Testss | 1  |

_Points:_ 2


```python
# Use boolean indexing or a query create a new table with only samples that came from samples with data from swabs.
swabbable_data = ...
```


```python
# What fraction of the data came from swab samples?
# Your answer should be between 0 and 1.
q4_fraction_swabbable = (merged_data['CollectionType'] == 'Swab').mean()

```


```python
print(f'{q4_fraction_swabbable*100:0.2f}% of the data came from swabbable samples')
```


```python
grader.check("q4_swabable")
```

### Q5: Which samples are _high_?

Previously, we saw that there was more Actinobacteria in across certain regions in severe disease.
In this case, we'll consider **high** as being 1 standard-deviation above the average of typical patients for that region.



Create a new column in `swabbable_data` called `is_high` that is true if the Actinobacteria is 1 standard-deviation above the average for that region.

|               |    |
| --------------|----|
| Points        | 5  |
| Public Checks | 2  |
| Hidden Testss | 0  |

_Points:_ 5


```python
# Isolate the subset of swabbable_data that come from typical disease types
typical_swab_data = ...
```


```python
# Use `groupby()` to aggregate values while keeping the same shape

typical_region_means = ...
typical_region_stds = ...
```


```python
# Combine the values to create a cutoff 
typical_region_cutoff = typical_region_means+typical_region_stds
```


```python
typical_region_cutoff
```


```python
# Add a new column called `is_high`
# If you've done the above cells correctly, this will run.

# Get the appropriate cutoff into each row
row_cutoff = swabbable_data['Location'].map(typical_region_cutoff.get)

swabbable_data = swabbable_data.assign(is_high = swabbable_data['Actinobacteria'] > row_cutoff)
```


```python
grader.check("q5_high_values")
```

### Q6: Which swabbable region has the highest positive predictive value when predicting **persistent** disease?

The positive predictive value is the ratio of patients truly diagnosed as positive vs all those who had positive test results.
It indicates the likelihood that a patient "has the condition" given a positive test.
This makes PPV one of the most useful metrics when describing diagnostic tests to clinicians and patients.

Use the `is_high` column as a prediction of whether a patient has a persistent infection.
Calculate the PPV for each region.
In the provided space, place the most accurate region and its calculated PPV.

|               |    |
| --------------|----|
| Points        | 10  |
| Public Checks | 3  |
| Hidden Testss | 2  |

_Points:_ 10


```python

# There are a number of ways to approach this problem
# Look back through the groupby and pivot table explanations


q6_highest_region = ...
q6_best_ppv = ...
```


```python
grader.check("q6_swabbable_ppv")
```

<!-- BEGIN QUESTION -->

### Q7: Context

Put these results into context.

_Points:_ 5

Write your solution here in this box and consider the following:
 - What are the number 2 and 3 swabbable regions when ranking by PPV?
 - How many patients are these results based on?
 - Consider the likelihood of persistent infections relative to the PPV. Is the test giving more information compared to a null assumption?

<!-- END QUESTION -->

--------------------------------------------

## Submission

Check:
 - That all tables and graphs are rendered properly.
 - Code completes without errors by using `Restart & Run All`.
 - All checks **pass**.
 
Then save the notebook and the `File` -> `Download` -> `Download .ipynb`. Upload this file to BBLearn.
