li = []
n = int(input())
for i in range(n):
    s = input()
    if s not in li:
        li.append(s)
print(*li, sep='\n')