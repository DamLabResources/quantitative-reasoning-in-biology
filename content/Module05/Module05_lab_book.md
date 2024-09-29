# Lab

Remember, all assignments are due at 11:59 PM (Philadelphia time) on the Sunday of each instructional week.

## Introduction

This week we will look at data from a cohort of People Living with HIV (PLH) here at Drexel.

As we discussed in the introduction, this data collection effort was done to provide a resource for many projects across the fields of HIV, aging, inflammation, neurocognitive impairment, immune function, and unknowable future projects.
In this lab we will explore a collection of cytokines and chemokines measured by a Luminex panel of common biomarkers of inflammation.

## Learning Objectives
At the end of this learning activity you will be able to:
 - Pratice creating barplots and scatterplots.
 - Employ `DataFrame.corr` to measure the correlation between varaibles.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
```


```python
data = pd.read_csv('cytokine_data.csv')
data.head()
```

### Q1: Explore the neurological function of the participants in the dataset.

Create a barplot for the `neuro_screen_impairment_level` level categories.

 - Adjust the y-axis to have a limit of 0 to 150 and the label to Participants
 - Adjust the x-label to Impairement Level

|               |    |
| --------------|----|
| Points        | 2  |
| Public Checks | 5  |
| Hidden Testss | 0  |

_Points:_ 2


```python

# Generate the figure
q1_ax = ...


# Adjust labels and limits

```


```python
# DO NOT REMOVE!
plt.close()
# For the grader
```


```python
grader.check("q1_impairement_plot")
```

### Q2: Consider how pro-inflamatory markers are related to neurological impairment.

Examine the expression of the following cytokines.
 - `tnfalpha`
 - `il6`
 - `mcp1`
 - `mip1alpha`



|               |    |
| --------------|----|
| Points        | 10 |
| Public Checks | 9  |
| Hidden Testss | 1  |

_Points:_ 10


```python

q2_cytokine_summary = ...

```


```python

q2_axs = ...

```


```python
# Answer as a string

q2_ans = ...
```


```python
# DO NOT REMOVE!
plt.close()
# For the grader
```


```python
grader.check("q2_pro_inflam")
```

### Q3: Hypothesis generation

One advantage of a cohort-style study is that the data can be used to generate new hypotheses to test.
Here, we have collected the cytokine expression of many people along with their BMI.
Use the `.corr()` method to find the correlation between BMI and all cytokines.
Then, generate a hypothesis about which top-5 cytokines are worth a followup.

|               |    |
| --------------|----|
| Points        | 10 |
| Public Checks | 10 |
| Hidden Testss | 3  |

_Points:_ 10


```python
# Calculate the cross correlation matrix that only includes bmi and other cytokines

q3_cross_cor = ...

```


```python
# Plot the correlation between BMI and all other columns

q3_bar_ax = ...
```


```python
# Extract a Series of the top 5 cytokines 
q3_top5 = ...
```


```python
# Create a scatterplot between the bmi (on the x-axis) and the most correlated cytokine (on the y-axis)

q3_scatter_ax = ...
# Leave the axes labels as defaults for the grader
```


```python
grader.check("q3_bmi_hypothesis_gen")
```


```python
# DO NOT REMOVE!
plt.close()
# For the grader
```

With this information in hand, one could design more directed experiments to further understand whether these correlations are biologically meaningful.
This hypothesis generating technique is useful in a number of ways.

<!-- BEGIN QUESTION -->

### Q4: Exploration

Use this technique to find correlations between between cytokines and any other demographic variable.

Include at least one barplot of correlation coefficients.
If your variable is categorical, use show a boxplot of the most correlated cytokine.
If your variable is continious, instead show a scatterplot.

With each figure, include a text-box with a figure caption.

There is no grader for this question.

_Points:_ 10

<!-- END QUESTION -->




```python
# DO NOT REMOVE!
plt.close()
# For the grader
```

--------------------------------------------

## Submission

Check:
 - That all tables and graphs are rendered properly.
 - Code completes without errors by using `Restart & Run All`.
 - All checks **pass**.
 
 Then save the notebook and the `File` -> `Download` -> `Download .ipynb`. Upload this file to BBLearn.

