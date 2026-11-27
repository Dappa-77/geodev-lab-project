# Week 13: Batch Processing with Logging

## Independent challenge

**Task:** Reproject every GeoPackage in a folder to UTM zone 31N (EPSG:32631) and save each result as a new GeoPackage.

**Script:** `my_batch.py`
**Outputs:** `my_batch_summary.csv` (one row per file) and `my_batch_run.log` (timestamped record of the run)

The script reads every `.gpkg` file in `mydata/`, reprojects it, and writes the result to `data/processed/mydata_utm/`. The input data is the Obio-Akpor LGA layers from my earlier GIS work: health facilities, hospitals, the LGA boundary and the joined wards layer.

## How to run

From the repository root:

```
uv run month-03/week-13/my_batch.py
```

## Results of the run

| Status  | Count |
|---------|-------|
| Done    | 4     |
| Skipped | 0     |
| Failed  | 1     |

Files found: 5 (4 real layers plus 1 deliberately broken file).

| File                       | Status | Features |
|----------------------------|--------|----------|
| Health_in_obioakpor.gpkg   | done   | 111      |
| Hospital_in_obioakpor.gpkg | done   | 111      |
| ObioAkpor.gpkg             | done   | 17       |
| wards_joined.gpkg          | done   | 17       |
| broken.gpkg                | failed | none     |

## What broke and what the log said

To test the error handling, I placed an empty file named `broken.gpkg` in the input folder. It has the right extension but contains no valid GeoPackage data.

The log recorded:

```
2026-11-27 15:10:42,318  ERROR  Failed on broken.gpkg: 'mydata\broken.gpkg' not recognized as being in a supported file format.
```

**Why it broke:** the file is empty, so geopandas could not open it as a GeoPackage and raised an error as soon as the script tried to read it.

**What the script did about it:** the `try`/`except` in `main()` caught the error, wrote it to the log, recorded the file as `failed` in the summary with no feature count, and carried on. The other four files were still processed. Without the `try`/`except`, one bad file would have stopped the whole batch.

I removed `broken.gpkg` from the data folder after the test.

## Other safeguards in the script

- A layer with no CRS raises a `ValueError` instead of guessing the projection, because a wrong guess would silently shift the data.
- A layer with no features raises a `ValueError`.
- Existing outputs are skipped unless `OVERWRITE = True`, so re-running the script does not redo finished work.