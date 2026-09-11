# Data Notes — Week 2

## GRID3 NGA - Operational Wards v1.0 (ward boundaries)

- **Source and link:** GRID3, https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about
- **Version and date published:** v1.0, published December 9, 2020; data last updated September 4, 2025
- **Downloaded on:** September 2026
- **Licence and required citation:** CC BY 4.0 (https://creativecommons.org/licenses/by/4.0)
- **Format and size:** Feature Layer / GeoPackage (Nigeria-wide, 9,410 records)

1. **How many rows/features?** 9,410 nationwide; filtered down to 1 feature (Obward 17) for this project.
2. **What are the column names?** globalid, uniq_id, timestamp, editor, wardname, wardcode, lganame, lgacode, statename, statecode.
3. **What type is each column?** globalid, uniq_id, timestamp, editor, wardname, wardcode, lganame, lgacode, statename, statecode are all Text (string), except timestamp which is a Date field.
4. **Are there nulls?** No nulls found — all fields were populated for the Obward 17 record (wardname: Obward 17, wardcode: RVSRUM17, lganame: Obio/Akpor, statename: Rivers).
5. **What geometry type?** Polygon.
6. **Does the coverage look complete?** Yes — the ward boundary is present and aligns visually with the OpenStreetMap basemap and known neighbourhood names (e.g. Elelenwo) within it.

## OSM minor roads within Obward 17 (Obio-Akpor LGA, Rivers State)

- **Source and link:** OpenStreetMap, extracted via the QuickOSM plugin in QGIS
- **Version and date published:** Live OSM data (continuously updated); extracted for this project in September 2026
- **Downloaded on:** September 2026
- **Licence and required citation:** © OpenStreetMap contributors
- **Format and size:** GeoPackage (.gpkg)

1. **How many rows/features?** 1,232.
2. **What are the column names?** fid, full_id, osm_id, osm_type, toll, lit, covered, motorroad, noname, service, barrier, passenger_, substance, voltage, power, demolished, motor_vehi, foot, tunnel, access, name_ar, smoothness, horse, bicycle, GNS_id, GNS_dsg_st, GNS_dsg_co, waterway, source_dat, boundary, admin_leve, wikipedia, wikidata, operator, man_made, location, name_fr, addr_city, alt_name, junction, int_ref, int_name, maxspeed, usage, railway, gauge, electrifie, layer, constructi, bridge, destinatio, surface, ref, oneway, lanes, name, highway.
3. **What type is each column?** All Text (string), except fid which is Integer (64 bit).
4. **Are there nulls?** Yes, there are null values — most attribute columns are empty for the majority of features, with only a handful of fields (e.g. highway, oneway, sometimes name, surface, ref) consistently populated.
5. **What geometry type?** Line (MultiLineString).
6. **Does the coverage look complete?** No — there are obvious gaps when compared against the satellite basemap for Obward 17.
