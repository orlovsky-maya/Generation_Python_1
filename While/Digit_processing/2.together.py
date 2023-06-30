num = int(input())
last_digit = num % 10
total_sum = 0
counter = 0
total_pro = 1
first_digit = 0
while num != 0:
    current_digit = num % 10
    first_digit = current_digit
    total_sum += current_digit
    counter += 1
    total_pro *= current_digit
    num = num // 10

print(total_sum)
print(counter)
print(total_pro)
print(total_sum / counter)
print(first_digit)
print(first_digit + last_digit)
