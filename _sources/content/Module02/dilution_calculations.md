# Molarity Calculations

When collecting DNA/RNA from a sample it is important to measure the amount that you have.
In biology labs, this is typically done by measuring the absorbance of light at specific wavelengths.

## Calculating Concentration

Nucleic acids absorb light at 260 nanometers.
This can be used to _weigh_ the amount of DNA in a sample like so:

$\text{Concentration (ng/μL)} = A_{260} \times \text{Conversion Factor}$

With the following standard conversion factors.

| Nucleic Acid | Conversion Factor |
|--------------|-------------------|
| DS-DNA       | 50 ng/uL          |
| SS-DNA       | 33 ng/uL          |
| SS-RNA       | 40 ng/uL          |

{cite}`nebiocalculator`

## Calulating Molarity

Oftentimes when performing enzymatic reactions it is important to know the **number** of molecules per unit volume.
This is called the _molarity_ of a sample.
By controling the number of DNA molecules added to a sample we can ensure they are enough enzyme **molecules** to properly cataylze the reaction.

Since DNA fragments can be different lengths, we need to employ a conversion that calculates the weight of each molecule of DNA.
This will be specific to each experiment as different protocols will generate DNA fragments of different lengths.

Assume we have a 250 basepair double-stranded piece of DNA and we want to add 25 femptomoles of DNA to our reaction.

We can calculate how much each mole weighs using:

$250bp×660g/mol=165,000g/mol$

Using this, we can calculate the number of moles per μL in our sample:

$\text{Moles/μL} = \frac{\text{Mass/μL}}{\text{Molar Mass}} = \frac{100 \times 10^{-12}}{165,000}$

$\text{Moles/μL} = 6.06 \times 10^{-16} \, \text{mol/μL}$

6.06E-16 moles/μL is a valid answer, however, most protocols use femptomoles as the unit of choice.

$ 1 \text{mol}=10^{15} \text{femptomols} $

$\text{Molarity of the DNA sample} = 6.06 \, \text{fmols/μL}$

Therefore, to add 25 femptomoles of our DNA to a solution we would:

$  \frac{25 μL}{6.06 \text{fmols/μL}} = 4.1 μL$

In the walkthrough and lab you will employ these techniques to determine the efficiency of different protocols.


## Extra Resources

Below are additional links to review unit conversion.

* Khan Academy's [Unit Conversions](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-measurement-and-data-2/imp-conversion-word-problems/v/multi-step-unit-conversion-examples)
* Bite Size Bio has a [DNA focused example](https://bitesizebio.com/20669/how-to-calculate-the-number-of-molecules-in-any-piece-of-dna/).
* New England Biosciences [Calculators](https://nebiocalculator.neb.com/#!/dsdnaamt) are a great in-lab resource.