# объявление функции
def is_pangram(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in text:
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))