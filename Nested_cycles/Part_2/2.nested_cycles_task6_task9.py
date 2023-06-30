# Number Triangle 3

n = int(input())
total = 0
for i in range(n + 1):
    for j in range(i):
        total += 1
        print(total, end='')
    print()

# Number Triangle 4

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()

# Dividers-1
a = int(input())
b = int(input())

current_total = 0
largest_total = a
num = 0

for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            current_total += j
        if current_total >= largest_total:
            largest_total = current_total
            num = i
    current_total = 0
print(num, largest_total)

# Dividers-2
n = int(input())
denominator_counter = 0

for num in range(1, n + 1):
    denominator_counter = 0
    for denominator in range(1, num + 1):
        if num % denominator == 0:
            denominator_counter += 1
    print(num, '+' * denominator_counter, sep='')