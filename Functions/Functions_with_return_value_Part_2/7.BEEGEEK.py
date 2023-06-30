# Провернка на полиндрома
def is_palindrome(number):
    number = str(number)
    if number[:] == number[::-1]:
        return True
    else:
        return False


# Проверка на простоту
def is_prime(num):
    flag = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
    if num > 1 and flag is True:
        return True
    else:
        return False


# Проверка на четность
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# объявление функции
def is_valid_password(password):
    password = [int(i) for i in password.split(':')]
    if len(password) == 3:
        if is_palindrome(password[0]):
            if is_prime(password[1]):
                if is_even(password[2]):
                    return True
    return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
