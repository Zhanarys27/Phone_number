def phonebook():
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write('')


def show_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line, end="")
