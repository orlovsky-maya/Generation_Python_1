# объявление функции
def is_prime(num):
    flag = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        return True
    else:
        return False


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))