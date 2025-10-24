# Python Syntax Quick Reference

This page provides a quick reference for Python and pandas syntax commonly used in this course.

## Bracket Types: When to Use What

Python uses three types of brackets, each with a specific purpose:

| Bracket Type | Symbol | Primary Uses | Examples |
|--------------|--------|--------------|----------|
| **Square brackets** | `[ ]` | Lists, indexing, selecting columns | `my_list = [1, 2, 3]`<br>`df['column_name']`<br>`df.loc[0:5]` |
| **Parentheses** | `( )` | Function calls, tuples, grouping | `print('Hello')`<br>`my_tuple = (1, 2, 3)`<br>`(x + y) * z` |
| **Curly braces** | `{ }` | Dictionaries, sets | `my_dict = {'key': 'value'}`<br>`my_set = {1, 2, 3}` |

### Common Mistakes

```python
# ❌ WRONG: Using parentheses for column selection
df('column_name')  # This won't work!

# ✅ CORRECT: Use square brackets
df['column_name']

# ❌ WRONG: Using square brackets for function calls
print['Hello']  # This won't work!

# ✅ CORRECT: Use parentheses
print('Hello')
```

## DataFrame Column Selection

```python
# Select a single column (returns a Series)
ages = data['age']

# Select multiple columns (returns a DataFrame)
subset = data[['age', 'sex', 'education']]
# Note the double square brackets: outer for indexing, inner for the list

# Select columns by condition
numeric_cols = data[data.columns[data.dtypes == 'float64']]
```

## DataFrame Indexing: `.loc[]` vs `.iloc[]`

| Method | What it uses | Example |
|--------|--------------|---------|
| `.loc[]` | Labels/names | `df.loc[0:5, 'column_name']`<br>`df.loc[df['age'] > 30]` |
| `.iloc[]` | Integer positions | `df.iloc[0:5, 0:3]`<br>`df.iloc[0, 1]` |

### Key Difference
```python
# .loc[] uses LABELS (inclusive on both ends)
df.loc[0:5]  # Includes rows 0, 1, 2, 3, 4, AND 5

# .iloc[] uses INTEGER POSITIONS (exclusive on the end)
df.iloc[0:5]  # Includes rows 0, 1, 2, 3, 4 (NOT 5)
```



## Spacing and Formatting

### Spaces DON'T Matter (Mostly)
```python
# These are all equivalent:
data['age']
data[ 'age' ]
data  [  'age'  ]

# Function arguments with spaces
print('Hello', 'World')
print( 'Hello' , 'World' )
```

### Commas DO Matter
```python
# ❌ WRONG: Missing comma
df[['age' 'sex']]  # This will cause an error!

# ✅ CORRECT: Comma separates items in a list
df[['age', 'sex']]

# ❌ WRONG: Extra comma at the end (in some contexts)
my_list = [1, 2, 3,]  # Works but not recommended

# ✅ CORRECT: No trailing comma
my_list = [1, 2, 3]
```

### Quotes: Single vs Double
```python
# Both work the same for strings
name1 = 'Alice'
name2 = "Alice"

# Use the opposite quote type for nested quotes
message = "She said 'Hello'"
message = 'She said "Hello"'

# Or use escape characters
message = 'She said \'Hello\''
```

## Common String Operations

```python
# Column names are strings
column_name = 'age'
data[column_name]  # Same as data['age']

# String values need quotes
data[data['sex'] == 'Male']  # ✅ CORRECT

data[data['sex'] == Male]  # ❌ WRONG: Male without quotes is a variable
```

## Method Chaining

```python
# You can chain multiple operations
result = (data
          .query('age > 30')
          .groupby('ART')
          ['visuospatial_domain_z']
          .mean())

# Same as:
temp1 = data.query('age > 30')
temp2 = temp1.groupby('ART')
temp3 = temp2['visuospatial_domain_z']
result = temp3.mean()
```

## Quick Troubleshooting Checklist

When you encounter an error, check:

1. ✅ Are you using the right bracket type?
2. ✅ Do you have matching opening and closing brackets?
3. ✅ Are all your commas in the right places?
4. ✅ Are strings surrounded by quotes?
5. ✅ Are you using `.loc[]` or `.iloc[]` correctly?
6. ✅ Do column names match exactly (including capitalization)?

## Resources

- **[Python Types Reference](python_types_reference.md)** - Learn about common types (int, str, list, Series, DataFrame, Axes)
- **[Troubleshooting Common Errors](troubleshooting_errors.md)** - Understand and fix Python errors
- [Official pandas documentation](https://pandas.pydata.org/docs/)
- [Python official tutorial](https://docs.python.org/3/tutorial/)

