import geopandas as gpd
import matplotlib.pyplot as plt


obio_wards = gpd.read_file("mydata/ObioAkpor.gpkg",).to_crs(epsg = 32632)
health = gpd.read_file("mydata/Hospital_in_obioakpor.gpkg").to_crs(epsg = 32632)

obio_wards["area_km2"]= obio_wards.area/1e6
reach = health[["geometry"]].copy()
reach['geometry'] = reach.buffer(2000)
reach = reach.dissolve()

uncovered = gpd.overlay(obio_wards,reach,how='difference')
uncovered['uncovered_km2'] = uncovered.area/1e6

gaps = uncovered[['wardname','uncovered_km2']]

results = obio_wards.merge(gaps,on='wardname',how='left')
results['uncovered_km2'] = results['uncovered_km2'].fillna(0)
share = results['uncovered_km2']/results['area_km2'] *100
results['uncovered_pct'] = share.round(1)

print(results[['wardname','area_km2','uncovered_km2','uncovered_pct']].round(2))



centres = obio_wards[["wardname","geometry"]].copy()
centres['geometry'] = centres.centroid

nearest = gpd.sjoin_nearest(
    centres,health[['facility_n','geometry']],how = 'left',distance_col = 'distance_m'
)

nearest['distance_km'] = (nearest['distance_m']/1000).round(2)
print(nearest[['wardname','facility_n','distance_km']].head(3))

## STRETCH TASK


uncovered_layer = uncovered[~uncovered.is_empty].copy()
print("this is the uncovered layer:")
print(uncovered_layer)
uncovered_layer.to_file(
    "data/processed/my_coverage.gpkg",
    layer="uncovered_areas",
    driver="GPKG"

)


fig, ax = plt.subplots(figsize=(10, 10))
obio_wards.plot(ax=ax, color="#eeeeee", edgecolor="grey", linewidth=0.8)
uncovered_layer.plot(ax=ax, color="crimson", edgecolor="darkred", alpha=0.8)
health.plot(ax=ax, color="black", markersize=8)

for _, row in obio_wards.iterrows():
    c = row.geometry.representative_point()
    ax.annotate(row["wardname"], (c.x, c.y), ha="center", fontsize=7)

ax.set_title("Obio-Akpor: areas more than 2 km from a health facility")
ax.set_axis_off()
plt.savefig("month-03/week-11/obio_akpor_uncovered_map.png", dpi=200, bbox_inches="tight")
plt.close()