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

print("Выберите действие: ")
print("выводить все контакты на экран - 1")
print("Добавить контакт - 2")
print("изменить контакт -3")
print("найти контакт - 4")
print("открыть или сохранить - 5")
print("выход - 6")
phonebook()
while True:
    click = int(input())
    if click == 1:

        show_phonebook()
    elif click == 2:
        add_person()
    # elif click == 3:
    elif click == 6:
        break
