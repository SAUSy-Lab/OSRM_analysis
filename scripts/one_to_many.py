# computes travel times from one origin to many destinations using OSRM

# will need to have OSRM running somewhere before running this script

# originally setup for the Toronto region

import csv
import time
import requests
import json

# test coordinate for possible origin location
test = [[-79.0396866,43.8522169]]

# inputting list of coordinates and unique IDs for potetntial origins of home locations
in_home_data = []
with open("people/geocoded.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    n = 0
    q = 0
    for row in reader:
        if row['X'] != '':
            q += 1
            x = float(row['X'])
            y = float(row['Y'])
            in_home_data.append([row['ID'],x,y])

print len(in_home_data)

# grab destination points and code to list
in_destination_data = []
with open("taz/TAZ_point_coords.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    n = 0
    q = 0
    for row in reader:
        q += 1
        x = float(row['X'])
        y = float(row['Y'])
        in_destination_data.append([row['GTA06'],x,y])
        # if q > 10:
        #     break

print len(in_destination_data)


# get list of destination ids
dids = []
for row in in_destination_data:
    dids.append(row[0])


# function for one-to-many - input origin X, origin Y, and list of destinations
def row_request(ox,oy,destinations):

    # grab string of all the coordinates - for plugging into OSRM url
    coord_str = str(ox) + ',' + str(oy) + ';'
    for row in destinations:
        coord_str = coord_str + str(row[1]) + ',' + str(row[2]) + ';'
    coord_str = coord_str[:-1]

    # grab list of destinations IDs for URL string
    distr = ''
    di = 1
    while di <= len(destinations):
        distr = distr + str(di) + ';'
        di += 1
    distr = distr[:-1]

    # setting up the url to send
    url = 'http://localhost:5000/table/v1/walking/' + coord_str + '?sources=0&destinations=' + distr

    
    # sending and recieving the data
    page = requests.get(url)
    data = json.loads(page.content)

    # print length for testing
    print len(data['durations']) # should be 1
    print len(data['durations'][0]) # should be = len(destinations)
    
    # return the data as a row
    return data['durations'][0]



# do this for a bunch of origins if needed = essentially an OD matrix
out_rows = []
for person in in_home_data:
    tt = row_request(person[1],person[2],in_destination_data)
    tt = [person[0]] + tt
    out_rows.append(tt)

# write to csv file
with open("test.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id"] + dids)
    for p in out_rows:
        writer.writerow(p)


# # #
# ! #
# # #
