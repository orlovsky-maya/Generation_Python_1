year = int(input())
a = year % 10
b = (year // 10) % 10
if a == 0 and b == 0:
    print('YES')
else:
    print('NO')