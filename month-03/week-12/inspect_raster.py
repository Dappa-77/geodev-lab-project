import rasterio

with rasterio.open('data/raw/dem.tif') as src:
    print("width x height:", src.width,"x", src.height)
    print("Bands:", src.count)
    print("Data types:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("NoData:", src.nodata)
    print("Transform:")
    print(src.transform)
    
    
    
    