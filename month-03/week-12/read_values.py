import rasterio
import numpy as np

with rasterio.open('data/raw/dem.tif') as src:
    elevation = src.read(1)
    print('Array shape:', elevation.shape)
    print("smallest value:", elevation.min())

    elevation = src.read(1, masked=True)
    print("smallest real value:", round(float(elevation.min()), 1))
    print("largest real value:", round(float(elevation.max()), 1))
    print("mean value:", round(float(elevation.mean()), 1))
    print('Nodata cells:',int(elevation.mask.sum()))