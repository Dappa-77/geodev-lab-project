# Week 12: Raster Inspection, NDWI and Zonal Statistics

Month 3 · Geospatial Python and Automation · GeoDev Lab Africa

This folder holds my independent challenge for Week 12, applied to my own project area.

## Data used

| Item | Detail |
|---|---|
| Source | USGS EarthExplorer (https://earthexplorer.usgs.gov/) |
| Satellite / product | Landsat 8 OLI/TIRS, Collection 2 Level-2 Surface Reflectance |
| Scene ID | `LC08_L2SP_188057_20240126_20240130_02_T1` |
| WRS-2 Path / Row | 188 / 057 |
| Acquisition date | 26 January 2024 |
| Processing date | 30 January 2024 |
| Collection / Tier | Collection 2, Tier 1 |
| Cloud cover | **[FILL IN: % from the EarthExplorer scene metadata]** |
| Bands used | `SR_B3` (Green) and `SR_B5` (NIR) |
| Boundary layer | **[FILL IN: name of your polygon file, e.g. my boundary shapefile/GeoJSON]** |

The rasters are not uploaded to this repository (excluded by `.gitignore`). See `data-notes.md` for where the data came from.

## Index chosen: NDWI

NDWI (water) = (Green - NIR) / (Green + NIR), which is bands 3 and 5 on Landsat 8.

Surface reflectance scale factor applied to both bands before computing the index:

```
reflectance = DN * 0.0000275 - 0.2
```

Pixels where Green + NIR = 0 were excluded to avoid division by zero.

## Scripts and outputs

| File | What it does |
|---|---|
| `my_inspect.py` | Prints the inspection checklist for my raster (CRS, size, resolution, bounds, nodata, dtype) and checks that width x resolution equals right minus left |
| `my_index.py` | Computes NDWI, prints the range and mean, and saves the result to `data/processed/` |
| `my_zonal.py` | Computes the mean NDWI per polygon in my boundary layer and saves a CSV in this folder |
| `my_map.png` | Map of NDWI with a colour bar |
## Inspection result



## Notes and limitations

- The scene was acquired in January (dry season), so water extent may differ from the rainy season.
- Haze or cloud in the scene can distort NDWI values. See the cloud cover figure above.
- Mean NDWI per polygon blends water and land pixels, so a large polygon with a small river can still show a low mean.


