def find_person(find):
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for item in data:
            if find in item.split():
                print(item)


