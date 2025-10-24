# Python Types Reference Guide

This guide explains the common data types you'll encounter in this course and what you can do with them.

## How to Check a Type

```python
# Check the type of any variable
type(my_variable)

# Example
x = 5
print(type(x))  # Output: <class 'int'>

# Check if something is a specific type
isinstance(x, int)  # Returns True or False
```

---

## Python Built-in Types

### Numbers

#### int (Integer)
**What it is:** Whole numbers (no decimal point)

**Examples:**
```python
age = 25
count = 100
negative = -5
```

**Common operations:**
```python
x = 10
y = 3

# Arithmetic
x + y    # Addition: 13
x - y    # Subtraction: 7
x * y    # Multiplication: 30
x / y    # Division: 3.333...
x // y   # Integer division: 3
x % y    # Modulo (remainder): 1
x ** y   # Power: 1000

# Comparison
x > y    # Greater than: True
x == y   # Equal to: False
```

#### float (Floating Point Number)
**What it is:** Numbers with decimal points

**Examples:**
```python
height = 1.75
temperature = 98.6
pi = 3.14159
```

**Common operations:**
```python
# Same as int, plus:
round(3.14159, 2)  # Round to 2 decimals: 3.14
abs(-5.5)          # Absolute value: 5.5
```

**Converting between types:**
```python
int(3.9)      # Converts to int: 3 (truncates, doesn't round)
float(5)      # Converts to float: 5.0
int('42')     # String to int: 42
float('3.14') # String to float: 3.14
```

---

### Text

#### str (String)
**What it is:** Text data

**Examples:**
```python
name = 'Alice'
message = "Hello, World!"
column_name = 'age'
```

**Common operations:**
```python
text = 'Hello World'

# Concatenation
'Hello' + ' ' + 'World'  # 'Hello World'

# Length
len(text)  # 11

# Case conversion
text.lower()  # 'hello world'
text.upper()  # 'HELLO WORLD'

# Splitting
text.split()  # ['Hello', 'World']

# Checking contents
'Hello' in text     # True
text.startswith('H') # True
text.endswith('d')   # True

# Replacing
text.replace('World', 'Python')  # 'Hello Python'

# Stripping whitespace
'  hello  '.strip()  # 'hello'
```

**F-strings (formatted strings):**
```python
name = 'Alice'
age = 25

# Modern way (Python 3.6+)
message = f'{name} is {age} years old'
# Output: 'Alice is 25 years old'

# With formatting
pi = 3.14159
f'{pi:.2f}'  # '3.14' (2 decimal places)
```

---

### Collections

#### list
**What it is:** Ordered, mutable collection

**Examples:**
```python
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']
mixed = [1, 'two', 3.0, True]
```

**Common operations:**
```python
my_list = [1, 2, 3]

# Accessing elements (0-indexed)
my_list[0]      # First element: 1
my_list[-1]     # Last element: 3
my_list[0:2]    # Slice: [1, 2]

# Adding elements
my_list.append(4)         # Add to end: [1, 2, 3, 4]
my_list.insert(0, 0)      # Insert at position: [0, 1, 2, 3, 4]
my_list.extend([5, 6])    # Add multiple: [0, 1, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(0)    # Remove first occurrence of value
my_list.pop()        # Remove and return last element
my_list.pop(0)       # Remove and return element at index

# Other operations
len(my_list)         # Length
3 in my_list         # Check if contains: True/False
my_list.sort()       # Sort in place
sorted(my_list)      # Return sorted copy
my_list.reverse()    # Reverse in place
```

