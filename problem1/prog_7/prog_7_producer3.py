from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(100):
    data = {'number3': random.randrange(0, 100)}
    producer.send('test', value=data)
    sleep(1)
