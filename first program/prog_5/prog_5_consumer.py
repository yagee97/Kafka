from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt

# Make a Kafaka consumer
consumer = KafkaConsumer(
    'pro_1',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='m_g',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# Make a plot graph
plt.rcParams['animation.html'] = 'jshtml'
plt.rcParams['axes.grid'] = True
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0

# x is a second, y is a data from producer
x, y = [], []

# Get message from the producer via kafka
for message in consumer:
    message = message.value
    if len(x) > 9:
        del (x[0])
        del (y[0])
    # z is for min, max and current value in last ten second
    z = []
    x.append(i)
    y.append(message['number'])
    z.append(min(y))
    z.append(max(y))
    z.append(message['number'])
    ax.clear()
    ax.plot(x, y, color='r')
    for n, txt in enumerate(z):
        ax.annotate(txt, (i - 9 + y.index(z[n]), z[n]))
    ax.set_xlim(left=max(0, i - 10), right=i + 1)
    fig.canvas.draw()
    i += 1
