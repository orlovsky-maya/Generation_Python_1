# объявление функции
def draw_triangle():
    space = ' '
    star = '*'
    count_of_space = 7
    count_of_star = 1
    for i in range(8):
        print(space * count_of_space + star * count_of_star)
        count_of_space -= 1
        count_of_star += 2


# основная программа
draw_triangle()  # вызов функции


# Second solution

# объявление функции
def draw_triangle():
    m = 15
    for i in range(1, m + 1, 2):
        print(' ' * ((m - i) // 2) + '*' * i)


# основная программа
draw_triangle()
