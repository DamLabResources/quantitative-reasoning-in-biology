# Troubleshooting Common Errors

This guide helps you understand and fix common Python and pandas errors you might encounter in this course.

## How to Read Error Messages

Python error messages follow a pattern. Here's an example:

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-5-abc123def456> in <module>
      1 # Select the age column
----> 2 data['Age']

KeyError: 'Age'
```

**Reading the error:**
1. **Error Type** (top): `KeyError` - tells you what went wrong
2. **Traceback** (middle): Shows which line caused the error (marked with `---->`)
3. **Error Message** (bottom): `'Age'` - gives specific details

The arrow (`---->`) points to the exact line that caused the problem.

## Common Error Types

### KeyError

**What it means:** You're trying to access a dictionary key or DataFrame column that doesn't exist.

**Common causes:**
```python
# ❌ Wrong column name (case sensitive!)
data['Age']  # Column is actually 'age' (lowercase)

# ❌ Typo in column name
data['ART_regimen']  # Column is actually 'ART'

# ❌ Column doesn't exist at all
data['nonexistent_column']
```

**How to fix:**
```python
# 1. Check available columns
print(data.columns)

# 2. Use the exact column name (case matters!)
data['age']  # ✅ CORRECT

# 3. For complex names, copy-paste from the columns list
print(data.columns.tolist())
```

**Real example from our course:**
```python
# ❌ WRONG
result = data['Processing_Domain_Z']

# ✅ CORRECT (check the actual column name)
print(data.columns)  # Shows: 'processing_domain_z'
result = data['processing_domain_z']
```

---

### TypeError

**What it means:** You're using an operation on the wrong type of data.

**Common causes:**

**Example 1: Using + on incompatible types**
```python
# ❌ Can't add string and number
age = '25' + 5  # TypeError: can only concatenate str (not "int") to str

# ✅ Convert to same type first
age = int('25') + 5  # Returns 30
age = '25' + str(5)  # Returns '255'
```

**Example 2: Wrong bracket type**
```python
# ❌ Using () instead of [] for indexing
data('age')  # TypeError: 'DataFrame' object is not callable

# ✅ Use square brackets
data['age']
```

**Example 3: Missing quotes on strings**
```python
# ❌ Treating variable as string
data[data['sex'] == Male]  # TypeError or NameError

