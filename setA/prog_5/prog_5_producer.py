from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

# Make a Kafaka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

# Generate data every second
for e in range(100):
    data = {'number': random.randrange(0, 100)}
    producer.send('pro_1', value=data)
    sleep(1)
