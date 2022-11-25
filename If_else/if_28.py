a_1 = int(input())
b_1 = int(input())
a_2 = int(input())
b_2 = int(input())
if a_1 == a_2:  # common point a
    if b_1 == b_2:  # 5
        print(a_1, b_1)
    elif b_1 > b_2:  # 2
        print(a_1, b_2)
    elif b_1 < b_2:  # 1
        print(a_1, b_1)
elif b_1 == b_2:  # common point b
    if a_1 < a_2:  # 4
        print(a_2, b_1)
    elif a_1 > a_2:  # 3
        print(a_1, b_1)
elif a_1 < a_2:  # cross
    if b_2 > b_1 > a_2:  # 8.1
        print(a_2, b_1)
    elif b_1 > b_2:  # 7.1
        print(a_2, b_2)
    elif b_1 == a_2:  # 6.1
        print(b_1)
    else:
        print('пустое множество')  # 9.1
elif a_1 > a_2:  # cross
    if b_1 > b_2 > a_1:  # 8.2
        print(a_1, b_2)
    elif b_1 < b_2:  # 7.2
        print(a_1, b_1)
    elif b_2 == a_1:  # 6.2
        print(b_2)
    else:
        print('пустое множество')  # 9.2
else:
    print('пустое множество')
