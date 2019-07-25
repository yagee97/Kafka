from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(100):
    if e % 10 != 0:
        data = {'student_id': random.randrange(0, 5000),
                'value': random.randrange(0, 1000)
                }
    # for 10 interval, randomly send no data
    else:
        data = {'student_id': random.randrange(0, 5000)
                }

    producer.send('mongotest', value=data)
    sleep(5)
    e += 1
