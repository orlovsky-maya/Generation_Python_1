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