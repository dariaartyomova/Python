import json
import csv
import os

with (open("Sample-employee-JSON-data.json", 'r') as j):
    data = json.load(j)
    name = list(data.keys())[0]
    f = os.path.splitext("Sample-employee-JSON-data.json")[0] + '-' + name + '.csv'

with open(f, 'w', newline='') as c:
    w = csv.writer(c)
    title = list(data[name][0].keys())
    w.writerow(title)
    for i in data[name]:
        w.writerow([i[j] for j in title])






