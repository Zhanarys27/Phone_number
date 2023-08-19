def remove_cont(remove_contakt):
    print(remove_contakt)
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        data.truncate()




