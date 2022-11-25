x = int(input())
y = int(input())

day = 1
while x < y:
    x = x * 0.1 + x
    day += 1

print(day)