# import csv
# with open("places_ibnorth.csv", encoding='utf-8') as f:
#   reader = csv.DictReader(f)
#    rows = list(reader)

# values = []
# for row in rows:
#    raw = row['area_km2'] . strip()
#    if raw=="":
#        continue
#    values.append(float(raw))
# print("Smallest:", min(values))
# print("Largest:", max(values))
# print("count:", len(values))

def inspect_column(filename, column_name):
    import csv
    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column_name].strip()
        if raw == "":

            continue
        values.append(float(raw))

    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }

area_result = inspect_column("places_ibnorth.csv", "area_km2")
population_result = inspect_column("places_ibnorth.csv", "population")

print("Area:", area_result)
print("Population:", population_result)
