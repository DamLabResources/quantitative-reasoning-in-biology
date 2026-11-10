# Module 12: Actigraphy and the Data Science Agent

## Overview

This week you explore continuous wrist actigraphy from the Depresjon study: people with depression and healthy controls, recorded at one-minute resolution for many days. The statistical question is person-level, not minute-level. You will use Colab’s **Data Science Agent** to explore aggregations across time windows.

## Learning resources

- [Depresjon dataset and question](depresjon_dataset.md)
- [Pandas date-time utilities](pandas_datetime.md)
- [Three styles of AI-assisted programming](../part4/ai_programming_styles.md)
- [Code generation vs agent exploration](code_generation_vs_agents.md)
- License and citation: [LICENSE.md](LICENSE.md)

### Having trouble with syntax or errors?

- [Python Syntax Quick Reference](../misc/python_syntax_guide.md)
- [Troubleshooting Common Errors](../misc/troubleshooting_errors.md)

## Learning activities

### Read

Review the three pages above before opening the notebook.

### Participate: Walkthrough / Lab

Open the skeletal Module 12 notebook. The setup cell and data load are filled in. Continue with the Data Science Agent following the person-level question on the dataset page. Prompts from the recorded session will be posted on Canvas after class.

## Getting help

- **Office Hours**: Thursday 8 PM at the course Zoom link
- **Discussion Board**: Conceptual questions about units of analysis and time aggregation

## Tips for success

1. State the observational unit before any test (person, or person-day—not minute)
2. Use pandas datetime tools to build hour-of-day and weekday features
3. Review every agent step; do not paste a conclusion you cannot defend
