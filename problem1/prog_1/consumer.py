from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt

# Consumer connection
consumer = KafkaConsumer(
    'numtest',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my_group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# Draw graph
plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0

x, y = [], []

for message in consumer:
    message = message.value
    x.append(i)
    y.append(message['number'])
    ax.plot(x, y, color='b')
    fig.canvas.draw()
    i += 1

# Close plot
plt.close('all')