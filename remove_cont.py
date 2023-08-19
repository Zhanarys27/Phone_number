def remove_cont(remove_contakt):

    lst = []
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lst = list(data)
        for item in reversed(range(len(lst))):
            if remove_contakt in lst[item]:
                lst.pop(item)
        print(lst)
    with open('phonebook.txt', 'r', encoding='utf-8') as data:

        data.writelines(lst)







