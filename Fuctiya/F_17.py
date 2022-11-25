# объявление функции
def is_password_good(password):
    if len(password) >= 8 and password.islower() == False and password.isupper() == False and password.isalpha() == False and password.isdigit() == False and password.isalnum() == True:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
