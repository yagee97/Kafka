from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(100):
    data = {'number': random.randrange(0, 100)}
    producer.send('numtest4', value=data)
    it = random.randrange(0, 10) # random interval
    sleep(it)
