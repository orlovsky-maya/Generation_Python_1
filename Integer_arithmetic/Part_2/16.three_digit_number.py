num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100
summa = a + b + c
product = a * b * c
print('Сумма цифр =', summa)
print('Произведение цифр =', product)
