import random

# Функция которая принимает правую границу


def start_the_game():
    print('Добро пожаловать в числовую угадайку')
    print('Введите целое число для правой границы:')

    def is_digit(border):  # Функция которая проверят что правая граница это число
        if border.isdigit():
            return True
        return False

    while True:
        right_border_local = input()
        if is_digit(right_border_local):
            right_border_local = int(right_border_local)
            num_local = random.randint(1, right_border_local)
            print('Введите предпологаемое число:')
            return num_local, right_border_local
        else:
            print('Введите целое число:')


def is_valid(an):  # Функция которая проверят что введеное число в рамках границ и что это целое число
    if an.isdigit():
        if 1 <= int(an) <= right_border:
            return True
    return False


num, right_border = start_the_game()
counter = 0
first_try = True

while True:
    answer = input()
    counter += 1

    if not is_valid(answer):
        print('А может быть все-таки введем целое число от 1 до', right_border, '?')
    else:
        answer = int(answer)
        if answer < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif answer > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            print('Количество попыток:', counter)

            if first_try:  # Вторая игра и после этого программа останавливается
                num, right_border = start_the_game()
                first_try = False
                counter = 0
            else:
                break
