# объявление функции
def number_to_words(num):
    units = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    dozens_1 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
                'семнадцать', 'восемнадцать', 'девятнадцать']
    dozens_2 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if 1 <= num <= 9:
        index_units = num - 1
        return units[index_units]
    if 10 <= num <= 19:
        index_dozens_1 = num % 10
        return dozens_1[index_dozens_1]
    if 20 <= num <= 99:
        if num % 10 == 0:
            index_dozens_2 = num // 10 - 2
            return dozens_2[index_dozens_2]
        else:
            index_d_1 = num // 10 - 2
            index_u = num % 10 - 1
            return dozens_2[index_d_1] + ' ' + units[index_u]


# считываем данные
n = int(input())

# вызываем функцию21

print(number_to_words(n))
