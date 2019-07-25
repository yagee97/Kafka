from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'mongotest',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# connect with mongoDB
connection = MongoClient("localhost", 27017)

# make database
db = connection.testDB

# make collection
collection = db.test

for message in consumer:
    message = message.value

    # if value exists, check range
    if 'value' in message:
        if message['value'] > 100:
            print("the number is bigger than 100")
            continue
    # insert data into collection
    collection.insert_one(message)

    # if no value, represent "*"
    collection.find_one_and_update(
        {"value": {"$exists": False}}, {"$set": {"value": "*"}}, new=True)
