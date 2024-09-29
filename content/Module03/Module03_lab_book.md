# Lab

Remember, all assignments are due at 11:59 PM (Philadelphia time) on the Sunday of each instructional week.

## Introduction

In this lab, you will use Python to analyze data from a hypothetical HIV treatment trial and explore the effects of the treatment on different types of participants.
Specifically, you will look at the infection status of participants at the start of the treatment and the length of their infection.
These considerations have clinical implications for the application of the treatment.
Through this activity, you will practice using Python methods to append a column to an existing table, load spreadsheet data into Python using the Table object, create derived columns in tables, and use Python summary methods like sum, mean, and max.

## Learning Objectives

At the end of this learning activity you will be able to:
 - Use Python methods to append a column into an existing table.
 - Practice loading spreadsheet data into Python using the `Table` object.
 - Use Python methods to create derived columns in Tables
 - Use Python summary methods like sum, mean, and max

## Dataset Reference

_File_: `trail_data.csv`

_Columns_:

 - `age` : (years) Current age during the study. 
 - `age_initial_infection` : (years) Age at which the participant was initially infected.
 - `initial_viral_load` : (copies/ul) The level of infection at the start of the study.
 - `treatment` : (boolean) `True` for participants in the treatment group, `False` for those in the control group.
 - `weeks_to_failure` : (weeks) Time from the treatment to the first week of uncontrolled viral load.




```python
import numpy as np
import pandas as pd
```

## Questions

### Q1: Load in the data from the CSV file.

_Hint: Remember to use the `read_csv` function of the `pandas` library._

|               |    |
| --------------|----|
| Points        | 2  |
| Public Checks | 2  |
| Hidden Tests  | 0  |

_Points:_ 2


```python
trial_df = ...
trial_df.head()
```


```python
grader.check("q1_table_loading")
```

### Q2: Calculate the length of for each row.

Create a derived column in `trial_df` with the column name `infection_time` that indicates the length of the the infection.

_Hint: You can extract two columns and subtract them. And you can do this in one line or many._

_Points:_ 3


```python
trial_df['infection_time'] = ...
```


```python
grader.check("q2_infection_time")
```

To understand the effectiveness of the HIV treatment being evaluated in this experiment, focus the analysis on the individuals in the **treated** group.
By examining this group specifically, you can better understand how factors such as age and initial viral load may impact the effectiveness of the treatment.

### Q3: Create a new `DataFrame` that includes only the treated individuals.

Create a new table that includes only the treated individuals, you can use the `query` method to filter the original table by the value of the `treatment` column.

|               |    |
| --------------|----|
| Points        | 3  |
| Public Checks | 3  |
| Hidden Tests  | 0  |

_Points:_ 3


```python
treated_df = ...
treated_df
```


```python
grader.check("q3_treated_indiv")
```

### Q4: Make two new tables that contain high and low initial viral load samples of the *treated* individuals.

For this next step, we will create two separate tables that contain the treated individuals with either high or low initial viral load.
This will allow us to compare the effectiveness of the treatment between participants with different levels of disease severity at the start of the treatment.
To do this, we can use the `DataFrame.query` method to filter the `treated_df` `DataFrame` we created earlier based on the value of the initial_viral_load column.
Create two tables, one for treated participants with high initial viral load **(defined as >= 50 copies/ul)** and one for treated participants with low initial viral load **(defined as < 50 copies/ul)**.
This will allow us to see if the treatment is more or less effective for participants with different levels of disease severity at the start of the treatment.

|               |    |
| --------------|----|
| Points        | 4  |
| Public Checks | 6  |
| Hidden Tests  | 0  |

_Points:_ 4


```python
high_treated_df = ...
low_treated_df = ...
```


```python
grader.check("q4_vl_selection")
```

Now that there are two different `DataFrames`s we can see if there are any differences in the treated individuals.


```python
low_treated_df["weeks_to_failure"]
```


```python
low_treated_df["weeks_to_failure"]
```

### Q5: Calculate descriptive statistics on the `weeks_to_failure` column to compare the high and low viral load participants.

