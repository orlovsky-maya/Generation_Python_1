# объявление функции
def is_magic(date):
    date_list = date.split('.')
    day_month = int(date_list[0]) * int(date_list[1])
    last_digits_year = int(date_list[2]) % 100
    if day_month == last_digits_year:
        return True
    return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))