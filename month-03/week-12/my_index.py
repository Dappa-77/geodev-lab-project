







import numpy as np
import rasterio


folder = "mydata/"
scene = 'LC08_L2SP_188057_20240126_20240130_02_T1'

with rasterio.open(folder + scene + '_SR_B3.TIF') as src:
    green_raw = src.read(1).astype('float32')
    profile = src.profile

with rasterio.open(folder + scene + '_SR_B5.TIF') as src:
    nir_raw = src.read(1).astype('float32')

valid = (green_raw >= 7273) & (green_raw <= 43636) & (nir_raw >= 7273) & (nir_raw <= 43636)

green = green_raw * 0.0000275 - 0.2
nir = nir_raw * 0.0000275 - 0.2

ndvi = np.full(green.shape, -9999, dtype='float32')
total = green + nir
ok = valid & (total != 0)
ndvi[ok] = (nir[ok] - green[ok]) / total[ok]

low = round(float(ndvi[ok].min()), 3)
high = round(float(ndvi[ok].max()), 3)

print("NDVI range:", low, "to", high)
print("mean NDVI:", round(float(ndvi[ok].mean()), 3))

profile.update(dtype = 'float32', count = 1, nodata = -9999)
with rasterio.open('data/processed/my_ndvi.tif', 'w', **profile) as dst:
    dst.write(ndvi, 1)

print('Saved data/processed/my_ndvi.tif')


