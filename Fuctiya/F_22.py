# объявление функции
def convert_to_python_case(text):
    text = list(text)
    text[0] = text[0].lower()
    for i in range(1, len(text)):
        if text[i].isupper():
            text[i] = text[i].lower()
            text.insert(i, '_')
    text = ''.join(text)
    return text

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))


# объявление функции
def convert_to_python_case(text):
    result = ''
    for c in text:
        if c.isupper():
            result += '_'
        result += c.lower()
    return result[1::]

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))