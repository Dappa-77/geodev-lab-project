import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/wards.gpkg",layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file("data/processed/facilities.gpkg",layers='facilities').to_crs(epsg=32631)

wards["area_km2"]= wards.area/1e6
reach = facilities[["geometry"]].copy()
reach['geometry'] = reach.buffer(2000)
reach = reach.dissolve()

uncovered = gpd.overlay(wards,reach,how='difference')
uncovered['uncovered_km2'] = uncovered.area/1e6

gaps = uncovered[['ward_name','uncovered_km2']]

results = wards.merge(gaps,on='ward_name',how='left')
results['uncovered_km2'] = results['uncovered_km2'].fillna(0)
share = results['uncovered_km2']/results['area_km2'] *100
results['uncovered_pct'] = share.round(1)

print(results[['ward_name','area_km2','uncovered_km2','uncovered_pct']].round(2))

## STRETCH TASK

uncovered = uncovered[~uncovered.is_empty]  
print(uncovered)       
uncovered.to_file(
    "data/processed/coverage.gpkg",
    layer="uncovered_areas",
    driver="GPKG"
)


fig, ax = plt.subplots(figsize=(8, 8))
wards.plot(ax=ax, color="#eeeeee", edgecolor="grey", linewidth=0.8)
uncovered.plot(ax=ax, color="crimson", edgecolor="darkred", alpha=0.8)
facilities.plot(ax=ax, color="black", markersize=8)   # optional: show facilities

ax.set_title("Areas more than 2 km from a facility")
ax.set_axis_off()
for _, row in wards.iterrows():
    x, y = row.geometry.centroid.x, row.geometry.centroid.y
    ax.annotate(row["ward_name"], (x, y), ha="center", fontsize=8)
plt.savefig("month-03/week-11/uncovered_map.png", dpi=200, bbox_inches="tight")
plt.close()