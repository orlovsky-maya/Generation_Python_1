def is_valid_answer(v1, v2, request):
    while True:
        answer = input().upper().strip()
        if answer == v1 or answer == v2:
            return answer
        else:
            print(request)


def is_digit_more_then_zero():
    while True:
        num = input()
        if num.isdigit():
            if int(num) > 0:
                number = int(num)
                return number
        print('Введите целое число больше нуля:')


def is_text_correct_language(alphabet, request):
    while True:
        text_to_encrypt = input()
        for symbol in text_to_encrypt.lower():
            if symbol in alphabet:
                print(request)
                break
            else:
                return text_to_encrypt


def encrypting(text_to_encrypt, alphabet_lower, alphabet_upper, step, number_of_characters):
    encrypted_text = ''
    for symbol_open in text_to_encrypt:
        if str(symbol_open).isalpha():
            if str(symbol_open).islower():
                index_of_symbol_open = alphabet_lower.find(str(symbol_open))
                index_of_symbol_encrypted = (index_of_symbol_open + step) % number_of_characters
                encrypted_text += alphabet_lower[index_of_symbol_encrypted]
            if str(symbol_open).isupper():
                index_of_symbol_open = alphabet_upper.find(str(symbol_open))
                index_of_symbol_encrypted = (index_of_symbol_open + step) % number_of_characters
                encrypted_text += alphabet_upper[index_of_symbol_encrypted]
        else:
            encrypted_text += symbol_open
    return encrypted_text


def decryption(text_to_decrypt, alphabet_lower, alphabet_upper, step, number_of_characters):
    decrypted_text = ''
    for symbol_open in text_to_decrypt:
        if str(symbol_open).isalpha():
            if str(symbol_open).islower():
                index_of_symbol_open = alphabet_lower.find(str(symbol_open))
                index_of_symbol_encrypted = (index_of_symbol_open - step) % number_of_characters
                decrypted_text += alphabet_lower[index_of_symbol_encrypted]
            if str(symbol_open).isupper():
                index_of_symbol_open = alphabet_upper.find(str(symbol_open))
                index_of_symbol_encrypted = (index_of_symbol_open - step) % number_of_characters
                decrypted_text += alphabet_upper[index_of_symbol_encrypted]
        else:
            decrypted_text += symbol_open
    return decrypted_text


alphabet_lower_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number_of_characters_en = 26
alphabet_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_upper_ru = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
number_of_characters_ru = 32

print('Привет! Эта программа поможет Вам зашифровать или дешифровать текст. Прежде чем мы начнем, ответьте пожалуйста '
      'на несколько вопросов.')

print('Вы хотите зашифровать текст или дешифровать? Ответы: Ш - шифровать, Д - дешифровать')
direction = is_valid_answer('Ш', 'Д', 'Введите ответ либо Ш - шифровать, либо Д - дешифровать')

print('Какой язык Вы хотели бы использовать? Ответы:  Р - русский, А - Английский')
alphabet_language = is_valid_answer('Р', 'А', 'Введите ответ либо Р - русский, либо А - Английский')

print('Введите шаг сдвига. Шаг сдвига должен быть целым числом.')
shift_step = is_digit_more_then_zero()

if alphabet_language == 'А':
    if direction == 'Ш':
        print('Введите текст для шифрования на английском языке.')
        text_to_encrypt_en = is_text_correct_language(alphabet_lower_ru, 'Пожалуйста используйте английский язык.')
        encrypted_text_en = encrypting(text_to_encrypt_en, alphabet_lower_en, alphabet_upper_en, shift_step,
                                       number_of_characters_en)
        print(encrypted_text_en)
    if direction == 'Д':
        print('Введите текст для дешифрования на английском языке.')
        text_to_decrypt_en = is_text_correct_language(alphabet_lower_ru, 'Пожалуйста используйте английский язык.')
        decrypted_text_en = decryption(text_to_decrypt_en, alphabet_lower_en, alphabet_upper_en, shift_step,
                                       number_of_characters_en)
        print(decrypted_text_en)

if alphabet_language == 'Р':
    if direction == 'Ш':
        print('Введите текст для шифрования на русском языке.')
        text_to_encrypt_ru = is_text_correct_language(alphabet_lower_en, 'Пожалуйста используйте русский язык.')
        encrypted_text_ru = encrypting(text_to_encrypt_ru, alphabet_lower_ru, alphabet_upper_ru, shift_step,
                                       number_of_characters_ru)
        print(encrypted_text_ru)
    if direction == 'Д':
        print('Введите текст для дешифрования на русском языке.')
        text_to_decrypt_ru = is_text_correct_language(alphabet_lower_en, 'Пожалуйста используйте русский язык.')
        decrypted_text_ru = decryption(text_to_decrypt_ru, alphabet_lower_ru, alphabet_upper_ru, shift_step,
                                       number_of_characters_ru)
        print(decrypted_text_ru)
