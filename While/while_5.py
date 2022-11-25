num = int(input())
last_digit_1 = num % 10
total_sum = 0
counter = 0
total_pro = 1
while num != 0:
    last_digit = num % 10
    total_sum += last_digit
    counter += 1
    total_pro *= last_digit
    num = num // 10
print(total_sum)
print(counter)
print(total_pro)
print(total_sum / counter)
print(last_digit)
print(last_digit + last_digit_1)


