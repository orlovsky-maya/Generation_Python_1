s = []
n = int(input())
current_number = int(input())
for i in range(n - 1):
    number = int(input())
    summa = current_number + number
    current_number = number
    s.append(summa)
print(s)
