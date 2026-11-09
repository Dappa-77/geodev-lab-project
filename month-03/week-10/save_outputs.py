import geopandas as gpd


wards = gpd.read_file("data/processed/wards.gpkg",layers='wards')
wards.to_file("data/processed/week10_outputs.gpkg",layer = "wards_copy")
wards.drop(columns='geometry').to_csv("month-03/wards_table.csv",index= False)
print(gpd.list_layers("data/processed/week10_outputs.gpkg"))