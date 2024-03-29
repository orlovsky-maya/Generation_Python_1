# объявление функции
def is_correct_bracket(text):
    if not text.isspace():
        if not text.isalnum():
            if text.startswith('(') and text.endswith(')'):
                counter = 0
                for c in text:
                    if c in '(':
                        counter += 1
                    if c in ')':
                        if counter == 0:
                            return False
                        if counter > 0:
                            counter -= 1
                if counter == 0:
                    return True
    return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


# Second solution

# # объявление функции
def is_correct_bracket(text):
    if text.isspace():
        return False

    if text.isalnum():
        return False

    counter = 0
    for c in text:
        if c in '(':
            counter += 1
        if c in ')':
            if counter == 0:
                return False
            if counter > 0:
                counter -= 1
    return counter == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


# Third solution

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return text == ''


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
