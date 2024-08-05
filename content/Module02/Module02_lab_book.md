# Lab

Remember, all labs are due at 11:59 PM (Philadelphia time) on the Sunday of each instructional week.

## Introduction

In this lab, we will delve into the exciting world of viral sample preparation for nanopore sequencing for COIVD-19 sequencing.
Specifically, we will be comparing the yield of two different RT-PCR methods: the Paragon system and the PacBio system.

Before we can sequence our samples, we need to make sure that we have a sufficient amount of DNA to work with.
This means calculating the appropriate dilutions of our samples to ensure that we have enough material to generate accurate and reliable results.

The Paragon system uses over 200 pairs of overlapping PCR primers that generate DNA fragments that are, on average, 285 basepairs long.
On the other hand, the PacBio system uses 35 overlapping fragments that have an average length of 2200 bp.
It will be interesting to see which method produces a higher yield of DNA and is more efficient in preparing our samples for sequencing.

Get ready to dive into some math and use Python to compare these two RT-PCR methods!

## Learning Objectives

By the end of this activity, you will be able to:

 - Apply basic math in Python to summarize an experimental result.
 - Create f-strings to display dynamic results.
 - Compare and contrast the Nanopore and PacBio systems in terms of sample preparation for nCov2 sequencing.

# Protocol Evaluation

In the COVID sequencing lab we often have to evaluate multiple techniques for preparing viral samples for sequencing.
There are *many* aspects to this comparison, but one important one is the yield of the reaction that prepares DNA for sequencing.
This reaction is called an RT-PCR reaction because it _reverse-transcribes_ the nCov2 RNA into DNA through a _polymerase chain reaction_.

Currently, our lab uses a system with over 200 pairs of overlapping PCR primers that generate DNA fragments that are, on average, **285 basepairs** long.
We'll call this the _Paragon_ system.
Short RT-PCR fragments are ideal when dealing with degraded RNA because it allows for the amplification of even shredded RNA.
However, because no fragment is longer than ~300bp it is difficult to tell whether a mutation in one gene is 'linked' with a mutation in another gene.

So, we are exploring another technique, which we'll call the _PacBio_ system.
This system uses 35 overlapping fragments that have an average length of **2200 bp**.
These longer fragments help with understanding the linkage between more distant locations but are more difficult to run on degraded samples.

In this lab, you will work through a basic exercise in evaluating the yield of the _Paragon_ and _PacBio_ systems.

## Q1: Extract the relevant information from the text above

|               |    |
| --------------|----|
| Points        | 2  |
| Public Checks | 2  |
| Hidden Tests  | 0  |

_Points:_ 2


```python
# It is often useful to define all of your variables at the beginning.
# It is helpful to include units using '#' to keep track of your calculations

dna_weight = 650  # g/mole/bp

# bp
paragon_amplicon_length = ...
pacbio_amplicon_length = ...
```


```python
grader.check("q1_amp_length")
```

## Q2: Calculate the molecular weight of each template

In this lab, we are comparing the yield of two different RT-PCR methods for preparing viral samples for nanopore sequencing.
In order to accurately compare the yield of each method, it is important to know the molecular weight of the templates being used.
Therefore, as a part of this lab, we need to calculate the molecular weight of each template.
This will allow us to accurately compare the yield of each method and understand how the different characteristics of each method may impact the overall results.

|               |    |
| --------------|----|
| Points        | 2  |
| Public Checks | 4  |
| Hidden Tests  | 0  |

_Feeling stuck?_

Try doing it on **paper** first.

_Points:_ 4


```python
paragon_template_weight = ...
pacbio_template_weight = ...
```


```python
# Complete the cell above before running this one
print(f'The Paragon templates weigh {paragon_template_weight} g/mole')
print(f'The PacBio templates weigh {pacbio_template_weight} g/mole')
```


```python
grader.check("q2_mol_weight")
```

In order to investigate the impact of degradation on the yield of each protocol, you will examine two samples.
One sample has been freshly isolated and the other has been left at room temperature for 72 hours before preparation.
We then ran each sample according to the manufacturer's guidelines.

We obtained the following results after quantification of **15 ul** of final volume.

sample | Fresh | Degraded
-------|-------|---------
Paragon| 21.4 ng/ul  | 19.3 ng/ul
PacBio | 38.1 ng/ul | 7.4 ng/ul

