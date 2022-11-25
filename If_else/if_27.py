a = int(input())
if 1 <= a <= 10:
    if a % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= a <= 18:
    if a % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= a <= 28:
    if a % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= a <= 36:
    if a % 2 == 0:
        print('красный')
    else:
        print('черный')
elif a == 0:
    print('зеленый')
else:
    print('ошибка ввода')
