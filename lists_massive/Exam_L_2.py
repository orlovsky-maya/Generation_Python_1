L = [int(l) for l in input().split()]
M = [int(m) for m in input().split()]
list_summa = []
for i in range(len(L)):
    summa = L[i] + M[i]
    list_summa.append(summa)
print(*list_summa)

