from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt
import statistics

# kafka consumer connect
consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my_group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# Draw 4 graph
plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
fig.show()

# init
x1, y1, x2, y2, x3, y3, avg_x, avg_y = [], [], [], [], [], [], [], []
total = [0, ]
i = [0, 0, 0, 0]

# receive data from kafka producer and draw real time graph
for message in consumer:
    message = message.value
    # Range checking

    if i[3] > 9:
        del (avg_x[0])
        del (avg_y[0])

    if 'number1' in message:
        x1.append(i[0])
        i[0] += 1
        y1.append(message['number1'])
        total.append(message['number1'])
    if 'number2' in message:
        x2.append(i[1])
        i[1] += 1
        y2.append(message['number2'])
        total.append(message['number2'])
    if 'number3' in message:
        x3.append(i[2])
        i[2] += 1
        y3.append(message['number3'])
        total.append(message['number3'])
    i[3] += 1
    avg_x.append(i[3])
    avg_y.append(statistics.mean(total))

    # Draw graph1
    ax1.clear()
    ax1.plot(x1, y1, color='r')
    ax1.set_xlim(left=max(0, i[0] - 10), right=i[0] + 1)
    fig.canvas.draw()

    # Draw graph2
    ax2.clear()
    ax2.plot(x2, y2, color='b')
    ax2.set_xlim(left=max(0, i[1] - 10), right=i[1] + 1)
    fig.canvas.draw()

    # Draw graph3
    ax3.clear()
    ax3.plot(x3, y3, color='y')
    ax3.set_xlim(left=max(0, i[2] - 10), right=i[2] + 1)
    fig.canvas.draw()

    # Draw graph4
    ax4.clear()
    ax4.plot(avg_x, avg_y, color='g')
    ax4.set_xlim(left=max(0, i[3] - 10), right=i[3] + 1)
    fig.canvas.draw()
