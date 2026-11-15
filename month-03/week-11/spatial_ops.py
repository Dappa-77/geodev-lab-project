import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg",layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file("data/processed/facilities.gpkg",layers='facilities').to_crs(epsg=32631)

#buffer
reach = facilities.copy()
reach['geometry'] = facilities.buffer(2000)
print("Buffered",len(reach),"facilities")

joined = gpd.sjoin(
    facilities,wards[['ward_name','geometry']],how = 'inner',predicate = 'within'
)

print(joined.head(3))

counts = joined.groupby('ward_name').size().reset_index(name='facility_count').reset_index()
print(counts.head(3))
wards = wards.merge(counts,on='ward_name',how='left')
wards['facility_count'] = wards['facility_count'].fillna(0).astype(int)

print(wards[['ward_name','facility_count']].head(3))
print("Total counted",wards["facility_count"].sum(), 'of',len(facilities))