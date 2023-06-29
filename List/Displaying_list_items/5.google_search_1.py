li = []
li_2 = []
n = int(input())
for i in range(n):
    s = input()
    li.append(s)
poisk = input()
for el in li:
    if poisk.lower() in el.lower():
        li_2.append(el)
print(*li_2, sep='\n')

