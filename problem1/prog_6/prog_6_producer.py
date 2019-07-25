from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

# 오리지널 데이타도 보요주기
# Make a Kafaka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

# Generate data every sec
for e in range(100):
    data = {'data': random.randrange(0, 100)}
    producer.send('kafka_6', value=data)
    sleep(1)
