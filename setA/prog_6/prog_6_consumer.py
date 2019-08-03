from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt
import statistics

# Consumer connection
consumer = KafkaConsumer(
    'kafka_6',
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
check = 0

x, y, x_, avg = [], [], [], []

# Data from producer
for message in consumer:
    message = message.value

    # Range checking
    if len(x) > 49:
        del (x[0])
        del (y[0])
    if len(avg) > 49:
        del (x_[0])
        del (avg[0])

    x.append(i)
    y.append(message['data'])
    ax.clear()

    check += 1
    if check > 9:
        avg.append(statistics.mean(y))
        x_.append(i)
        ax.plot(x_, avg, color='g', label="Average")

    ax.plot(x, y, color='r', label="Data per sec")

    ax.set_xlim(left=max(0, i - 50), right=i)
    ax.set_title("Plotting data every sec, and average every 10 secs.")
    # ax.set_xlabel("Time(sec)")
    # ax.set_ylabel("Data")
    fig.canvas.draw()
    i += 1
