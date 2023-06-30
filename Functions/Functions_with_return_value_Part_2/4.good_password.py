# объявление функции
def is_password_good(password):
    if len(password) >= 8 and password.islower() is False and password.isupper() is False and \
            password.isalpha() is False and password.isdigit() is False and password.isalnum() is True:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
