salary = int(input())
total = 0

while salary >= 25:
    salary -= 25
    total += 1
while 25 > salary >= 10:
    salary -= 10
    total += 1
while 10 > salary >= 5:
    salary -= 5
    total += 1
while 5 > salary >= 1:
    salary -= 1
    total += 1
print(total)