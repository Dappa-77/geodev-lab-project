# Week 10: GeoPandas, layers as tables

## What this folder contains
- explore_pandas.py: first look at the ward population table 
- join_population.py: joins the population data to the ward polygons 
- facilities_map.png: map of health facilites by ward
- my_explore.py: loads my main vector layer (Obio/Akpor wards) and prints layers, shape, geometry types, CRS and bounds
- my_points.py: turns the health facilities CSV into a point layer, saves it to data/processed/ and plots it over the ward polygons
- my_join.py: cleans the ward names and joins the facilities data to the ward layer, printing the match count before and after cleaning
- my_map.py: draws one map of health facilities by ward in Obio/Akpor and saves it as a PNG

- README.md: this file

## How to run it
From the repository root:
uv run month-03/week-10/join_population.py
uv run month-03/week-10/my_join.py

## What I found in my data
Obio/Akpor has 17 wards, and the hospital data places 111 facilities across them. Obward 15 and Obward 11 have the most facilities (11 each), while Obward 1 has the fewest. The map shows that facilities cluster in the southern wards and are sparse in the northern wards. The layer's bounds sit where I expected for Obio/Akpor in Rivers State.

## What went wrong and how I fixed it
The ward names in the hospital data did not match the ward layer. The CSV used names like "Obio/Akpor 14", while my layer used "Obward 14", so the first join matched very few wards. The CSV also contained "Port Harcourt 1" and "Unknown" as ward values, which are not Obio/Akpor wards in my layer and did not match anything. I wrote a `clean_ward()` function that standardises every name to "Obward N", then used a spatial join on the facility coordinates to place the "Unknown" rows. The rows that still fell outside every ward (2 of 111) were excluded and are not in the counts.