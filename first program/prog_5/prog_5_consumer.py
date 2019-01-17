from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt

# kafka consumer connect
consumer = KafkaConsumer(
    'test5',
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

x, y, z = [], [], []

# receive data from kafka producer and draw real time graph
for message in consumer:
    message = message.value
    if len(x) > 9:
        del (x[0])
        del (y[0])
    x.append(i)
    y.append(message['number'])

    ax.clear()
    ax.plot(x, y, color='g')

    # calculate max value
    ymax = max(y)
    xpos = y.index(ymax)
    if i > 9:
        xpos = i - 9 + y.index(ymax)

    # annotate max value every 10 seconds
    ax.annotate('MAX', (xpos, ymax), arrowprops=dict(facecolor='red', shrink=0.05))

    # calculate min value
    ymin = min(y)
    xpos2 = y.index(ymin)
    if i > 9:
        xpos2 = i - 9 + y.index(ymin)

    # annotate min value every 10 seconds
    ax.annotate('MIN', (xpos2, ymin), arrowprops=dict(facecolor='red', shrink=0.05))

    # find current value
    xpos3 = y.index(message['number'])
    if i > 9:
        xpos3 = i - 9 + y.index(message['number'])

    # annotate current value
    ax.annotate('CURRENT', (xpos3, message['number']), arrowprops=dict(facecolor='red', shrink=0.05))

    ax.set_xlim(left=max(0, i - 10), right=i + 1)
    fig.canvas.draw()
    i += 1