## Q3: What is the _molarity_ of each _Paragon_ sample?

|               |    |
| --------------|----|
| Points        | 4  |
| Public Checks | 4  |
| Hidden Tests  | 2  |

_Feeling stuck?_

Try doing it on **paper** first.

A typical molarity for this protocol is between 50 and 500 fmols/ul.

_Points:_ 4


```python
# Add variables to hold the concentration of each sample

# Answer in fmoles/ul
paragon_fresh_molarity = ...
paragon_degraded_molarity = ...
```


```python
# If the cell above is correct, this will print the results.
print(f'The fresh Paragon-prepped sample has a concentration of {paragon_fresh_molarity:0.1f} fmoles/ul')
print(f'The degraded Paragon-prepped sample has a concentration of {paragon_degraded_molarity:0.1f} fmoles/ul')
```


```python
grader.check("q3_molarity")
```

## Q4: What is the yield of each _PacBio_ sample?

Now, let's calculate the yield of the fresh and degraded PacBio samples.
The yield is the total amount of DNA produced in the reaction (as measured in femptomoles).
This information is important because it allows us to compare the efficiency of the PacBio system in both fresh and degraded samples and determine whether it is a suitable method for our purposes.

_Points:_ 5


```python
# Add variables to hold the concentration of each sample in ng/ul
```


```python
# Calculate the molarity of each sample

pacbio_fresh_molarity = ...
pacbio_degraded_molarity = ...
```


```python
print(f'The fresh PacBio-prepped sample had a molarity of {pacbio_fresh_molarity:0.1f} fmoles/ul')
print(f'The degraded PacBio-prepped sample had a molarity of {pacbio_degraded_molarity:0.1f} fmoles/ul')
```


```python
# Calculate the total vield

pacbio_fresh_yield = ...
pacbio_degraded_yield = ...
```


```python
print(f'The fresh PacBio-prepped sample had a yield of {pacbio_fresh_yield:0.1f} fmoles')
print(f'The degraded PacBio-prepped sample has a yield of {pacbio_degraded_yield:0.1f} fmoles')
```


```python
grader.check("q4_dna_yield")
```

## Q5: Which samples are _usable_?

In order to determine which samples are suitable for use in the sequencing protocol, you must first determine if they have sufficient concentration of DNA.
As stated in the protocol, you need to provide 200 fmoles of DNA in 10 ul of dH20.
Based on the yield data that you calculated for the fresh and degraded PacBio and Paragon samples, you will need to determine which samples have a concentration of DNA that meets or exceeds this requirement.
In other words, you will need to determine which samples are usable for the sequencing protocol based on their DNA concentration.

|               |    |
| --------------|----|
| Points        | 6  |
| Public Checks | 1  |
| Hidden Tests  | 4  |

_Points:_ 6


```python
# Do the necessary calculations in this cell or the create more above.
# Remember, you can use variables that you have calculated in cells before.
# Finally, write a set of formatted print statements that describe the volume of DNA required for each reaction.
```


```python
# put a 'yes' or 'no' for each sample

paragon_fresh_usable = ...
paragon_degraded_usable = ...

pacbio_fresh_usable = ...
pacbio_degraded_usable = ...
```


```python
grader.check("q5_usable_samples")
```

# Conclusion

Congratulations on completing this lab! You have successfully compared the yield of two different RT-PCR methods for preparing viral samples for genomic sequencing.
You have determined that the Nanopore system is ideal for degraded samples due to its shorter PCR fragments, while the PacBio system is better for fresher samples and is able to produce longer sequencing fragments.
This is just the beginning of your journey with Python and data analysis.
Keep up the great work as we continue to expand on these techniques and explore more complicated results in future assignments.

--------------------------------------------

## Submission

Check:
 - That all tables and graphs are rendered properly.
 - Code completes without errors by using `Restart & Run All`.
 - All checks **pass**.
 - Excess code cells and print statments have been removed to create a _clean_ submission.

Remember, as this is a lab, there are hidden tests that you will be evaluated against.
Just because all checks pass does not mean everything is correct.
Double-check your work!

Then save the notebook and the `File` -> `Download` -> `Download .ipynb`. Upload this file to BBLearn.
