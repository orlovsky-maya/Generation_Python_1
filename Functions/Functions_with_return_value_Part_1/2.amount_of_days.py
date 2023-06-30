# объявление функции
def get_days(month):
    if str(month) in '1 3 5 7 8' or month == 10 or month == 12:
        return 31
    elif str(month) in '4 6 9 11':
        return 30
    else:
        return 28


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))


# Second solution

# объявление функции
def get_days():
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month[num]


# считываем данные
num = int(input())

# вызываем функцию
print(get_days())
