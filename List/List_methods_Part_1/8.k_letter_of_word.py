answer = ''
sp = []
n = int(input())
for i in range(n):
    st = input()
    sp.append(st)
k = int(input())
for j in range(len(sp)):
    if len(sp[j]) >= k:
        el = sp[j]
        answer += el[k - 1]
print(answer)