To better understand the impact of initial viral load on the effectiveness of the treatment, we will compare the weeks_to_failure data for treated participants with high and low initial viral loads.
By calculating descriptive statistics such as mean, median, and standard deviation, we can determine whether there are significant differences between the two groups and gain insights into how initial viral load may affect the success of the treatment.
To do this, we will first need to create two separate tables for treated participants with high and low initial viral loads, and then calculate the relevant statistics for each group.

_Hint: Remember methods like `.mean()` and `.min()` can be called on extracted columns._

|               |    |
| --------------|----|
| Points        | 6  |
| Public Checks | 5  |
| Hidden Tests  | 4  |

_Points:_ 6


```python

# average weeks_to_failure for low viral load participants
low_mean = ...

# minimum weeks_to_failure for low viral load participants
low_min = ...


# for high viral load participants
high_mean = ...
high_min = ...
```


```python
print('The low viral load participants had an average time to failure ',
      f'of {low_mean} ',
      f'with a minimum {low_min} weeks')
print('The high viral load participants had an average time to failure ',
      f'of {high_mean} ',
      f'with a minimum {high_min} weeks')
```


```python
grader.check("q5_vl_comparison")
```

Our initial analysis suggests that there may not be a significant difference between the two groups of treated participants in terms of the time until failure.
However, we will continue to explore this data in future weeks to get a more definitive answer.

### Q6: Calculate the same descriptive statistics on the `weeks_to_failure` column to compare the **treated** participants with short and long infection lengths.

In this final question, we will investigate whether the length of time a participant has been infected with HIV impacts the effectiveness of the treatment.
Specifically, we will compare the weeks to failure for treated participants with short and long infection lengths.
For this analysis, we will consider participants with less than 10 years of infection to have a short infection length, and those with 10 years or more to have a long infection length.
It is important to note that these arbitrary cut-offs were chosen for the purpose of this analysis and may not necessarily reflect the clinical definitions of short and long infection lengths.

To answer this question, we will need to calculate the descriptive statistics on the `weeks_to_failure` column for treated participants with short and long infection lengths.

_Remember, it is helpful to break down the problem into smaller steps and create intermediate cells to better understand and debug the analysis._

|               |    |
| --------------|----|
| Points        | 8  |
| Public Checks | 5  |
| Hidden Tests  | 4  |

_Points:_ 8


```python


# average weeks_to_failure for short infection lengths
short_mean = ...

# minimum weeks_to_failure for the short infection lengths
short_min = ...


# for long infection lengths
long_mean = ...
long_min = ...
```


```python
print('The participants with short infections had an average time to failure ',
      f'of {short_mean:0.1f} ',
      f'with a minimum {short_min:0.1f} weeks')
print('The participants with long infections had an average time to failure ',
      f'of {long_mean:0.1f} ',
      f'with a minimum {long_min:0.1f} weeks')
```


```python
grader.check("q6_length_comparison")
```

<!-- BEGIN QUESTION -->

To reflect on the results from the lab, we can consider the fact that participants with longer infections have a ~1/2 week shorter time to treatment failure compared to those with shorter infections.
This difference might seem small in reference to the average value across untreated participants in the study, as well as in comparison to the difference between high and low initial infections.
However, it is important to consider whether this difference is large or small in a clinical context.
Therefore, it is important to carefully consider the clinical significance of any observed differences in the results of a study.

**Edit the next cell (as a Markdown cell) and put this 1/2 week difference into context.
Consider the following things:**
 - Is it large or small in reference to the average value across untreated participants in the study?
 - Is it large or small in reference to the difference between high & low initial infections?
 - Is it large or small in a clinical context?

| **Total Points** | 5 |
|--------|----|
| Manual | 5 |




_Points:_ 5

**_Write answer here._**

<!-- END QUESTION -->

--------------------------------------------


```python
grader.check_all()
```

## Submission

Check:
 - That all tables and graphs are rendered properly.
 - Code completes without errors by using `Restart & Run All`.
 - All checks **pass**.
 - Excess code cells and print statments have been removed to create a _clean_ submission.

Remember, as this is a lab, there are hidden tests that you will be evaluated against.
Just because all checks pass does not mean everything is correct.
Double-check your work!

Then save the notebook and the `File` -> `Download` -> `Download .ipynb`. Upload this file to BBLearn.
