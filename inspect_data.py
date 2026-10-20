import csv

# with open("wards.csv",encoding = "utf-8-sig") as f:
#     reader = csv.reader(f)
#     rows = list(reader)

# print(f"Number of rows: {len(rows)}")
# print(f"Number of columns: {len(rows[0])}")

# with open("wards.csv",encoding = "utf-8-sig") as f:
    
#     rows = list(csv.DictReader(f))



# values = []
# for row in rows:
#     value = float(row['area_km2'])
#     values.append(value)

# print('smallest area:', min(values))
# print('largest area:', max(values))
# print("count", len(values) )

# with open("wards.csv",encoding = "utf-8-sig") as f:
    
#     rows = list(csv.DictReader(f))
# values = []
# for row in rows:
#     raw = row['area_km2'].strip()
#     if raw == '':
#         continue
#     values.append(float(raw))

# print('smallest area:', min(values))
# print('largest area:', max(values))
# print("count", len(values) )

def inspect_column(filename,column):
    with open("wards.csv",encoding = "utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == '':
            continue
        values.append(float(raw))

    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }


results = inspect_column("wards.csv","area_km2")
print(results)

area_result = inspect_column("wards.csv","area_km2")
pop_result = inspect_column("wards.csv","population")

print(f"Area: {area_result}")
print(f"Population: {pop_result}")