import csv

def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def clean_values (rows, column):
    values= []
    for row in rows:
        cell= row.get(column)
        if cell is None:
            continue
        raw = cell.strip().replace(",", "")
        if raw == "":
            continue
        try:
            values.append(float(raw))
        except ValueError:
            print(f"skipping non-numeric value for column '{column}': {raw!r}")
            continue
    return values


def summarise(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values),
    }
    
def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report

report = summarise_all("places_ibnorth.csv", ["area_km2", "population"])

for column, stats in report.items():
    print(column, "->", stats)
