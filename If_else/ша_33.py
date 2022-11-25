num = int(input())
if num % 2 != 0:
    print('YES')
elif num % 2 == 0:
    if num >= 2 and num <= 5:
        print('NO')
    elif num >= 6 and num <= 20:
        print('YES')
    else:
        print('NO')


a = int(input())
if (a % 2 != 0) or (a % 2 == 0 and 6 <= a <= 20):
    print('YES')
else:
    print('NO')

number = int(input())
if number % 2 != 0 or 6 <= number <= 20:
    print('YES')
else:
    print('NO')