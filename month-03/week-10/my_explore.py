import geopandas as gpd

Obio_akpor = gpd.read_file("mydata/ObioAkpor.gpkg")
print(Obio_akpor.head(3))
print("Rows and columns:",Obio_akpor.shape)
print(Obio_akpor.geom_type.value_counts())
print("CRS:",Obio_akpor.crs)
print("Bounds:",Obio_akpor.total_bounds)