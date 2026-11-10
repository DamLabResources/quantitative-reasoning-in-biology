# Depresjon dataset and biological question

## What was measured

Participants wore a wrist **Actiwatch** that stored activity counts once per minute. The public DEPRESJON release includes:

- **23** people with unipolar or bipolar depression (`condition`)
- **32** controls (`control`)
- About **two weeks** of recording per person (exact length varies; see `days` in the score table)
- Clinical scores including **MADRS** at the start and end of the recording window

Original collection: Berge / Fasmer group, Haukeland University Hospital (Bergen, Norway). Public packaging: Garcia-Ceja et al., MMSys 2018.

## Files in this module

`depresjon_minute.csv.gz` — one row per person-minute after trimming each recording to the first `days` listed for that person (the window used in the dataset paper). Columns include `person_id`, `group`, `timestamp`, `activity`, and score fields (`madrs1`, `madrs2`, age band, sex, …).

Rebuild with `python prepare_depresjon.py`. Terms: [LICENSE.md](LICENSE.md) (CC BY-NC 4.0; citation required).

## Question for the module

**Among these wrist recordings, do people with depression have lower daytime activity than controls when activity is summarized per person?**

A minute is **not** the sample size. Neither is a single hour treated as an independent subject. Aggregate first (for example mean daytime activity per person), then compare groups. You may also explore hour-of-day profiles and weekday versus weekend patterns, but any hypothesis test should state the observational unit explicitly.

## Why this dataset

It forces the same replicate logic you practiced earlier: many measurements nested inside people. The Data Science Agent can propose many plots; you decide which summaries respect the design.
