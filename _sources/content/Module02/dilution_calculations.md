# Molarity Calculations

When collecting DNA/RNA from a sample it is important to measure the amount that you have.
This can be used for quality control on the sample preperation and for downstream experiments.
Since DNA, RNA, and protein absorb different wavelengths of light, one can use a spectrophotometer to measure absorbance and estimate the concentration.

Many molecular biology protocols depend on precise molecular ratios to function optimally. For example:

- **Ligation reactions** require specific molar ratios between vector and insert DNA (typically 1:3 to 1:10) to maximize successful cloning efficiency. Too little insert DNA results in self-ligated vectors, while too much can inhibit the ligase enzyme.

- **PCR amplification** benefits from balanced primer-to-template ratios. Excess template can lead to primer depletion and reduced amplification efficiency, while too little template may result in failed reactions or non-specific products.

- **Bacterial transformation** protocols often specify precise DNA amounts (typically 1-100 ng of plasmid DNA) to optimize transformation efficiency without overwhelming the cellular uptake machinery.

- **Next-Generation Sequencing (NGS)** platforms require extremely precise DNA loading concentrations. For example, Illumina sequencing requires libraries to be loaded at specific molarity ranges (typically 2-20 pM) to achieve optimal cluster density on the flow cell. Incorrect loading can result in over-clustering (poor sequence quality) or under-clustering (low data yield).

- **Diagnostic PCR assays** and **qPCR** protocols rely on precise template concentrations to ensure accurate quantification and reliable detection limits, particularly important for clinical applications where sensitivity and specificity are critical.

In this example, we'll focus on measuring the amount of DNA generate from a PCR.

## Measuring Concentration

Spectrophotometry works by measuring how much light is absorbed by molecules in solution.
When UV light passes through a sample containing nucleic acids, the aromatic bases (adenine, guanine, cytosine, thymine, and uracil) absorb light most strongly at 260 nm.
The amount of light absorbed is directly proportional to the concentration of nucleic acids present.

Nucleic acids absorb light at 260 nanometers.
This can be used to _weigh_ the amount of DNA in a sample like so:

$\text{Concentration (ng/μL)} = A_{260} \times \text{Conversion Factor}$

With the following standard conversion factors.

| Nucleic Acid | Conversion Factor |
|--------------|-------------------|
| DS-DNA       | 50 ng/uL          |
| SS-DNA       | 33 ng/uL          |
| SS-RNA       | 40 ng/uL          |

```{note}
:class: dropdown
**Quality Assessment: 260/280 Ratios**

Beyond concentration measurement, spectrophotometry provides valuable quality control information through absorbance ratios.
The 260/280 ratio is particularly important for assessing sample purity:

 - **Measure** both A₂₆₀ and A₂₈₀ absorbance values
 - **Ratio** the ratio by dividing A₂₆₀ by A₂₈₀  
   - Pure DNA: 260/280 ratio ≈ 1.8
   - Pure RNA: 260/280 ratio ≈ 2.0

**Troubleshoot** based on results:
- Low ratios (< 1.6): Indicates protein contamination, may require additional purification
- High ratios (> 2.2): Suggests organic solvent carryover or RNA degradation
- Ratios within expected ranges: Sample is suitable for downstream applications
```

{cite}`nebiocalculator`

### Example

Assume you've prepared PCR product and measured on the spectrophotometer.
This produces a double-stranded DNA product.
The device says that your $A_{260}$ absorbance is 1.1 units.
What is the concentration of your PCR product.

$\text{Concentration (ng/μL)} = A_{260} \times \text{Conversion Factor}$

$\text{Concentration (ng/μL)} = 1.1 \times 50$

$ 55 \text{(ng/μL)} $


## Calulating Molarity

Oftentimes when performing enzymatic reactions it is important to know the **number** of molecules per unit volume.
This is called the _molarity_ of a sample.
By controling the number of DNA molecules added to a sample we can ensure there are enough enzyme **molecules** to properly cataylze the reaction.

Since DNA fragments can be different lengths, we need to employ a conversion that calculates the weight of each molecule of DNA.
This will be specific to each experiment as different protocols will generate DNA fragments of different lengths.

### Example

In our system, we have a 250 basepair double-stranded piece of DNA and the next step requires adding precisely 500 femptomoles of DNA to our reaction.
How many uL of our PCR product should we add?

We can calculate how much each mole weighs using:

$250bp×660g/mol=165,000g/mol$

Using this, we can calculate the number of moles per μL in our sample using the 55 ng/μL concentration from our previous calculation:

$\text{Moles/μL} = \frac{\text{Mass/μL}}{\text{Molar Mass}} = \frac{55 \times 10^{-9}g/μL}{165,000g/mol}$

$\text{Moles/μL} = 3.33 \times 10^{-13} \, \text{mol/μL}$

3.33E-13 moles/μL is a valid answer, however, most protocols use femptomoles as the unit of choice.

$ 1 \text{mol}=10^{15} \text{femptomols} $

$\text{Molarity of the DNA sample} = 333 \, \text{fmols/μL}$

Therefore, to add 500 femptomoles of our DNA to a solution we would:

$  \frac{500 fmols}{333 \text{fmols/μL}} = 1.5 μL$

In the walkthrough and lab you will employ these techniques to determine the efficiency of different protocols.


## Extra Resources

Below are additional links to review unit conversion.

* Khan Academy's [Unit Conversions](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-measurement-and-data-2/imp-conversion-word-problems/v/multi-step-unit-conversion-examples)
* Bite Size Bio has a [DNA focused example](https://bitesizebio.com/20669/how-to-calculate-the-number-of-molecules-in-any-piece-of-dna/).
* New England Biosciences [Calculators](https://nebiocalculator.neb.com/#!/dsdnaamt) are a great in-lab resource.