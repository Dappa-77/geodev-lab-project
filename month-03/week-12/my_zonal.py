


import geopandas as gpd
import rasterio
import numpy as np
from rasterio.mask import mask

with rasterio.open('data/processed/my_ndvi.tif') as src:
    wards = gpd.read_file('mydata/ObioAkpor.gpkg').to_crs(src.crs)
    means = []
    for geom in wards.geometry:
        cells,_ = mask(src,[geom], crop = True, filled = False)
        means.append(float(cells.mean()))


wards['mean_ndvi'] = np.round(means,3)
print(wards[['wardname','mean_ndvi']])



