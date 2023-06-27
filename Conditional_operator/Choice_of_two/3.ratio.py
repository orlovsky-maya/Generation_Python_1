num = int(input())
digit_4 = num % 10
digit_3 = (num % 100) // 10
digit_2 = (num // 100) % 10
digit_1 = num // 1000
summ = digit_1 + digit_4
diff = digit_2 - digit_3
if summ == diff:
    print('ДА')
else:
    print('НЕТ')
