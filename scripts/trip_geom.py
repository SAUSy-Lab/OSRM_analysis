# script for batch computing the geometries and travel attributes of shortest-path trees

import csv
import requests
import polyline
import time
import json

start_time = time.time()

fail_list = []

def route_to_geojson(x1,y1,x2,y2,dbuid):

    route_url = "http://127.0.0.1:5000/route/v1/driving/" + str(x1) + "," + str(y1) + ";" + str(x2) + "," + str(y2) + "?steps=false&geometries=geojson&overview=full"

    print route_url

    page = requests.get(route_url)

    route = json.loads(page.content)

    duration = route['routes'][0]['legs'][0]["duration"]

    print duration

    geometry = route['routes'][0]["geometry"]

    geojson = {
        "type": "FeatureCollection","features": [
        {
          "type": "Feature",
          "properties": {
            "duration": duration,
            "DAUID": dbuid
          },
          "geometry": geometry
        }
      ]
    }

    return geojson

    #mapmatch_url

with open('db.csv') as csvfile:

    # read in csv of destination points
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:

        try:

            # origin
            o_lat = 43.65187
            o_lon = -79.38220

            # destination
            d_lat = row["Y"]
            d_lon = row["X"]

            #url
            dbuid = row["dbuid"]
            geojson = route_to_geojson(o_lon,o_lat,d_lon,d_lat,dbuid)

            with open("geojsons_car/" + dbuid + ".geojson", 'w') as fatty_mcgoo:
                json.dump(geojson, fatty_mcgoo)

            print i
            print time.time() - start_time
            print "===================="

        except:

            print "fail!"
            print "===================="
            fail_list.append(row["dbuid"])

        i += 1
