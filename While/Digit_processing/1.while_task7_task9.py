# Reverse Order 1

num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

# Reverse Order 2

num = int(input())

while num != 0:
    last_digit = num % 10
    num //= 10
    print(last_digit, end='')


# Max and Min
n = int(input())
largest = n % 10
smallest = n % 10
n //= 10
while n != 0:
    last_digit = n % 10
    if last_digit > largest:
        largest = last_digit
    else:
        if last_digit < smallest:
            smallest = last_digit
    n //= 10
print('Максимальная цифра равна', largest)
print('Минимальная цифра равна', smallest)

# Max and Min second solution

n = int(input())
minimum = 9
maximum = 0
while n > 0:
    x = n % 10
    if x < minimum:
        minimum = x
    if x > maximum:
        maximum = x
    n = n // 10
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)
