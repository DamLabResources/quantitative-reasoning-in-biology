# Spreadsheet Organization

Organizing data *before* loading it into DataFrames is a critical Step 0.
As data-scientists, we can consider the *form* and *shape* of the data file.

This book only concerns itself with _tabular_ data.
While other forms of data such are important in biology such a phylogenti

## Data Form

In the early 1970's the computer scientist Edgar F. Codd developed a classification system for data tables {cite}`codd1970relational`.
While he developed these to describe relational databases they are also important for spreadsheet style databases.

### Haphazard Form

While not directly described by Codd, the _haphazard form_ is a form I find often in biology labs.
Data is not in a strict table format but instead organized loosely across cells, often making it difficult to parse programmatically.

| A            | B           |
|--------------|-------------|
| Gene Name    | BRCA1       |
| Expression   | High        |
| Gene Name    | TP53        |
| Expression   | Moderate    |

Issues:
* This format lacks structure, making automated data extraction error-prone.
* It's equivalent to no normalization.

### Non-Normalized (Unnormalized Form)

Data is stored in a single table but contains redundant or nested data.

| Gene      | Sample IDs             | Expression Levels |
|-----------|------------------------|-------------------|
| BRCA1     | S1, S2, S3             | High, Low, High   |
| TP53      | S1, S2, S3             | Moderate, Low, High |

Issues:
* Repetition of information within cells.
* Difficult to filter or query specific combinations of data.
* Doesn't separate repeated data into distinct rows.


### First Normal Form (1NF)

Data is organized into a table where each cell contains a single value, and each row is unique.

| Gene      | Sample ID | Expression Level |
|-----------|-----------|------------------|
| BRCA1     | S1        | High             |
| BRCA1     | S2        | Low              |
| BRCA1     | S3        | High             |
| TP53      | S1        | Moderate         |
| TP53      | S2        | Low              |
| TP53      | S3        | High             |

Advantages:
* Eliminates multi-valued attributes
* data is easier to query and process programmatically.

`````{admonition} Goal
:class: tip
This is the ideal format for Pandas DataFrames.
`````


### Even more forms

Codd described additional normalization schemes:

* UNF: Unnormalized form
* 1NF: First normal form
* 2NF: Second normal form
* 3NF: Third normal form
* EKNF: Elementary key normal form
* BCNF: Boyce–Codd normal form
* 4NF: Fourth normal form
* ETNF: Essential tuple normal form
* 5NF: Fifth normal form
* DKNF: Domain-key normal form
* 6NF: Sixth normal form

But these are more relavant to relational databases and are outside the scope of this course.

## Data Shape

There are two data shapes, wide and long.
These two formats will be covered in greater depth in Module 4 with `pd.pivot_table` and `pd.melt`.

### Wide Format

In wide format, each subject's repeated measurements (e.g., blood pressure at different time points) are stored in separate columns.

| Subject_ID | BP_Time_0 | BP_Time_1 | BP_Time_2 |
|------------|-----------|-----------|-----------|
| 001        | 120       | 125       | 130       |
| 002        | 110       | 115       | 120       |
| 003        | 130       | 135       | 140       |


### Long Format

In long format, each measurement is stored as a separate row, with additional columns identifying the subject and the time point.

| Subject_ID | Time_Point | Blood_Pressure |
|------------|------------|----------------|
| 001        | 0          | 120            |
| 001        | 1          | 125            |
| 001        | 2          | 130            |
| 002        | 0          | 110            |
| 002        | 1          | 115            |
| 002        | 2          | 120            |
| 003        | 0          | 130            |
| 003        | 1          | 135            |
| 003        | 2          | 140            |


