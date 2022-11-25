# num = int(input())
# if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# if c >= a <= b:
#     print(a)
# elif a >= b <= c:
#     print(b)
# else:
#     print(c)

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(3)
# elif a == b or b == c or c == a:
#     print(2)
# else:
#     print(0)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a == c) or (b == d):
#     print('YES')
# else:
#     print('NO')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (c == a + 1 or c == a - 1 or c == a) and (b == d or d == b + 1 or d == b - 1):
    print('YES')
else:
    print('NO')
