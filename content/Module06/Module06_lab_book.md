# Lab

Remember, all assignments are due at 11:59 PM (Philadelphia time) on the Sunday of each instructional week.

## Learning Objectives
At the end of this learning activity you will be able to:
 - Practice creating statistical figures to answer biological questions.
 - Practice writing figure legends for statistical figures.
 - Practice writing descriptive reasonings about a figure.

**Note**: It is difficult to automatically grade figures as they are many "correct" answers.
So, most questions will accept _any_ figure or axis and then ask you to answer a question that should be obvious from a properly generated figure.
For all questions, assume a 95% interval.

--------------------------------------------


```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
data = pd.read_csv('cytokine_data.csv')
data.head()
```

## Explore the effect of cocaine use on `mcp1`

### Q1: Do cocaine users have a higher level of expression of `mcp1`?

|               |    |
| --------------|----|
| Points        | 5  |
| Public Checks | 2  |
| Hidden Tests  | 1  |

_Points:_ 5


```python
# Generate a plot which displays the spread of mcp1 measurements across cocaine use

q1_plot = ...

```


```python
# Answer 'users' or 'non-users', 'same'
q1_higher_level = ...
```


```python
grader.check("q1_cocaine_use_spread")
```

### Q2: Do cocaine users or non-users have a higher _average_ level of `mcp1`?

|               |    |
| --------------|----|
| Points        | 5  |
| Public Checks | 2  |
| Hidden Tests  | 1  |

_Points:_ 5


```python
# Generate a plot which displays the confidence of the mean of mcp1 expression across cocaine use

q2_plot = ...

```


```python
# Answer 'users' or 'non-users', 'same'
q2_higher_mean = ...
```


```python
grader.check("q2_cocaine_use_mean")
```

### Q3: Does Sex impact the effect of cocaine use on the average level of `mcp1` expression?

|               |    |
| --------------|----|
| Points        | 5  |
| Public Checks | 2  |
| Hidden Tests  | 1  |

_Points:_ 5


```python
# Generate a plot which displays the confidence of the mean of mcp1 expression across cocaine use

q3_plot = ...

```


```python
# Is it 'likely' or 'unlikely' that gender has an impact on the effect of cocaine use on mcp1?
q3_gender_impact = ...
```


```python
grader.check("q3_cocaine_use_gender_mean")
```

### Q4: Is there a correlation between infection length and `mcp1` expression?

|               |    |
| --------------|----|
| Points        | 5  |
| Public Checks | 2  |
| Hidden Tests  | 1  |

_Points:_ 5


```python

q4_plot = ...

```


```python
# Is there a correlation between infection length and mcp1 expression? 'yes' or 'no'
q4_infection_length_corr = ...
```


```python
grader.check("q4_infection_length")
```

### Q5: Does cocaine use impact the correlation between infection length and `mcp1` expression?

|               |    |
| --------------|----|
| Points        | 5  |
| Public Checks | 2  |
| Hidden Tests  | 1  |

_Points:_ 5


```python
# Generate a plot which displays the confidence of the mean of mcp1 expression across cocaine use

q5_plot = ...

```


```python
# Does cocaine use impact the rate of mcp1 increase with infection length? 'yes' or 'no'
q5_infection_length_cocaine_slope = ...
```


```python
grader.check("q5_infection_length_cocaine")
```

## Submission

Check:
 - That all tables and graphs are rendered properly.
 - Code completes without errors by using `Restart & Run All`.
 - All checks **pass**.
 
Then save the notebook and the `File` -> `Download` -> `Download .ipynb`. Upload this file to BBLearn.
