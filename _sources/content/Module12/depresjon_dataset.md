# Depresjon dataset and biological question

## What was measured

Participants wore a wrist **Actiwatch** that stored activity counts once per minute. The public DEPRESJON release includes:

- **23** people with unipolar or bipolar depression (`condition`)
- **32** controls (`control`)
- About **two weeks** of recording per person (exact length varies; see `days`)
- A timestamp and an activity count on each minute

Score fields are stored on those minute rows and repeat for a given person: `gender`, `age` (age range), `edu` (education), `inpatient`, `madrs1` and `madrs2`, plus related fields (`afftype`, `melanch`, `marriage`, `work`).

Each person was recorded on their own dates. A control file may fall in a different month than a condition file. Read each person on their own timeline, by hour and weekday, rather than by a shared calendar day.

Original collection: Berge / Fasmer group, Haukeland University Hospital (Bergen, Norway). Public packaging: Garcia-Ceja et al., MMSys 2018.

## What the study reported

The study these recordings come from reported lower daytime activity in depression than in controls, and a larger gap on weekends than on weekdays.

## Files in this module

`depresjon_minute.csv.gz` — one row per person-minute after trimming each recording to the first `days` listed for that person (the window used in the dataset paper). Columns include `person_id`, `group`, `timestamp`, `activity`, `days`, and the score fields above.

Rebuild with `python prepare_depresjon.py`. Terms: [LICENSE.md](LICENSE.md) (CC BY-NC 4.0; citation required).

## Question for the module

**In this table, is activity lower in the condition group than in controls, and does weekday versus weekend change the comparison?**

A minute is **not** the sample size. Neither is a single hour treated as an independent subject. The person is the unit: the same person contributes both weekday and weekend activity. Use hour-of-day and day-of-week summaries to see the pattern, then aggregate to the person before a test.

People do not share one weekly schedule. A person who is active on Monday will not look like a person whose active day is Tuesday, and a group average can blur that.

## Why this dataset

Many measurements sit inside each person. The Data Science Agent can propose plots and tests. You decide which summaries respect the design, and you interpret the figure.
