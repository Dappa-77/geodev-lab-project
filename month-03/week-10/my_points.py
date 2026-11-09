import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
table = pd.read_csv("mydata/Hospital_in_obioakpor.csv")
print(table.head(3))

health_centers = gpd.GeoDataFrame(
    table,
    geometry = gpd.points_from_xy(table['longitude'],table['latitude']),
    crs ='EPSG:4326'
)
print(health_centers.head(3))
print(health_centers.crs)

health_centers.to_file('mydata/Health_in_obioakpor.gpkg',layer = 'health_centers')
print("Saved",len(health_centers),"health_centers")


Obio_akpor = gpd.read_file("mydata/ObioAkpor.gpkg")
health_centers = gpd.read_file("mydata/Health_in_obioakpor.gpkg",layers='health_centers')

fig,ax = plt.subplots(figsize=(7,8) )
Obio_akpor.plot(ax=ax,color = '#E6F2F3',edgecolor="#037EBE")
health_centers.plot(ax=ax,color="#094923",markersize=18)
ax.set_title("Health Centers in ObioAkpor")
ax.set_axis_off()

fig.savefig("month-03/week-10/my_map.png",dpi=150,bbox_inches = 'tight')
print('Map saved')