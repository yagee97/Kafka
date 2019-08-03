import json

frequency = {}

with open('data.json') as data_file:
    data = json.load(data_file)  # JSON 파일 읽어와서 data라는 변수에 저장

month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for data in data.values():
    temp = data.split('/')
    month[int(temp[1]) - 1] = month[int(temp[1]) - 1] + 1

for x in range(12):
    print("month:",x+1," = ",month[x],"people")
