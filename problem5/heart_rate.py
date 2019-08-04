import fitbit
import gather_keys_oauth2 as Oauth2
import datetime
from time import sleep
from json import dumps
from kafka import KafkaProducer
import matplotlib

matplotlib.use('TkAgg')

# Update Fitbit API client_id and client_secret
CLIENT_ID = '22DD2Z'
CLIENT_SECRET = '34e491d057e9f7ac217349eea6876823'

# connect to server
server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()

ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN,
                             refresh_token=REFRESH_TOKEN)

# to loading todays time info
today = str(datetime.datetime.now().strftime("%Y-%m-%d"))

fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=today, detail_level='1sec')

time_list = []
val_list = []

for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_list.append(i['value'])
    time_list.append(i['time'])

# Make a Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
# Update the data every 5 minutes
i = 0
for e in range(len(val_list)):
    data1 = {'data1': val_list[i], 'time': time_list[i]}
    # transfer the data(heart_rate , time)
    producer.send('Fitbit', value=data1)
    print(val_list[i], time_list[i])

    sleep(300)
    i += 1
