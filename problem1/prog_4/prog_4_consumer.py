from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt

# Consumer connection
consumer = KafkaConsumer(
    'kafka_4',
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
j = 0
tmp_time = []

# x for xAxis, y for yAxis
x, y = [], []

# Data from producer
for message in consumer:
    message = message.value

    # Range checking
    if len(x) > 50:
        del (x[0])
        del (y[0])

    tmp_time.append(message['time'])

    # value of xAxis and yAxis with max value of yAxis
    x.append(i)
    y.append(message['data'])

    ax.clear()
    for xe, ye in zip(x, y):
        plt.scatter([xe] * len(ye), ye, label="Data from producer")
    fig.canvas.draw()

    ax.set_xlim(left=max(0, i - 50), right=i)

    i += tmp_time[j]
    j += 1
