# выводить все контакты на экран
# добавить контакт
# удалить контакт
# изменить контакт
# найти контакт
# открыть или сохранить
# выход

from phonebook import phonebook
from phonebook import show_phonebook
from add_person import add_person
from find_person import find_person
from remove_cont import remove_cont

print("Выберите действие: ")
print("выводить все контакты на экран - 1")
print("Добавить контакт - 2")
print("изменить контакт -3")
print("найти контакт - 4")
print("открыть или сохранить - 5")
print("удалить контакт - 6")
print("выход - 7")
phonebook()
while True:
    click = int(input())
    if click == 1:

        show_phonebook()
    elif click == 2:
        add_person()
    # elif click == 3:

    elif click == 4:
        find = input('Напишите что кого вы ищете: ')
        find_person(find.title())
    # elif click == 5:
    elif click == 6:
        remove_cont(input('Подскажите кого нужно удалить: '))
    elif click == 7:
        break
