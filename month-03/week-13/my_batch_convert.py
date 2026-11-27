"""
Reproject every GeoPackage in a folder to UTM zone 31N and save each as a GeoPackage.

Run from the root of your repository:
    uv run month-03/week-13/my_batch.py
"""
import logging
import time
from pathlib import Path

import geopandas as gpd
import pandas as pd

# ---- Settings ----
INPUT_FOLDER = Path("mydata")
OUTPUT_FOLDER = Path("data/processed/mydata_utm")
SUMMARY_FILE = Path("month-03/week-13/my_batch_summary.csv")
LOG_FILE = Path("month-03/week-13/my_batch_run.log")
WORKING_CRS = "EPSG:32631"
OVERWRITE = False

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)
logging.getLogger("pyogrio").setLevel(logging.WARNING)


def load_and_reproject(gpkg_path):
    """Read one layer and return it in WORKING_CRS."""
    layer = gpd.read_file(gpkg_path)
    if layer.crs is None:
        # Deliberate raise: we cannot guess the CRS safely
        raise ValueError("layer has no CRS defined, cannot reproject safely")
    if layer.empty:
        raise ValueError("layer has no features")
    return layer.to_crs(WORKING_CRS)


def process_one(gpkg_path):
    """Reproject one layer and save it, skipping existing outputs."""
    out_path = OUTPUT_FOLDER / f"{gpkg_path.stem}.gpkg"
    if out_path.exists() and not OVERWRITE:
        logging.info("Skipping %s, output already exists", gpkg_path.name)
        return {"file": gpkg_path.name, "status": "skipped", "features": None}
    layer = load_and_reproject(gpkg_path)
    layer.to_file(out_path, layer=gpkg_path.stem)
    logging.info("Reprojected %s: %d features", gpkg_path.name, len(layer))
    return {"file": gpkg_path.name, "status": "done", "features": len(layer)}


def main():
    start = time.perf_counter()
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
    results = []
    for gpkg_path in sorted(INPUT_FOLDER.glob("*.gpkg")):
        try:
            results.append(process_one(gpkg_path))
        except Exception as error:
            logging.error("Failed on %s: %s", gpkg_path.name, error)
            results.append(
                {"file": gpkg_path.name, "status": "failed", "features": None}
            )
    summary = pd.DataFrame(results)
    if not summary.empty:
        summary["features"] = summary["features"].astype("Int64")
    summary.to_csv(SUMMARY_FILE, index=False)
    elapsed = time.perf_counter() - start
    logging.info("Finished %d files in %.1f seconds", len(results), elapsed)
    print(summary)


if __name__ == "__main__":
    main()
