# объявление функции
def print_fio(name, surname, patronymic):
    name = name.title()
    surname = surname.title()
    patronymic = patronymic.title()
    print(surname[0], name[0], patronymic[0], sep='')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

# Second solution

# объявление функции
def print_fio(name, surname, patronymic):
    for _ in (surname, name, patronymic):
        print(_[0].upper(), end = '')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)