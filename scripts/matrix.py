import csv
import requests
import time
import json
import polyline


points = []

# grab points from a test.csv file - just grab, x, y, and a unique ID
with open("test.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    n = 0
    for row in reader:
        # print row
        points.append([row['X'],row['Y'],row['ID']])
        n += 1


point_list = []

for row in points:

    point_list.append((float(row[1]),float(row[0])))

# print '--------------'
# print point_list

line = polyline.encode(point_list, 5)

# print line

url = 'http://localhost:5000/table/v1/driving/polyline(' + line + ')'

print url

page = requests.get(url)
data = json.loads(page.content)

print data

out_matrix = []
for row in data['durations']:
    out_matrix.append(row)
    print row

# can then output out_matrix to csv if needed. should also code in the ID of points

#[0, 41963.3, 18704.9, 39579]
#[41963.3, 0, 30362.4, 6756.8]
#[18704.9, 30362.4, 0, 27978.1]
#[39579, 6756.8, 27978.1, 0]







#
