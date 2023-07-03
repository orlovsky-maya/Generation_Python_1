# Code review - 1

counter = 0
p = 1  # error_1
for i in range(10):  # error_2
    x = int(input())
    if x >= 0:  # error_3
        p *= x
        counter += 1
if counter > 0:
    print(counter)  # error_4
    print(p)
else:
    print('NO')

# Code review - 2

largest = -10 ** 6  # error_1
total = 0
counter = 0
for i in range(10):  # error_2
    x = int(input())
    if x < 0:
        total += x  # error_3
        counter += 1
        if x > largest:  # error_4
            largest = x
if counter > 0:
    print(total)
    print(largest)
else:
    print('NO')  # error_5

# Code review - 3

total = 0  # error_1
for i in range(7):  # error_2
    num = int(input())  # error_3
    if num > 0 and num % 2 == 0:  # error_4
        total += num
print(total)

# Code review - 4

num = int(input())

largest_digit = -1

while num != 0:
    last_digit = num % 10
    if last_digit % 3 == 0 and last_digit > largest_digit:
        largest_digit = last_digit
    num //= 10
if largest_digit == -1:
    print('NO')
else:
    print(largest_digit)

# Code review - 5

n = int(input())
while n > 9:
    n //= 10
print(n)

# Code review - 6

n = int(input())  # error_1
total = 1  # error_2
while n != 0:  # error_3
    last_digit = n % 10
    total *= last_digit
    n //= 10
print(total)