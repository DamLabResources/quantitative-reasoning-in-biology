# Three styles of AI-assisted programming

Part 4 uses AI to write analysis code. The scientific rules do not change: name the observational unit, report effect before p, and keep a written claim tied to a table or figure. What changes is **how much of the next code the AI proposes**, and **who steers the analysis path**.

A code model on its own can outscore most beginners {cite:t}`finnieansley2022` and lands near the middle of a programming contest {cite:t}`li2022alphacode`. On a set of GitHub issues the best agent in the study resolved about 43% {cite:t}`jimenez2024swebench,zhang2025swebenchlive`. On course assignments, Copilot's best suggestion was correct about as a student solution, and the rest of its suggestions were correct less often {cite:t}`moradidakhel2023`. The speedups show up when a person still accepts or rejects the code and the task has a known end. Developers with Copilot finished one specified program about 56% faster, Google engineers about 21% faster on a single enterprise change, and in three companies Copilot users closed about 26% more pull requests per week, **with larger gains for less experienced developers** {cite}`peng2023copilot,paradis2024speed,cui2025field`. Beside a human partner on a short exercise, Copilot wrote more lines, and more of those lines were deleted afterward {cite:t}`imai2022`.

Analysis tasks with lighter coders land in the same place. Marketing and sales professionals with no programming jobs, reading plain-language accounts of ChatGPT analyses and warned that the model often errs, still missed safety-critical flaws, and some of those flaws were missed by everyone in the study {cite:t}`virk2025nonprogrammers`. Epidemiology students and staff who already knew the statistics, randomized to ChatGPT's code interpreter or to R or Stata with ChatGPT beside it, scored about the same (8.5 versus 9.4 out of 17) with the interpreter group finishing in 38 minutes rather than 45 for the side-by-side group. A *serious mistake* was present in 74% of answers with ChatGPT plus R or Stata and in **93% with the interpreter alone** {cite:t}`dhokotera2025genai`. In another study, analysts comfortable with code could still check an AI analysis by turning to the data tables once a step looked wrong {cite:t}`gu2024verify`.

The styles below follow from how the suggestion is used. When you already know the next step, the tool finishes the line. When you are unsure, it starts to choose the path, and students either steer it back to the assignment or drift from one wrong guess to the next {cite}`barke2023,prather2024`. Autocomplete and one cell at a time are the first case: you keep the recipe, run the cell, and reject a result that fails the printed check. An agent is the second case. The trials that found a speedup left a person in charge of what counted as done. Here that person checks the observational unit, the effect, and a claim they would sign.

## 1. AI-enhanced autocomplete

AI autocomplete uses the surrounding text and code to infer what you are likely to type next. That can be the rest of a line or a multiline “verse” of code. You stay in the editor: accept, edit, or ignore the suggestion, then keep typing.

This course has been subtly engineered so context clues in the notebooks steer autocomplete toward what you need next. The hope is that the autocomplete would help bridge the gap between your intent and the code you need to write. Markdown that summarizes the analysis so far, names next steps, and states overall goals helps the engine place the right suggestion. If you are coding outside of this course make it a habit to leave a short written trail of your results and intent. This will help your collaborators and future self understand your analysis; and it will let the autocomplete engine help effectively.

**Useful when:**

- You mostly know the code and want help finishing a line or block
- Variable names and recent cells already define the next move
- You want to stay in flow without switching into a chat or agent

`````{admonition} Tip
:class: tip

Steer autocomplete by writing a `#` comment that states what you want the code to do, then let the suggestion fill in below it.
`````

## 2. Natural-language programming (cell by cell)

You give **one instruction at a time** in plain English. The AI translates that instruction into code for a single cell. You run it, read the objects and plots, then write the next instruction.

You own the analysis path. You choose the order of steps, name the objects the next cell will need, and catch mistakes while they are still local. [Module 11](../Module11/Module11_book.md) practices this style.

**Useful when:**

- The recipe is already clear (filter → transform → test → summarize)
- You are learning a method and want each step visible
- Intermediate objects must stay under your control (`results`, `sig`, group sizes)
- A wrong step should not silently cascade into later tests

**Example:** In [Module 11](../Module11/Module11_book.md) you already know the destination—log2 TPM, Welch t-tests, FDR, then Enrichr. Each Colab prompt is one brick. If the filter cell is wrong, you fix that prompt before asking for fold changes.

## 3. Agentic coding (goal-based, iterative)

You state a **broader scientific goal** and constraints (question, unit of analysis, what must not be treated as *n*). An agent proposes steps, writes code, runs it, and continues from the output. You refine the goal and reject bad turns; the agent manages most of the code trail. [Module 12](../Module12/Module12_book.md) practices this style.

You own long-range alignment: Is this still answering the question? Is the grain still correct? Would you defend this claim in a paper?

**Useful when:**

- The path is exploratory and many reasonable intermediate summaries exist
- The dataset is messy (timestamps, nested replicates, odd missingness) and you want help proposing the next check
- You are willing to stop the agent when it drifts or tests at the wrong level
- **You can audit a short trail of steps faster than writing every cell yourself**

**Example:** In [Module 12](../Module12/Module12_book.md) the question is about daytime activity in depression vs controls **per person**, not per minute. Ask an agent to explore toward that claim, then reject any step that treats minutes as independent samples.

## How to choose

| Situation | Prefer |
| --- | --- |
| Finishing code you already know how to structure | AI-enhanced autocomplete |
| Known pipeline, teaching a method, tight object names | Natural-language, one cell at a time |
| Open exploration, agent proposes checks, you supervise goals and grain | Agentic coding |

All three fail the same way when science is sloppy: wrong unit of analysis, p-hunting across a long chat, or a conclusion that only exists in the prompt history. The notebook you produce is the record because it is deterministic, reproducible, sharable, verifiable, and auditable. Your chat history is not.
