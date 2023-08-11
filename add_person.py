from phonebook import phonebook


def add_person():
    fio = input("Введите фамилию, имя и отчество: ")
    phone_number = int(input("Введите номер телефона: "))
    comment = input("Введите комментарии к данному человеку:")
    src = f'{fio}: {phone_number} |{comment}\n'
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(src)
