from random import *

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место', 'лицо', 'друг',
             'глаз', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'конец', 'система', 'отношение',
             'женщина', 'деньги', 'земля', 'машина', 'проблема', 'право', 'решение', 'дверь', 'образ', 'история',
             'власть', 'возможность', 'результат']


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


def get_answer():
    while True:
        symbol = input().strip()
        if str(symbol).isalpha():
            return symbol.upper()
        print('Введи пожалуйста букву или слово целиком ')


def is_answer_yes():
    print('Вы хотели бы сыграть еще раз? Ответьте да или нет.')
    while True:
        answer = input().lower().strip()
        if answer == 'да':
            return True
        if answer == 'нет':
            print('Спасибо за игру, до встречи!')
            break
        else:
            print('Пожалуйста введите ответ ДА или НЕТ!')
            continue


def play(word):
    word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')

    # цикл игры
    while tries != 0:
        print('Виселица:', display_hangman(tries))
        print('Количество попыток:', tries)
        print('Слово:', ''.join(word_completion))
        print('Ведите букву или слово целиком:')
        print(word)

        # цикл ввода
        while True:
            answer = get_answer()
            # validate answer
            if answer in guessed_words or answer in guessed_letters:
                print('Вы повторяетесь, введите слово или букву которые вы не называли.')
                continue
            else:
                break

        if len(answer) > 1:
            # слово
            if answer == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                print('Слово:', word)
                guessed = True
                break
            else:
                print('Вы не угадали слово.')
                guessed_words.append(answer)
                tries -= 1
        else:
            if answer in word:
                print('Вы угадали, эта буква есть в слове.')
                for i in range(len(word)):
                    if word[i] == answer:
                        word_completion[i] = answer
                if word == ''.join(word_completion):
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    print('Слово:', word)
                    guessed = True
                    break
            else:
                print('Вы не угадали, такой буквы нет в слове.')
                tries -= 1
            guessed_letters.append(answer)
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
