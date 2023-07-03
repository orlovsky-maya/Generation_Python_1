from math import factorial
n = int(input())
total = 0

for n in range(1, n + 1):
    total += factorial(n)
print(total)

# Second solution

n = int(input())

total_fak_num = 0

for n in range(1, n + 1):
    fak_num = 1
    for num in range(1, n + 1):
        fak_num *= num
    total_fak_num += fak_num
print(total_fak_num)