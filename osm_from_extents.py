# function for downloading osm data given extents

import subprocess
import csv

def dl_osm_from_extents(xmax, xmin, ymax, ymin):

    url = 'http://overpass-api.de/api/map?bbox=' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax)

    subprocess.call(["wget", url])

    temp_name = 'map?bbox=' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax)

    # rename to map.osm.xml
    subprocess.call(["mv", temp_name, "osrm/map.osm.xml"])

# e.g.

dl_osm_from_extents(-77.5,-78,46,45.5)


# ---------------------------

# alternative for downloading via coordinate extents in a .csv file

# # grabbing all blocks from csv and put into an array
# db = []
# with open('db.csv','r') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         header = row
#         break
#     for row in reader:
#         if row != header:
#             db.append(row)
#
# # print header for erf
# print header
#
# X = []
# Y = []
# for row in db:
#     X.append(float(row[0]))
#     Y.append(float(row[1]))
#
# print min(Y)
# print max(Y)
# print min(X)
# print max(X)
#
# # then grab the data, accordingly
# dl_osm_from_extents(max(X) + 0.02, min(X) - 0.02, max(Y) + 0.02, min(Y) - 0.02)

##########
