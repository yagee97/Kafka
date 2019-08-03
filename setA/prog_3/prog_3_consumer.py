from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt

# kafka consumer connect
consumer = KafkaConsumer(
    'numtest4',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my_group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))


plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0

x, y = [], []

# receive data from kafka producer and draw real time graph
for message in consumer:
    message = message.value
    x.append(i)
    y.append(message['number'])
    ax.clear()
    ax.plot(x, y, color='g')
    ax.set_xlim(left=max(0, i - 10), right=i + 1)
    fig.canvas.draw()
    i += 1
