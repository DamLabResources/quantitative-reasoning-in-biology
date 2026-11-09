# Two styles of AI-assisted programming

Part 4 uses AI to write analysis code. The scientific rules do not change: name the observational unit, report effect before p, and keep a written claim tied to a table or figure. What changes is **who steers the next line of code**.

This part covers two styles. Module 11 practices the first; Module 12 practices the second.

## Natural-language programming (cell by cell)

You give **one instruction at a time** in plain English. The AI translates that instruction into code for a single cell. You run it, read the objects and plots, then write the next instruction.

You own the analysis path. You choose the order of steps, name the objects the next cell will need, and catch mistakes while they are still local.

**Useful when:**

- The recipe is already clear (filter → transform → test → summarize)
- You are learning a method and want each step visible
- You only want the AI to help with part of the analysis

## Agentic coding (goal-based, iterative)

You state a **broader scientific goal** and constraints (question, unit of analysis, assumptions, context). An agent proposes steps, writes code, runs it, and continues from the output. You refine the goal and reject bad turns; the agent manages most of the code.

You own long-range alignment: Is this still answering the question? Is the grain still correct? Would you defend this claim in a paper?

**Useful when:**

- The path is exploratory and many reasonable intermediate summaries exist
- The dataset is messy (timestamps, nested replicates, odd missingness) and you want help proposing the next check
- You can audit a short trail of steps faster than writing every cell yourself
- You are willing to stop the agent when it drifts or tests at the wrong level

## Cautions

Both styles fail the same way when science is sloppy: wrong unit of analysis, p-hunting across a long chat, or a conclusion that only exists in the prompt history. The notebook is the record, not the conversation.
