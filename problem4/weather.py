import requests
import pandas
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pandas.read_csv('aus_vic.csv')
cities = []
suburb = []
for p in df['postcode']:
    cities.append('http://api.openweathermap.org/data/2.5/weather?zip=' + str(
        p) + ',au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8')
# for a in df['suburb']:
# suburb.append(df['suburb'])
# print(suburb)

# draw graphs
plt.rcParams['animation.html'] = 'jshtml'
plt.rcParams['axes.grid'] = True
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0
x = []


# json parsing
def parsing():
    # make a request to the collect the data
    reses = []
    idx = 0
    for res in cities:
        reses.append(requests.get(res))
        idx += 1
        if idx == 100:
            break

    # get data as json format
    datas = []
    for data in reses:
        datas.append(data.json()['main']['temp'])
    return datas


datas = parsing()
y, z = [], []
while True:
    ax.clear()
    ax.set_xlim(left=max(0, i - 100), right=i + 1)
    x.append(i)
    y.append(max(datas))
    z.append(min(datas))
    ax.plot(x, y, color='r')
    ax.plot(x, z, color='b')

    fig.canvas.draw()
    time.sleep(2)
    i += 10
