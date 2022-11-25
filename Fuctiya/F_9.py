# объявление функции
def get_factors(num):
    deliteli = []
    for i in range(1, num + 1):
        if num % i == 0:
            deliteli.append(i)
    return deliteli

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))