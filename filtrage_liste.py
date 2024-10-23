import math


# Filtrage de données en parcourant une liste
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
print(raw_data)

filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)