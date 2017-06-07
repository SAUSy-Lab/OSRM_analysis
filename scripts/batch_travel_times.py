# batch compute travel times between OD pairs


import csv
import requests
import polyline
import time
import json

start_time = time.time()

in_table = "in_table.csv"

fail_list = []

# function to compute trip
def walk_trip(id,x1,y1,x2,y2):

    route_url = "http://127.0.0.1:5000/route/v1/driving/" + str(x1) + "," + str(y1) + ";" + str(x2) + "," + str(y2) + "?overview=false"

    page = requests.get(route_url)

    route = json.loads(page.content)

    duration = route['routes'][0]['legs'][0]["duration"]

    return duration


# loop over each input file, do the function
f = 0
out_array = [["HHkey", "time"]]
with open(in_table, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        if row[1] != "home_x":

            try:
                d = walk_trip(row[0],row[1],row[2],row[3],row[4]) / 60
                out_row = [row[0], d]
                out_array.append(out_row)
                print d
            except:
                f += 1

# write the data to file
with open("out/times_drive.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for row in out_array:
        print row
        writer.writerow(row)

print "moooooooo"
