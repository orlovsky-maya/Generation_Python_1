a = int(input())
b = int(input())

for i in range(a, b + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if 1 < counter < 3:
        print(i)

# Second solution

a = int(input())
b = int(input())
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)