# ✅ Add quotes for string values
data[data['sex'] == 'Male']
```

**How to fix:**
1. Check if you're using the right bracket type (`[]` vs `()`)
2. Ensure strings have quotes
3. Check data types: `type(variable)` or `data.dtypes`

---

### SyntaxError

**What it means:** Python can't understand your code because of a typo or missing punctuation.

**Common causes:**

**Missing closing bracket/parenthesis**
```python
# ❌ Missing closing bracket
subset = data[data['age'] > 30
# SyntaxError: unexpected EOF while parsing

# ✅ Add the closing bracket
subset = data[data['age'] > 30]
```

**Missing comma**
```python
# ❌ Missing comma between list items
columns = ['age' 'sex' 'education']
# SyntaxError: invalid syntax

# ✅ Add commas
columns = ['age', 'sex', 'education']
```

**Mismatched quotes**
```python
# ❌ Starting with " but ending with '
name = "Alice'
# SyntaxError: EOL while scanning string literal

# ✅ Match your quotes
name = "Alice"
name = 'Alice'  # Both work, just be consistent
```

**How to fix:**
1. Look at the line indicated by the arrow (`---->`)
2. Count your brackets: each `(` needs a `)`, each `[` needs a `]`
3. Check for missing commas in lists
4. Ensure quotes match (both single `'` or both double `"`)

---

### AttributeError

**What it means:** You're trying to use a method or attribute that doesn't exist for that object type.

**Common causes:**

**Wrong method name (typo)**
```python
# ❌ Method doesn't exist (typo: groupby vs groupBy)
data.groupBy('ART')
# AttributeError: 'DataFrame' object has no attribute 'groupBy'

# ✅ Correct method name
data.groupby('ART')
```

**Using DataFrame method on Series (or vice versa)**
```python
# ❌ .query() only works on DataFrames, not Series
ages = data['age']
young_ages = ages.query('age < 30')
# AttributeError: 'Series' object has no attribute 'query'

# ✅ Filter the DataFrame first, then select column
young_data = data.query('age < 30')
young_ages = young_data['age']

# OR use boolean indexing
young_ages = data[data['age'] < 30]['age']
```

**Calling a result instead of a method**
```python
# ❌ Missing parentheses to call the method
data_copy = data.copy
# This assigns the function itself, not the result

# ✅ Add () to call the method
data_copy = data.copy()
```

**How to fix:**
1. Check spelling of method names (case matters!)
2. Verify you're using a DataFrame vs Series method correctly
3. Don't forget parentheses `()` when calling methods
4. Check the documentation: `help(data.groupby)` or online docs

---

### NameError

**What it means:** You're using a variable or function name that Python doesn't recognize.

**Common causes:**

**Typo in variable name**
```python
# ❌ Variable name misspelled
my_data = pd.read_csv('file.csv')
result = mydata['age']
# NameError: name 'mydata' is not defined

# ✅ Use exact variable name
result = my_data['age']
```

**Forgot to import a library**
```python
# ❌ Using pd before importing pandas
data = pd.read_csv('file.csv')
# NameError: name 'pd' is not defined

# ✅ Import first
import pandas as pd
data = pd.read_csv('file.csv')
```

**Variable not defined yet**
```python
# ❌ Using variable before creating it
print(result)
result = data['age'].mean()
# NameError: name 'result' is not defined

# ✅ Create variable first
result = data['age'].mean()
print(result)
```

**How to fix:**
1. Check spelling of variable names
2. Ensure you've run all necessary cells (especially imports!)
3. Make sure you've run cells in order (top to bottom)
4. In Colab, use `Runtime` → `Restart and Run All` to start fresh

---

### IndexError

**What it means:** You're trying to access a position in a list or array that doesn't exist.

**Common causes:**

```python
# ❌ List only has 3 items (indices 0, 1, 2)
my_list = ['a', 'b', 'c']
print(my_list[3])
# IndexError: list index out of range

# ✅ Use valid indices
print(my_list[2])  # Last item
print(my_list[-1])  # Also gets last item
```

**How to fix:**
1. Remember Python uses 0-based indexing (first item is `[0]`)
2. Check the length: `len(my_list)`
3. Use negative indices to count from the end: `[-1]` is the last item

---

### ValueError

**What it means:** You passed the right type of argument, but an invalid value.

**Common causes:**

**Wrong value in function argument**
```python
# ❌ 'median' is not a valid method for normality test
pg.normality(data['age'], method='median')
# ValueError: method must be 'normaltest' or 'jarque_bera'

# ✅ Use a valid method
pg.normality(data['age'], method='normaltest')
```

**Incompatible array shapes**
```python
# ❌ Arrays have different lengths
x = [1, 2, 3]
y = [1, 2, 3, 4, 5]
plt.plot(x, y)
# ValueError: x and y must have same first dimension

# ✅ Make sure arrays match
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
plt.plot(x, y)
```

**How to fix:**
1. Read the error message carefully - it often tells you valid options
2. Check function documentation: `help(function_name)`
3. Verify data dimensions match when required

---

## Troubleshooting Workflow

When you encounter an error, follow these steps:

1. **Read the error type** - What kind of error is it?
2. **Find the line** - Look for the arrow `---->` in the traceback
3. **Check the error message** - What specific detail does it give?
4. **Consult this guide** - Find your error type above
5. **Try the fixes** - Work through the suggested solutions
6. **Still stuck?**
   - Print intermediate values: `print(variable)`
   - Check types: `type(variable)` or `data.dtypes`
   - Review earlier cells - did they all run successfully?
   - Restart and run all: `Runtime` → `Restart and Run All`
   - Ask for help in office hours or discussion board

## Prevention Tips

1. **Run cells in order** - Start from the top and work down
2. **Check column names** - Use `data.columns` frequently
3. **Use tab completion** - Start typing and press Tab to autocomplete
4. **Match the examples** - Follow the pattern from walkthroughs
5. **Test as you go** - Don't write lots of code before running it
6. **Read error messages** - They often tell you exactly what's wrong

## Additional Resources

- [Python Syntax Quick Reference](python_syntax_guide.md) - For syntax questions
- Official pandas documentation: https://pandas.pydata.org/docs/

