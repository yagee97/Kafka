import sys
import requests
import time
import matplotlib.pyplot as plt
import statistics
from pymongo import MongoClient
import datetime

latrobe_bundoora = 'http://api.openweathermap.org/data/2.5/weather?zip=3086,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
monash_clayton = 'http://api.openweathermap.org/data/2.5/weather?zip=3800,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
monash_caulfield = 'http://api.openweathermap.org/data/2.5/weather?zip=3145,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'

# make a request to the collect the dat
res_bundoora = requests.get(latrobe_bundoora)
res_clayton = requests.get(monash_clayton)
res_caulfield = requests.get(monash_caulfield)

# get dta as json format
data_bundoora = res_bundoora.json()
data_clayton = res_clayton.json()
data_caulfield = res_caulfield.json()

# collect the temperature data
temperature_bundoora = data_bundoora['main']['temp']
temperature_clayton = data_clayton['main']['temp']
temperature_caulfield = data_caulfield['main']['temp']

# 3 variables for each temperature data and xAxis,yAxis
clayton, caulfield, bundoora, x, y = [], [], [], [], []

# plotting setting
plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
plt.title('Hot Weather HomeWork')
ax = fig.add_subplot(111)
fig.show()
client = MongoClient('localhost:27017')
collection = client.campus.temp

db = client.campus

temps = db.temps

print(db.collection_names())
i = 0
count = 0
flag = 0
now = datetime.datetime.now()
while flag != 1:
    i += 1
    count += 1
    print('Temparature of Bundoora Campus==' + str(temperature_bundoora))
    print('Temparature of Clayton Campus==' + str(temperature_clayton))
    print('Temparature of Caulfield Campus==' + str(temperature_caulfield))

    bundoora.append(temperature_bundoora)
    clayton.append(temperature_clayton)
    caulfield.append(temperature_caulfield)

    min_bundoora = min(bundoora)
    min_clayton = min(clayton)
    min_caulfield = min(caulfield)

    max_bundoora = max(bundoora)
    max_clayton = max(clayton)
    max_caulfield = max(caulfield)

    x.append(i)
    y.append(temperature_bundoora)
    y.append(temperature_clayton)
    y.append(temperature_caulfield)
    y_mean = statistics.mean(y)

    temp1 = {
        'campus': 'bundoora',
        'min': min_bundoora,
        'max': max_bundoora
    }
    temp2 = {
        'campus': 'clayton',
        'min': min_clayton,
        'max': max_clayton
    }
    temp3 = {
        'campus': 'caulfield',
        'min': min_caulfield,
        'max': max_caulfield
    }

    temps.insert_one(temp1)
    temps.insert_one(temp2)
    temps.insert_one(temp3)

    ax.clear()
    ax.plot(x, bundoora, 'b', label='bundoora')
    ax.plot(x, clayton, 'r', label='clayton')
    ax.plot(x, caulfield, 'g', label='caulfield')

    ax.annotate('Current', xy=(i, temperature_bundoora),
                arrowprops=dict(facecolor='blue', shrink=0.05), )
    ax.annotate('Current', xy=(i, temperature_clayton),
                arrowprops=dict(facecolor='red', shrink=0.05), )
    ax.annotate('Current', xy=(i, temperature_caulfield),
                arrowprops=dict(facecolor='green', shrink=0.05), )

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    ax.set_xlim(left=max(0, i - 10), right=i)
    ax.set_ylim(bottom=max(0, y_mean - 1), top=y_mean + 1)

    fig.canvas.draw()

    time.sleep(605)
    y.clear()
    if count == 5:
        print('New set:')
        print("MIN: " + str(min_bundoora) + ", " + str(min_clayton) + ", " + str(min_caulfield))
        print("MAX: " + str(max_bundoora) + ", " + str(max_clayton) + ", " + str(max_caulfield))
        count = 0

    mean_bundoora = statistics.mean(bundoora)
    mean_clayton = statistics.mean(clayton)
    mean_caulfield = statistics.mean(caulfield)

    mean = {"Bundoora": mean_bundoora, "Clayton": mean_clayton, "Caulfield": mean_caulfield}
    coolest = min(mean, key=lambda k: mean[k])

    if now.hour == 18 and now.minute == 0:
        print("The coolest campus is " + coolest)
        flag = 1
        sys.exit()

plt.close('all')
