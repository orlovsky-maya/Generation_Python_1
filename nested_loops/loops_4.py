n = int(input())
denominator_counter = 0

for num in range(1, n + 1):
    denominator_counter = 0
    for denominator in range(1, num + 1):
        if num % denominator == 0:
            denominator_counter += 1
    print(num, '+' * denominator_counter, sep='')


n = int(input())
for i in range(1, n+1):
    print(i, end = '')
    for j in range(1, i+1):
        if i%j == 0:
            print('+', end = '')
    print()
