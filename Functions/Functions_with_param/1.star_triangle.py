# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
    for j in range(base // 2, 0, -1):
        print(fill * j)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
