def is_prime(num):
    flag = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag is True:
        return True
    else:
        return False


# объявление функции
def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
