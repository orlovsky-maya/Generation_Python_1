a = int(input())
b = int(input())
c = int(input())
if a > 0:
    a = a
else:
    a = 0
if b > 0:
    b = b
else:
    b = 0
if c > 0:
    c = c
else:
    c = 0
print(a + b + c)



a, b, c = int(input()), int(input()), int(input())
total = 0
if a > 0:
    total = total + a
if b > 0:
    total = total + b
if c > 0:
    total = total + c
print(total)


a, b, c = int(input()), int(input()), int(input())
if c < 0:
    c = 0
if b < 0:
    b = 0
if a < 0:
    a = 0
print(a + b + c)