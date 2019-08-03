import json
from collections import OrderedDict

file_data = OrderedDict()

file_data["Ellie"] = "23/11/1997"
file_data["Surim"] = "16/10/1997"

with open('test.json','w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

with open('test.json') as data_file:
    data = json.load(data_file)

cont = True
while cont:
    query = input("**Type query name** ")
    result = data.get(query)
    print(result)

    addition = input("Do you add information?(yes/no): ")
    if addition == 'yes':
        name = input("Enter your name: ")
        birth = input("Enter your birth: ")
        file_data[name] = birth

        with open('test.json', 'w', encoding="utf-8") as make_file:
            json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

        with open('test.json') as data_file:
            data = json.load(data_file)

    terminate = input("Do you want to terminate?(yes/no)")
    if terminate == "yes":
        cont = False
