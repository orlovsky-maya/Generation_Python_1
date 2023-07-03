# Wrong decision

n = 4
count = 0
maximum = 999
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = i
            break
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# Corrected Solution

counter = 0
largest = -10 ** 8
for i in range(4):
    x = int(input())
    if x % 2 != 0:
        counter += 1
        if x > largest:
            largest = x
if counter > 0:
    print(counter)
    print(largest)
else:
    print('NO')