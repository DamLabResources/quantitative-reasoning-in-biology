# Code generation vs agent-based exploration

Use this page as presentation notes for Module 12. The Part 4 overview of both styles is in [Two styles of AI-assisted programming](../part4/ai_programming_styles.md). Module 11 and Module 12 both involve AI, but the human role differs.

## Cell-level code generation (Module 11)

You write a **plain-English prompt for one cell**. Colab returns code. You run it, read the output, and write the next prompt.

- You choose the analysis path
- You name the objects (`results`, `sig_genes`)
- Failures are local: one bad cell, fix the prompt
- Good when the recipe is known (log2 → t-test → FDR → Enrichr)

## Data Science Agent (Module 12)

An **agent** proposes a sequence of steps, writes code, runs it, and continues from the result.

- The agent chooses intermediate plots and summaries
- You review the trail: Did it aggregate to the person? Did it peek at minutes as *n*?
- Failures can compound: an early wrong grain poisons later tests
- Good for open exploration when you can audit each step

## Same scientific rules either way

| Rule | Why |
| --- | --- |
| Name the observational unit | Minutes ≠ people |
| Prefer effect / overlap before p | Avoid p-hunting in long agent traces |
| Keep a written claim | The notebook is the record, not the chat |
| Cite the data license | Depresjon is CC BY-NC |

## How to supervise an agent

1. State the question and forbidden grains in the first prompt
2. After each major step, check `n` and the grain of the table
3. Reject steps that test at the wrong level
4. End with a short human-written conclusion tied to a specific table or figure
