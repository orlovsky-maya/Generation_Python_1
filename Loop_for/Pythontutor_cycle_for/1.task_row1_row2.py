# Row - 1

a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i, end=' ')


# Row - 2

a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end=' ')

# Row - 3

a = int(input())
b = int(input())
for i in range(a % 2 + a - 1, b - 1,  -2):
    print(i, end=' ')
