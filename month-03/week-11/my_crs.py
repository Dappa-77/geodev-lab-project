import geopandas as gpd

obio_wards = gpd.read_file("mydata/ObioAkpor.gpkg",)

print("CRS:",obio_wards.crs)


print("Suggested UTM:",obio_wards.estimate_utm_crs())

obio_wards_utm =obio_wards.to_crs(epsg = 32632)

obio_wards_utm["area_km2"] = obio_wards_utm.area / 10**6

print(obio_wards_utm.columns)

print(obio_wards_utm[['wardname','area_km2']].head(3))

print("Obio Akpor total:", round(obio_wards_utm["area_km2"].sum(),1),"km2")