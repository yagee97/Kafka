import json
import statistics

with open('data.json') as data_file:
    data = json.load(data_file)

x = 0
addition = 0
age = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for data, x in zip(data.values(), range(20)):
    temp = data.split('/')
    age[x] = 2019 - int(temp[2]) + 1 #Korean age!

mean = statistics.mean(age)
median = statistics.median(age)

print("Mean is ",mean)
print("Median is ", median)

