def is_palindrome(text):
    text = text.lower()
    text_list = list(text)
    clear_text_list = []
    for s in text_list:
        if s not in ",.!?-' '":
            clear_text_list.append(s)
    if clear_text_list[:] == clear_text_list[::-1]:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))


# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# объявление функции
def is_palindrome(text):
    s = ''
    for i in text:
        if i.isalpha():
            s += i.upper()
    return s == s[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))