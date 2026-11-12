# Pandas date-time utilities

Actigraphy rows are timestamps. Pandas can parse them once and then extract calendar fields without string hacking.

## Parse once

```python
df['timestamp'] = pd.to_datetime(df['timestamp'])
```

After that, use the **`.dt`** accessor:

```python
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.day_name()
df['date'] = df['timestamp'].dt.date
```

## Two ways to aggregate in time

### `groupby` on extracted fields

Good when you want mean activity by person and hour, or by person and weekday:

```python
by_hour = (
    df.groupby(['person_id', 'group', 'hour'], as_index=False)['activity']
      .mean()
)
```

### `resample` on a DatetimeIndex

Good when one series is already indexed by time and you want regular bins (15 min, 1 H, 1 D):

```python
one = df.loc[df['person_id'] == 'control_1'].set_index('timestamp').sort_index()
hourly = one['activity'].resample('1h').mean()
```

`resample` needs a datetime index. Multi-person tables usually `groupby` person first, then resample inside each group (or use `groupby` + `Grouper`).

## Link

Official user guide: [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html)

## Unit-of-analysis warning

Hourly means still leave **many rows per person**. A t-test on all hourly rows treats hours as independent subjects and inflates *n*. Collapse to **one summary per person** (or a pre-registered person-day model) before the group comparison that answers the module question.
