import rasterio

datapath = 'data/raw/dem.tif'

with rasterio.open(datapath) as src:
    print("width x height:", src.width,"x", src.height)
    print("Bands:", src.count)
    print("Data types:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("NoData:", src.nodata)
    print("Transform:")
    print(src.transform)
    
    