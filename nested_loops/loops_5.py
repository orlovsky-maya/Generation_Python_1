num = int(input())

while num > 9:
    current_num = 0
    while num != 0:
        last_digit = num % 10
        current_num += last_digit
        num //= 10
    num = current_num
print(num)
