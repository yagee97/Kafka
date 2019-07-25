from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt

# kafka consumer connect
consumer = KafkaConsumer(
    'problem11',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my_group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

plt.rcParams['animation.html'] = 'jshtml'
plt.rcParams['axes.grid'] = True
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0

x, y, z = [], [], []

# receive data from kafka producer and draw real time graph
for message in consumer:
    message = message.value
    x.append(i)
    y.append(message['number'])
    z.append(y[i - 1] - y[i])

    # print("y-1", y[i - 1], "y1", y[i], i)
    # print("result= ", y[i - 1] - y[i])

    ax.clear()
    ax.plot(x, z, color='r')

    # annotate current value
    ax.annotate(z[i], (x[i], z[i]), arrowprops=dict(facecolor='red', shrink=0.05))

    plt.axhline(y=0, color='gray', linewidth='0.7')
    ax.set_xlim(left=max(0, i - 10), right=i + 1)
    ax.set_ylim(top=100, bottom=-100)
    fig.canvas.draw()
    i += 1
