# объявление функции
def number_of_factors(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    return counter


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
