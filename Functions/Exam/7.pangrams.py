# объявление функции
def is_pangram(txt):
    txt = txt.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in txt:
            return False
    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
