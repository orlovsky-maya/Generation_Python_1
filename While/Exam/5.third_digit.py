num = int(input())
third_digit = 0
while num > 99:
    last_digit = num % 10
    num //= 10
    third_digit = last_digit
print(third_digit)