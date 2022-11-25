# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


#
# largest = -1
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)


# largest = int(input())  # принимаем первое число за максимальное
# for i in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)


# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)

total = 0
for i in range(1, 6):
    total += i
    print(total)


