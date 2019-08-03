import json
import matplotlib.pyplot as plt
import matplotlib

with open('data.json') as data_file:
    data = json.load(data_file)  # JSON 파일 읽어와서 data라는 변수에 저장

month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for data in data.values():
    temp = data.split('/')
    month[int(temp[1]) - 1] = month[int(temp[1]) - 1] + 1

m_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.bar(m_list,month)
plt.show()
