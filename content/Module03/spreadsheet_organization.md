# Spreadsheet Organization

Organizing data *before* loading it into DataFrames is a critical Step 0.
As data-scientists, we can consider the *form* and *shape* of the data file.

This book only concerns itself with _tabular_ data.
While other forms of data such are important in biology such a phylogenti

## Data Form

The *form* of the data refers to how it is stored within a spreadsheet.


Haphazard Form
Data is not in a strict table format but instead organized loosely across cells, often making it difficult to parse programmatically.

markdown
Copy code
| Cell A1: "Gene Name"    | Cell B2: "BRCA1"       |
| Cell A3: "Expression"   | Cell B4: "High"        |
| Cell D1: "Gene Name"    | Cell D2: "TP53"        |
| Cell D3: "Expression"   | Cell D4: "Moderate"    |
Issues: This format lacks structure, making automated data extraction error-prone. It's equivalent to no normalization.

Non-Normalized (Unnormalized Form)
Data is stored in a single table but contains redundant or nested data.

markdown
Copy code
| Gene      | Sample IDs             | Expression Levels |
|-----------|------------------------|-------------------|
| BRCA1     | S1, S2, S3             | High, Low, High   |
| TP53      | S1, S2, S3             | Moderate, Low, High |
Issues:

Repetition of information within cells.
Difficult to filter or query specific combinations of data.
Doesn't separate repeated data into distinct rows.
First Normal Form (1NF)
Data is organized into a table where each cell contains a single value, and each row is unique.

markdown
Copy code
| Gene      | Sample ID | Expression Level |
|-----------|-----------|------------------|
| BRCA1     | S1        | High             |
| BRCA1     | S2        | Low              |
| BRCA1     | S3        | High             |
| TP53      | S1        | Moderate         |
| TP53      | S2        | Low              |
| TP53      | S3        | High             |
Advantages: Eliminates multi-valued attributes; data is easier to query and process programmatically.

