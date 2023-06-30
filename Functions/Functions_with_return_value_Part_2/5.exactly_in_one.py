# объявление функции
def is_one_away(word1, word2):
    counter_of_different_symbols = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter_of_different_symbols += 1
    if counter_of_different_symbols == 1:
        return True
    else:
        return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))