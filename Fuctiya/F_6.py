# объявление функции
def print_digit_sum(num):
    summa = 0
    for i in range(len(str(num))):
        summa += int(str(num)[i])
    print(summa)

# считываем данные
k = int(input())

# вызываем функцию
print_digit_sum(k)

# объявление функции
def print_digit_sum(num):
    print(sum([int(i) for i in num]))

# считываем данные
n = input()

# вызываем функцию
print_digit_sum(n)