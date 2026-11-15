# Week 11: CRS checks and spatial operations

## Study area and question

Obio-Akpor LGA, Rivers State. Which parts of each ward are more than 2 km from a health facility?

## CRS used

```python
epsg = 32632
```

I used **EPSG:32632 (WGS 84 / UTM zone 32N)**. Obio-Akpor (Port Harcourt) is at about 7°E longitude, which falls inside UTM zone 32N (6°E to 12°E). Unlike geographic CRS such as EPSG:4326, which measures in degrees, UTM is measured in metres. That makes areas in km² and the 2000 m buffer correct. Both the wards and the health facilities were reprojected to this same CRS with `to_crs(epsg=32632)` before any buffering, overlay, join or area calculation.

## Method

1. Buffered every health facility by 2 km and dissolved the circles into one shape (`reach`).
2. Used `gpd.overlay(..., how="difference")` to keep the part of each ward not covered by `reach` (`uncovered`).
3. Merged the uncovered area back onto all wards, filled missing values with 0, and calculated the uncovered percentage.
4. Used `sjoin_nearest` to find the distance from each ward centroid to its nearest facility.
5. Saved the uncovered areas as a layer in `data/processed/coverage.gpkg` and mapped them over the wards in `month-03/week-11/uncovered_map.png`.

## Limitation of my method

The 2 km buffer measures straight-line distance, not the distance people actually travel. Roads, rivers, creeks, railways and traffic can make a facility that looks "covered" on the map much further away in real travel time, so the uncovered areas here are likely an underestimate of the true access gap. The buffer also treats every facility as equal, ignoring differences in size, services and capacity, and it depends on the facility list being complete: any hospital or clinic missing from the dataset will make a ward look less covered than it really is. Finally, the ward centroid used in the nearest-facility step may not sit where most residents live. Network distance along roads would give a more realistic result.
