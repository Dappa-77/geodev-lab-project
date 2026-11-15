import geopandas as gpd



obio_wards = gpd.read_file("mydata/ObioAkpor.gpkg",).to_crs(epsg = 32632)
health = gpd.read_file("mydata/Hospital_in_obioakpor.gpkg").to_crs(epsg = 32632)

#buffer
reach = health.copy()
reach['geometry'] = health.buffer(2000)
print("Buffered",len(reach),"Hea;th")

print(f"this is obio_ward column: {obio_wards.columns}")

print(f"this is health column: {health.columns}")



joined = gpd.sjoin(
    health,obio_wards[['wardname','geometry']],how = 'inner',predicate = 'within'
)

print(joined.head(3))

counts = joined.groupby('wardname').size().reset_index(name='health_count').reset_index()
print(counts.head(3))
wards = obio_wards.merge(counts,on='wardname',how='left')
wards['health_count'] = wards['health_count'].fillna(0).astype(int)

print(wards[['wardname','health_count']].head(3))
print("Total counted",wards["health_count"].sum(), 'of',len(health))