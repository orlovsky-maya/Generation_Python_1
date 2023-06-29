s = []
n = int(input())
for i in range(n):
    numbers = int(input())
    s.append(numbers)
del s[1::2]
print(s)