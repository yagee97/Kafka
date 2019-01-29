from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

# Make a Kafaka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

tmp_data = []

# Generate data every random sec
for e in range(100):
    getsu = random.randint(1, 5)
    tmp_time = random.randint(1, 10)

    # generate random number of data
    for i in range(0, getsu):
        tmp_data.append(random.randint(0, 100))

    data = {'data': tmp_data, 'time': tmp_time}
    producer.send('kafka_123', value=data)
    sleep(tmp_time)
    tmp_data.clear()
