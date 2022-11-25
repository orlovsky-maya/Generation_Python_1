# word = 'рука'
#
# word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
# guessed = False  # сигнальная метка
# guessed_letters = []  # список уже названных букв
# guessed_words = []  # список уже названных слов
# tries = 6  # количество попыток
#
# print('Давайте играть в угадайку слов!')
#
# while tries != 0:
#     if word == ''.join(word_completion):
#         print('Поздравляем, вы угадали слово! Вы победили!')
#         print('Слово:', word)
#         guessed = True
#         break
#     print('Количество попыток:', tries)
#     print('Слово:', ''.join(word_completion))
#     print('Ведите букву или слово целиком:')
#     try_symbol = input()
#
#     if try_symbol == word:
#         print('Поздравляем, вы угадали слово! Вы победили!')
#         print('Слово:', word)
#         guessed = True
#         break
#     else:
#         if len(try_symbol) > 1:
#             tries -= 1
#             continue
#         else:
#             if try_symbol in word:
#                 for i in range(len(word)):
#                     if word[i] == try_symbol:
#                         del word_completion[i]
#                         word_completion.insert(i, word[i])
#             else:
#                 tries -= 1
#                 continue
# if not guessed:
#     print('Вы проиграли!')
#     print('Загаданное слово было:', word)
#     print('Количество попыток:', tries)


from random import *

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз',
             'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'конец', 'система', 'отношение', 'женщина',
             'деньги', 'земля', 'машина', 'проблема', 'право', 'решение', 'дверь', 'образ', 'история', 'власть',
             'возможность', 'результат']


def get_word():
    word = choice(word_list).upper()
    return word


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def is_symbol_letter():
    while True:
        symbol = input().strip()
        if str(symbol).isalpha():
            return symbol.upper()
        print('Введи пожалуйста букву или слово целиком ')


def is_guessed_letter_or_words(symbol, guessed_list):
    while True:
        if symbol in guessed_list:
            print('Вы повторяетесь, введите слово или букву которые вы не называли.')
            symbol = is_symbol_letter()
        else:
            guessed_list.append(symbol)
            return symbol


def is_answer_yes():
    print('Вы хотели бы сыграть еще раз? Ответьте да или нет.')
    answer = input().lower().strip()
    while True:
        if answer == 'да':
            return True
        if answer == 'нет':
            print('Спасибо за игру, до встречи!')
            break
        else:
            print('Пожалуйста введите ответ ДА или НЕТ!')


def play(word):
    word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print('Виселица:', display_hangman(tries))
    print('Количество попыток:', tries)
    print('Слово:', ''.join(word_completion))

    while tries != 0:
        if word == ''.join(word_completion):
            print('Поздравляем, вы угадали слово! Вы победили!')
            print('Слово:', word)
            guessed = True
            break
        print('Ведите букву или слово целиком:')
        print(word)
        try_symbol = is_symbol_letter()

        if try_symbol == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            print('Слово:', word)
            guessed = True
            break
        else:
            if len(try_symbol) > 1:
                is_guessed_letter_or_words(try_symbol, guessed_words)
                tries -= 1
                continue
            else:
                try_symbol = is_guessed_letter_or_words(try_symbol, guessed_letters)
                if try_symbol in word:
                    for i in range(len(word)):
                        if word[i] == try_symbol:
                            del word_completion[i]
                            word_completion.insert(i, word[i])
                else:
                    tries -= 1
                    continue
    if not guessed:
        print('Вы проиграли!')
        print('Загаданное слово было:', word)
        print('Виселица:', display_hangman(tries))
        print('Количество попыток:', tries)


while True:
    hidden_word = get_word()
    play(hidden_word)
    if is_answer_yes():
        continue
    break

