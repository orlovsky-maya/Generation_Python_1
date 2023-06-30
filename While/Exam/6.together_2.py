num = int(input())
counter_3 = 0

counter_last_digit = 0
last_digit = num % 10

counter_even = 0

total_more_5 = 0

total_more_7 = 1

counter_0_and_5 = 0

while num != 0:
    digit = num % 10
    if digit == 3:
        counter_3 += 1
    if digit == last_digit:
        counter_last_digit += 1
    if digit % 2 == 0:
        counter_even += 1
    if digit > 5:
        total_more_5 += digit
    if digit > 7:
        total_more_7 *= digit
    if digit == 0:
        counter_0_and_5 += 1
    if digit == 5:
        counter_0_and_5 += 1
    num //= 10
print(counter_3)
print(counter_last_digit)
print(counter_even)
print(total_more_5)
print(total_more_7)
print(counter_0_and_5)