#### tuple
**What it is:** Ordered, immutable collection (can't be changed after creation)

**Examples:**
```python
coordinates = (10, 20)
rgb = (255, 128, 0)
```

**Common operations:**
```python
my_tuple = (1, 2, 3)

# Accessing (same as list)
my_tuple[0]   # 1
len(my_tuple) # 3

# Cannot modify!
# my_tuple[0] = 5  # This will cause an error!

# Unpacking
x, y = (10, 20)  # x=10, y=20
```

**When to use:** Function returns, dictionary keys, when you want to prevent modification

#### dict (Dictionary)
**What it is:** Unordered collection of key-value pairs

**Examples:**
```python
person = {'name': 'Alice', 'age': 25, 'city': 'Boston'}
settings = {'debug': True, 'timeout': 30}
```

**Common operations:**
```python
my_dict = {'name': 'Alice', 'age': 25}

# Accessing values
my_dict['name']         # 'Alice'
my_dict.get('name')     # 'Alice' (safer - won't error if key missing)
my_dict.get('city', 'Unknown')  # 'Unknown' (default if not found)

# Adding/modifying
my_dict['city'] = 'Boston'    # Add new key-value
my_dict['age'] = 26           # Update existing

# Checking
'name' in my_dict             # Check if key exists: True
len(my_dict)                  # Number of key-value pairs

# Getting all keys/values
my_dict.keys()                # dict_keys(['name', 'age', 'city'])
my_dict.values()              # dict_values(['Alice', 26, 'Boston'])
my_dict.items()               # key-value pairs

# Removing
my_dict.pop('city')           # Remove and return value
del my_dict['age']            # Remove key-value pair
```

**Iterating:**
```python
# Over keys
for key in my_dict:
    print(key)

# Over values
for value in my_dict.values():
    print(value)

# Over key-value pairs
for key, value in my_dict.items():
    print(f'{key}: {value}')
```

#### set
**What it is:** Unordered collection of unique values

**Examples:**
```python
unique_numbers = {1, 2, 3, 4, 5}
categories = {'A', 'B', 'C'}
```

**Common operations:**
```python
my_set = {1, 2, 3}

# Adding
my_set.add(4)           # {1, 2, 3, 4}

# Removing
my_set.remove(2)        # Removes 2, errors if not found
my_set.discard(2)       # Removes 2, no error if not found

# Checking
3 in my_set             # True

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.union(set2)        # {1, 2, 3, 4, 5}
set1.intersection(set2) # {3}
set1.difference(set2)   # {1, 2}
```

**When to use:** Remove duplicates, test membership, mathematical set operations

#### bool (Boolean)
**What it is:** True or False values

**Examples:**
```python
is_valid = True
has_error = False
```

**Common uses:**
```python
# In conditions
if is_valid:
    print('Valid!')

# Comparisons return booleans
5 > 3        # True
'a' == 'b'   # False

# Logical operations
True and False   # False
True or False    # True
not True         # False
```

---

## pandas Types

### pd.Series
**What it is:** One-dimensional labeled array (like a column in Excel)

**Examples:**
```python
import pandas as pd

# From a list
ages = pd.Series([25, 30, 35, 40])

# From a dictionary (keys become index)
grades = pd.Series({'Alice': 90, 'Bob': 85, 'Charlie': 92})

# Single column from DataFrame
age_column = data['age']  # This is a Series
```

**Common operations:**
```python
series = pd.Series([1, 2, 3, 4, 5])

# Accessing elements
series[0]           # First element
series.iloc[0]      # First element by position
series.head()       # First 5 elements

# Statistics
series.mean()       # Average
series.median()     # Median
series.std()        # Standard deviation
series.min()        # Minimum
series.max()        # Maximum
series.sum()        # Sum
series.describe()   # Summary statistics

# Boolean operations
series > 3          # Returns Series of True/False
series[series > 3]  # Filter: elements > 3

# Other operations
series.unique()     # Unique values
series.value_counts()  # Count of each unique value
series.isna()       # Check for missing values
series.dropna()     # Remove missing values
```

**Key attributes:**
```python
series.values       # Get underlying numpy array
series.index        # Get index
series.shape        # Shape (number of elements,)
series.dtype        # Data type
```

### pd.DataFrame
**What it is:** Two-dimensional labeled data structure (like a spreadsheet)

**Examples:**
```python
import pandas as pd

# From a dictionary
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Boston', 'NYC', 'LA']
})

# Reading data
df = pd.read_csv('data.csv')
```

**Common operations:**
```python
# Viewing data
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.info()           # Summary info
df.describe()       # Statistical summary
df.shape            # (rows, columns)

# Selecting columns
df['age']           # Single column (Series)
df[['age', 'name']] # Multiple columns (DataFrame)

# Selecting rows
df.loc[0]           # Row by label
df.iloc[0]          # Row by position
df.loc[0:5]         # Rows 0 through 5 (inclusive)
df.iloc[0:5]        # Rows 0 through 4 (exclusive)

# Filtering
df[df['age'] > 30]              # Rows where age > 30
df.query('age > 30')            # Same using query
df[(df['age'] > 30) & (df['city'] == 'NYC')]  # Multiple conditions

# Adding columns
df['age_squared'] = df['age'] ** 2

# Grouping
df.groupby('city').mean()       # Average by city
df.groupby('city')['age'].mean() # Average age by city

# Sorting
df.sort_values('age')            # Sort by age
df.sort_values('age', ascending=False)  # Descending

# Missing data
df.isna()           # Check for missing values
df.dropna()         # Remove rows with missing values
df.fillna(0)        # Replace missing with 0
```

**Key attributes:**
```python
df.columns          # Column names
df.index            # Row index
df.shape            # (rows, columns)
df.dtypes           # Data type of each column
df.values           # Underlying numpy array
```

**Checking type:**
```python
# Is it a Series?
isinstance(df['age'], pd.Series)  # True

# Is it a DataFrame?
isinstance(df, pd.DataFrame)  # True
```

---

## matplotlib Types

### plt.Figure
**What it is:** The entire window/page that holds your plot(s)

**Creating:**
```python
import matplotlib.pyplot as plt

# Automatically created when you plot
plt.plot([1, 2, 3])  # Creates figure automatically

# Explicitly create
fig = plt.figure(figsize=(10, 6))

# Create figure with subplots
fig, ax = plt.subplots()           # 1 plot
fig, axes = plt.subplots(2, 2)    # 2x2 grid of plots
```

**Common operations:**
```python
fig = plt.figure()

# Size
fig.set_size_inches(10, 6)

# Saving
fig.savefig('my_plot.png')
fig.savefig('my_plot.pdf', dpi=300)

# Showing
plt.show()
```

### plt.Axes
**What it is:** A single plot area within a figure (the actual plot)

**Creating:**
```python
# Method 1: Automatically created
plt.plot([1, 2, 3])  # Creates both figure and axes

# Method 2: Explicit creation
fig, ax = plt.subplots()

# Method 3: From seaborn/pandas
ax = sns.boxplot(data=df, x='category', y='value')
ax = df['age'].plot()
```

**Common operations:**
```python
fig, ax = plt.subplots()

# Plotting on axes
ax.plot([1, 2, 3], [1, 4, 9])          # Line plot
ax.scatter([1, 2, 3], [1, 4, 9])       # Scatter plot
ax.bar(['A', 'B', 'C'], [10, 20, 15])  # Bar plot
ax.hist([1, 2, 2, 3, 3, 3, 4])         # Histogram

# Labels and titles
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('My Plot')

# Limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

# Legend
ax.legend(['Series 1', 'Series 2'])

# Grid
ax.grid(True)
```

**Checking type:**
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

isinstance(fig, plt.Figure)  # True
isinstance(ax, plt.Axes)     # True

# Many plotting functions return Axes
result = sns.boxplot(data=df, x='group', y='value')
isinstance(result, plt.Axes)  # True
```

**Key difference:**
- **Figure** = The whole canvas
- **Axes** = The plot itself (yes, confusing name - it's not just the axes!)

```python
# One figure with multiple axes
fig, (ax1, ax2) = plt.subplots(1, 2)  # 1 row, 2 columns

ax1.plot([1, 2, 3])
ax1.set_title('Plot 1')

ax2.plot([3, 2, 1])
ax2.set_title('Plot 2')

plt.show()
```

---

## Quick Type Check Cheatsheet

```python
# Numbers
type(5)              # <class 'int'>
type(5.0)            # <class 'float'>

# Text
type('hello')        # <class 'str'>

# Collections
type([1, 2, 3])      # <class 'list'>
type((1, 2, 3))      # <class 'tuple'>
type({1, 2, 3})      # <class 'set'>
type({'a': 1})       # <class 'dict'>

# Boolean
type(True)           # <class 'bool'>

# pandas
type(df['age'])      # <class 'pandas.core.series.Series'>
type(df)             # <class 'pandas.core.frame.DataFrame'>

# matplotlib
type(fig)            # <class 'matplotlib.figure.Figure'>
type(ax)             # <class 'matplotlib.axes._axes.Axes'>
```

---

## Common Type Confusions

### "Why is this a Series and not a DataFrame?"

```python
# Single bracket returns Series
df['age']          # Series

# Double bracket returns DataFrame  
df[['age']]        # DataFrame
```

### "What's the difference between a list and a Series?"

- **List**: Basic Python, no labels, fewer methods
- **Series**: pandas, has index labels, many statistical methods

```python
# List
my_list = [1, 2, 3]
my_list.mean()  # ERROR! Lists don't have mean()

# Series
my_series = pd.Series([1, 2, 3])
my_series.mean()  # 2.0 - Works!
```

### "When do I get Figure vs Axes?"

```python
# Returns Axes only
ax = sns.boxplot(data=df, x='group', y='value')
ax = df.plot()

# Returns both Figure and Axes
fig, ax = plt.subplots()

# To get figure from axes
fig = ax.get_figure()
```

---

## Additional Resources

- [Python Built-in Types Documentation](https://docs.python.org/3/library/stdtypes.html)
- [pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)
- [matplotlib API Reference](https://matplotlib.org/stable/api/index.html)
- [Python Syntax Quick Reference](python_syntax_guide.md)
- [Troubleshooting Common Errors](troubleshooting_errors.md)

