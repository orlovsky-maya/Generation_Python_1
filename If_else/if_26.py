colour_1 = input()
colour_2 = input()
if colour_1 == 'красный':
    if colour_2 == colour_1:
        print('красный')
    elif colour_2 == 'синий':
        print('фиолетовый')
    elif colour_2 == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif colour_1 == 'синий':
    if colour_2 == colour_1:
        print('синий')
    elif colour_2 == 'красный':
        print('фиолетовый')
    elif colour_2 == 'желтый':
        print('зеленый')
    else:
        print('ошибка цвета')
elif colour_1 == 'желтый':
    if colour_2 == colour_1:
        print('желтый')
    elif colour_2 == 'красный':
        print('оранжевый')
    elif colour_2 == 'синий':
        print('зеленый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')
