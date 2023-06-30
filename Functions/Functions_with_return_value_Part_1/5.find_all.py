# объявление функции
def find_all(target, symbol):
    lst_index = []
    for i in range(len(target)):
        if symbol == target[i]:
            lst_index.append(i)
    return lst_index


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))


# Second solution

# объявление функции
def find_all(target, symbol):
    return [i for i in range(len(target)) if symbol == target[i]]


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
