# Month 1 Summary

## Question
Which settlements in Obio-Akpor Local Government Area have no paved road access within 2 km of a health facility?

## Operation and why
I worked in EPSG:32632 (WGS 84 / UTM zone 32N) so distances are in metres. I buffered the health facilities by 2 km (dissolved) and used Extract by location to split the settlements into those inside the buffer (near a facility) and those outside it (far). For the settlements inside the buffer, I used Join attributes by nearest against the paved roads to measure the distance to the nearest paved road, and flagged any settlement more than 200 m away.

I chose this because my question has two conditions: distance to a health facility, and access to a paved road. The buffer and location test handle the first, and the nearest-distance join handles the second. A settlement counts as unserved if it is outside the 2 km buffer, or inside it but more than 200 m from a paved road.

Two choices I made, which affect the result:
- OSM's surface tag was mostly empty, so I treated motorway, trunk, primary, secondary, tertiary and residential roads (and their link roads) as paved.
- I chose 200 m as the threshold for having road access.

Data: hospital points, OSM roads and OSM place points (settlements) downloaded with QuickOSM, and the Obio-Akpor LGA boundary. Roads and settlements were clipped to the LGA boundary.

## What I expected
Before running the analysis, I expected about 15 to 30 settlements inside the LGA and about 3 to 7 (10 to 25%) without access. I expected most to be in the north, the north-east and near the river in the south. I expected the dense central and western areas to be fully served, and only 0 to 3 settlements to fall outside the 2 km buffer.

## What I got
- Total settlements inside the LGA (T): 37
- Settlements within 2 km of a health facility (N): 37
- Settlements outside 2 km (F): 0
- Settlements within 200 m of a paved road: 37
- Settlements without paved road access (U): 0
- Largest distance to a paved road: 84.2 m (Rumu-Okoro-Odomey, nearest road residential). The next largest was 73.5 m (Rumuomasi). All 37 were under 100 m.

So no settlement in the data lacks paved road access within 2 km of a health facility.

## Checks
1. **Map:** the settlements, health facilities and paved roads are spread across the LGA, and every settlement sits inside the hospital buffer and near a road. There are no unserved points to show, which matches the table.
2. **Row count:** N + F = 37 + 0 = 37 = T, and served + unserved = 37 + 0. The total was higher than my expected 15 to 30.
3. **One feature by hand:** I took the settlement with the largest distance to a paved road (Rumu-Okoro-Odomey) and measured it to its nearest paved road with the Measure tool (Cartesian, metres). I got about 81.9 m, compared with 84.2 m in the attribute table. The 2 m difference comes from clicking by hand at map scale, so the table value is confirmed.
4. **Empty geometry:** I filtered for `$geometry IS NULL` and got 0 rows.

## What surprised me
- I expected a few unserved settlements and found none. The hospital layer is dense, so the 2 km buffers overlap and cover the whole LGA. Every settlement is also close to a mapped road.
- The count of 37 is higher than I expected, and the table suggests some are duplicates. Rumuomasi appears twice with the same ID, Eremo Ogbagoro, Eremo Ogbogoro and Eremogbogoro share one ID, and Rumu-Okoro and Rumuokoro share another. OSM often has several place points for one settlement, so 37 probably overcounts distinct settlements.
- Nearly all the nearest roads were residential, so the result depends on counting residential roads as paved. If residential roads were not counted, some settlements would probably fail.
- The place points are mostly in well-mapped parts of the LGA, so a null result may reflect the data rather than the real situation.

## Data I still need
- A more complete settlement layer, such as building footprints or a census settlement list, with duplicates removed.
- A reliable paved or unpaved surface attribute for roads, so I do not need to use road class as a proxy.
- Facility type or capacity, because a 2 km circle around a small clinic is not the same as access to a hospital.
- Travel distance along the road network, instead of straight-line distance, and hospitals just outside the LGA boundary that could serve border settlements.
