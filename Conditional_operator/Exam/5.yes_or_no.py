num = int(input())
if num % 2 != 0:
    print('YES')
elif num % 2 == 0:
    if 2 <= num <= 5:
        print('NO')
    elif 6 <= num <= 20:
        print('YES')
    else:
        print('NO')

# Second solution

a = int(input())
if (a % 2 != 0) or (a % 2 == 0 and 6 <= a <= 20):
    print('YES')
else:
    print('NO')

# Third solution

number = int(input())
if number % 2 != 0 or 6 <= number <= 20:
    print('YES')
else:
    print('NO')