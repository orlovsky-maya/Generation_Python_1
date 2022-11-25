a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((c > a or c < a) and d == b) or ((d > b or d < b) and c == a):
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == c or b == d:
    print('YES')
else:
    print('NO')