from json import loads
from pymongo import MongoClient
from kafka import KafkaConsumer
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# % matplotlib notebook

# Consumer connection
consumer = KafkaConsumer(
    'Fitbit',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my_group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# Mongodb
client = MongoClient('localhost:27017')
collection = client.p5.p5

# construct plotting
plt.rcParams['animation.html'] = 'jshtml'
plt.rcParams['axes.grid'] = True
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0
val = []
time_s = []
tmp = []
tmp_time = []
tmptmp = 0
key = []

for message in consumer:
    message = message.value
    if 'data1' in message:
        val.append(message['data1'])
        tmp_time.append(message['time'])
        time_s.append(i)

    # heart_rate < 90 or heart_rate > 140 , insert into mongoDB
    if message.get('data1') < 90 or message.get('data1') > 140:
        collection.insert_one(message)
        print(message.get('data1'))

    plt.title('plotting heartbeat')
    ax.clear()
    ax.set_xlim(left=max(0, i - 10), right=i + 1)
    # y axis
    # if i==100:
    # break
    ax.plot(tmp_time, val, color='r')
    plt.gcf().autofmt_xdate()
    fig.canvas.draw()
    i += 1

plt.close('all')
