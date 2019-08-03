from kafka import KafkaConsumer
from pymongo import MongoClient
import matplotlib.pyplot as plt
from json import loads

# Consumer connection
consumer = KafkaConsumer(
    'SetB_Problem3_1',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my_group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.p3.p3

fig = plt.figure()
ax = fig.add_subplot(111)
# Draw graph
plt.rcParams['animation.html'] = 'jshtml'
i = 0

# x1 for axis, y1 for y axis
x1, y1 = [], []
# x2 for x axis y2 for another y axis
x2, y2 = [], []

fig.show()
# Data from producer
for message in consumer:
    message = message.value
    collection.insert_one(message)
    if len(x1) > 9:
        del (x1[0])
        del (y1[0])
    if len(x2) > 9:
        del (x2[0])
        del (y2[0])

    #     print('{} added to {}'.format(message,collection))

    if 'data1' in message:
        x1.append(i)
        y1.append(message['data1'])

    if 'data2' in message:
        x2.append(i)
        y2.append(message['data2'])

    i += 1
    plt.title('comparable graph')
    ax.clear()
    # print(x1, y1)
    # print(x2, y2)
    ax.plot(x1, y1, 'r', label='data1')
    ax.plot(x2, y2, 'b', label='data2')
    ax.set_xlim(left=max(0, i - 10), right=i + 1)
    fig.canvas.draw()
# plt.show()

# Close plot
plt.close('all')