import gmplot
import webbrowser
import pandas as pd
from sodapy import Socrata
import geocoder
import gmaps
import googlemaps
from datetime import datetime
from scipy.spatial import distance

apikey = 'AIzaSyDegglaigtldDPa1GlX6FiKqJg2HVKZcO8'

# real time data using socrata
client = Socrata("data.melbourne.vic.gov.au", None)
results = client.get("dtpv-d4pf", limit=2000)

# convert data to pandas_data
results_df = pd.DataFrame.from_records(results)

# latitude list, longitude list
lats, lons, status, lats2, lons2, = [], [], [], [], []
coords = []
temp, temp2 = [], []

# store coordinator data to each value
for index, row in results_df.iterrows():
    # print(row)
    status.append(row[6])
    lats.append(float(row[2]))
    lons.append(float(row[4]))

# find the available parking space
for i in range(0, len(status)):
    if status[i] == "Unoccupied":
        lats2.append(lats[i])
        lons2.append(lons[i])

# my location
myloc = geocoder.ip('me')
cur, cur2 = myloc.lat, myloc.lng

# place map Melbourne
gmap = gmplot.GoogleMapPlotter(cur, cur2, 13)

# Scatter Drawing. parking spot
gmap.scatter(lats2, lons2, '#FF0000', size=20, marker=False)

# marker about current location
gmap.marker(cur, cur2, '#FFFF00', title="my location")

# Make coordinator list
for i in range(0, len(lats2)):
    temp.append(lats2[i])
    temp2.append(lons2[i])
    coords.append([temp[i], temp2[i]])

loc = [[cur, cur2], ]

# calculate euclidean distance
e_dst = distance.cdist(loc, coords, "euclidean")
e_dst = e_dst.tolist()
idx, m_val, i = 0, 1000000, 0

# find coordinator of the closest parking spot
for dst in e_dst[0]:
    if dst < m_val:
        m_val = dst
        idx = i
    i += 1

# marking the closest parking spot
gmap.marker(coords[idx][0], coords[idx][1], '#FF00FF', title="The nearest parking spot")

# plotting root
dis_lat = [coords[idx][0], cur]
dis_lng = [coords[idx][1], cur2]

gmap.plot(dis_lat, dis_lng, '#FFFFFF', edge_width=3)

# Draw
gmap.draw("parking_map.html")
# Run Browser
webbrowser.open_new("parking_map.html")

# gmaps.configure(api_key=apikey)
# fig = gmaps.figure()
# layer = gmaps.directions.Directions(loc[0], coords[idx], mode='car')
# fig.add_layer(layer)
# fig

gmaps2 = googlemaps.Client(key=apikey)

now = datetime.now()
directions_result = gmaps2.directions(loc[0], coords[idx], mode="driving", avoid="ferries", departure_time=now)

print(directions_result[0]['legs'][0]['duration']['text'])
