from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt
import statistics

# kafka consumer connect
consumer = KafkaConsumer(
    'test6',
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

x, y, avg = [], [], []

# receive data from kafka producer and draw real time graph
for message in consumer:
    message = message.value
    if len(x) > 9:
        del (x[0])
        del (y[0])
        del (avg[0])

    x.append(i)
    y.append(message['number'])
    avg.append(statistics.mean(y))

    ax.clear()
    ax.plot(x, avg, color='g')

    ax.set_xlim(left=max(0, i - 10), right=i + 1)
    fig.canvas.draw()
    i += 1
