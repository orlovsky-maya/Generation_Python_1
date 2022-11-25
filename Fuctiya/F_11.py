# # объявление функции
# def find_all(target, symbol):
#     spisok_index = []
#     for i in range(len(target)):
#         if symbol == target[i]:
#             spisok_index.append(i)
#     return spisok_index
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))

# объявление функции
def find_all(target, symbol):
    return [i for i in range(len(target)) if symbol == target[i]]

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))