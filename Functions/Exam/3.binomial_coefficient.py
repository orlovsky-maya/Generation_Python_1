from math import factorial


# объявление функции
def compute_binom(n, k):
    koficent = factorial(n) / (factorial(k) * factorial(n - k))
    return int(koficent)


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
