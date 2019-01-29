from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt

# Consumer connection
consumer = KafkaConsumer(
    'kafka_123',
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
# x for xAxis, y for yAxis
x, y, time = [], [], []

# Data from producer
for message in consumer:
    message = message.value

    if len(x) > 9:
        del (x[0])
        del (y[0])
        del (time[0])
    x.append(i)
    y.append(message['data'])
    time.append(message['time'])

    ax.clear()
    for z in len(y):
        ax.plot(time, y[z], "o")

    fig.canvas.draw()
    ax.set_xlim(left=max(0, i - 10), right=i)
