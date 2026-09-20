# Quality Checks

**Study area:** Rivers State, Nigeria
**Layers checked:** `Rivers_reprojectedUTM32` (boundary), `GRID3_NGA_health_facilities_v2_0` (health facilities, clipped to Rivers)
**Software:** QGIS

---

## 1. What is the coordinate system?

| Layer | CRS | Type |
|---|---|---|
| Rivers_reprojectedUTM32 (boundary) | **EPSG:32632, WGS 84 / UTM zone 32N** | Projected (metres) |
| GRID3_NGA_health_facilities_v2_0 | **EPSG:4326, WGS 84** (GRID3 default; confirm in Properties) | Geographic (degrees) |

- Project CRS is set to EPSG:32632.
- QGIS reprojects the facilities on the fly for display and clipping.
- **How to confirm:** right-click layer > **Properties** > **Information** > CRS.
- If distance or area analysis is needed, reproject the clipped facilities to EPSG:32632.

## 2. Are there null values you need?

**No.** None of the fields needed for this task contain null values.

- **How to verify:** open the Attribute Table and sort the key columns, or run **Processing Toolbox > Basic statistics for fields** and check the count of NULL values.
- **Quick filter:** select by expression `"fieldname" IS NULL` and confirm 0 features are selected.

## 3. Are there duplicate features?

- **How to check:** run **Processing Toolbox > Delete duplicate geometries** on the clipped facilities layer.
- Compare feature counts before and after. If the counts match, there are no duplicates.
- For attribute duplicates (same facility name repeated), use **Delete duplicates by attribute** on the facility name field.

| | Count |
|---|---|
| Features before | ______ |
| Features after | ______ |
| Duplicates found | ______ |

## 4. Does the geometry look valid?

- **How to check:** **Vector > Geometry Tools > Check Validity** (or Processing > **Check validity**), using the QGIS method.
- Run it on both the Rivers boundary and the facilities.
- Point layers are valid unless a geometry is empty or missing. Polygon layers are where errors appear (self-intersections, slivers, unclosed rings).
- If errors are found, run **Fix geometries** and use the fixed output.
- Visual check: the ward boundaries render cleanly, with no gaps, overlaps or spikes.

| Layer | Valid | Invalid |
|---|---|---|
| Rivers boundary | ______ | ______ |
| Health facilities | ______ | ______ |

## 5. Does the coverage include the study area?

- The Rivers State boundary is fully covered by the health facilities dataset. Facility points are spread across the state after the clip.
- **How to verify:**
  1. Right-click the clipped facilities > **Zoom to Layer** and confirm the points span the whole Rivers boundary.
  2. Check that no LGA is empty. Rivers has **23 LGAs**, so use **Count points in polygon** against the LGA layer and confirm none has a count of 0.
  3. Confirm no facilities were lost at the edge, by comparing the count from **Clip** with **Extract by location** (are within).

---

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Coordinate system | EPSG:32632 (boundary), EPSG:4326 (facilities) |
| 2 | Null values in needed fields | No |
| 3 | Duplicate features | To confirm with the tool above |
| 4 | Geometry validity | To confirm with the tool above |
| 5 | Coverage of study area | Covers Rivers State |
