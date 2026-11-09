import re
import numpy as np
import pandas as pd
import geopandas as gpd

data = pd.read_csv('mydata/Hospital_in_obioakpor.csv')
wards = gpd.read_file("mydata/ObioAkpor.gpkg")

print(data.columns)
print(data['ward'].unique().tolist())


def clean_ward(name):
    """Standardise ward names to 'Obward N'. Returns NaN if it isn't an Obio/Akpor ward."""
    if pd.isna(name):
        return np.nan
    s = str(name).strip().lower()
    # only accept Obio/Akpor-style names; this drops 'Unknown' and 'Port Harcourt 1'
    m = re.match(r'^(obio\s*/?\s*akpor|obward)\s*(\d+)$', s)
    if not m:
        return np.nan
    return f"Obward {int(m.group(2))}"


# CSV / DataFrame
data['ward_clean'] = data['ward'].apply(clean_ward)       # use your CSV's ward column name

# QGIS layer (GeoDataFrame). In your attribute table the column is 'wardname'
wards['ward_clean'] = wards['wardname'].apply(clean_ward)


print(data.loc[data['ward_clean'].isna(), 'ward'].unique())    # rows that won't match
print(set(data['ward_clean'].dropna()) - set(wards['ward_clean']))   # should be empty
print(set(wards['ward_clean']) - set(data['ward_clean'].dropna()))   # wards with no CSV data

# one row per ward (count of facilities, as an example)
summary = data.groupby('ward_clean').size().reset_index(name='n_facilities')
merged = wards.merge(summary, on='ward_clean', how='left')
print(merged)
merged.to_file('mydata/wards_joined.gpkg', layer='wards_joined', driver='GPKG')