# объявление функции
def get_factors(num):
    divider = []
    for i in range(1, num + 1):
        if num % i == 0:
            divider.append(i)
    return divider


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
