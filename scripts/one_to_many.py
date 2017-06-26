
import csv
import time
import requests
import polyline
import json
import threading

test = [[-79.0396866,43.8522169]]

# inputting the coordinates and unique IDs
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

# printing the length of how many to compute
print len(in_home_data) # should be 57

# grab destination points
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



def row_request(ox,oy,destinations):

    coord_str = str(ox) + ',' + str(oy) + ';'
    for row in destinations:
        coord_str = coord_str + str(row[1]) + ',' + str(row[2]) + ';'
    coord_str = coord_str[:-1]

    distr = ''
    di = 1
    while di <= len(destinations):
        distr = distr + str(di) + ';'
        di += 1
    distr = distr[:-1]


    url = 'http://localhost:5000/table/v1/walking/' + coord_str + '?sources=0&destinations=' + distr

    #
    # print url

    # sending and recieving

    page = requests.get(url)
    data = json.loads(page.content)
    # # print data['durations']
    # print "meow"
    print len(data['durations'])
    # print "meow"
    print len(data['durations'][0])

    return data['durations'][0]
    # # print data['durations'][0][0],data['durations'][1][0],data['durations'][2][0]


    # return data['durations']


out_rows = []

for person in in_home_data:

    tt = row_request(person[1],person[2],in_destination_data)

    tt = [person[0]] + tt

    out_rows.append(tt)


with open("test.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id"] + dids)
    for p in out_rows:
        writer.writerow(p)




# # #
# ! #
# # #
