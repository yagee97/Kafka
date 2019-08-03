dic = {'Ellie':'23/11/1997','Surim':'16/10/1997'}
cont = True

while cont:
    query = input("**Type query name: **")
    result = dic.get(query)
    print(result)

    addition = input("Do you add information?(yes/no): ")
    if addition == 'yes':
        name = input("Enter your name: ")
        birth = input("Enter your birth: ")
        dic[name] = birth

    terminate = input("Do you want to terminate?(yes/no)")
    if terminate == "yes":
        cont = False



