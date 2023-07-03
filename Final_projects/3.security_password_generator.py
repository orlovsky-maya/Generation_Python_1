import random


def is_digit_more_then_zero(num):
    while True:
        if num.isdigit():
            if int(num) > 0:
                number = int(num)
                return number
        print('Введите целое число больше нуля:')
        num = input()


def is_length_is_more_0_less_76(leng):
    while True:
        if leng.isdigit():
            if 76 >= int(leng) > 0:
                leng = int(leng)
                return leng
            if int(leng) > 76:
                print('Количество символов превышает 76, введите число меньше чем 76:')
            if int(leng) <= 0:
                print('Введите целое число больше нуля:')
        else:
            print('Введите целое число больше нуля:')
        leng = input()


def is_answer_yes():
    answer = input().lower().strip()
    while True:
        if answer == 'да':
            return True
        if answer != 'нет':
            print('Пожалуйста введите ответ ДА или НЕТ!')
            input().lower().strip()
        return False


def generate_password(char, leng):
    password = random.sample(char, leng)
    print('Ваш пароль:', *password, sep='')


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

print('Для того чтобы сгенерировать надежный пароль, ответьте на несколько вопросов.')
print('Начнем!')

print('Введите количество паролей для генерации:')
count_of_passwords = input()
count_of_passwords = is_digit_more_then_zero(count_of_passwords)

while True:
    print('Введите длину одного пароля (пароль может содержать не более 76 символов):')
    length_of_password = input()
    length_of_password = is_length_is_more_0_less_76(length_of_password)

    print('Включать ли цифры 0123456789? да/нет')
    if is_answer_yes():
        chars += digits

    print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет')
    if is_answer_yes():
        chars += uppercase_letters

    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет')
    if is_answer_yes():
        chars += lowercase_letters

    print('Включать ли символы !#$%&*+-=?@^_? да/нет')
    if is_answer_yes():
        chars += punctuation

    print('Исключать ли неоднозначные символы il1Lo0O? да/нет')
    if is_answer_yes():
        for symbol in chars:
            if symbol in 'il1Lo0O':
                chars = chars.replace(symbol, '')

    if length_of_password < len(chars):
        break
    else:
        print('К сожалению сгенерировать пароль не получилось.')
        print('Включите в пароль еще символы или уменьшите длину пароля.')
        continue

for i in range(count_of_passwords):
    generate_password(chars, length_of_password)
