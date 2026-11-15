from shapely.geometry import Polygon
from shapely.validation import explain_validity
import geopandas as gpd

obio_wards = gpd.read_file("mydata/ObioAkpor.gpkg",).to_crs(epsg = 32632)
print(type(obio_wards))


if obio_wards.is_valid.all():
    print("none")

else:
    obio_wards['geometry'] = obio_wards.make_valid()
    print('valid now;',obio_wards.is_valid.all())
    print("New type:",obio_wards.geom_type.iloc[0])


