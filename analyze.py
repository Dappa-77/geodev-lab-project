with open("wards.csv") as f:
    lines = f.readlines()



# for line in lines:
#     print(line.strip())

# for line in lines[1:]:
    
#     parts = line.strip().split(",")
#     ward = parts[0]
#     area = parts[1]
#     print(f"{ward} has area of {area}")

for line in lines[1:]:
    
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    if area_km2 >9:
        size = 'large'
    else:
        size = 'small'

    print(f'{ward} is {size}')


