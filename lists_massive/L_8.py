li_1 = []
li_2 = []
li_3 = []
n = int(input())
for i in range(n):
    s_n = input()
    li_1.append(s_n)
k = int(input())
for j in range(k):
    s_k = input()
    li_2.append(s_k)
for el_n in li_1:
    counter = 0
    for el_k in li_2:
        if el_k.lower() in el_n.lower():
            counter += 1
            if counter == k:
                li_3.append(el_n)
print(*li_3, sep='\n')



