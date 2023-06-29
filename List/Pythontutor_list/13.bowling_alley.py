spisok_kegli = []
count_kegli_N, count_throw_K = [int(count) for count in input().split()]
for number_of_kegli in range(1, count_kegli_N + 1):
    spisok_kegli.append(number_of_kegli)
for killed_kegli in range(count_throw_K):
    l_i, r_i = [int(i) for i in input().split()]
    srez = spisok_kegli[l_i - 1:r_i]
    for elem_srez in range(len(srez)):
        if srez[elem_srez] in spisok_kegli:
            position = spisok_kegli.index(srez[elem_srez])
            spisok_kegli[position] = '.'
for elem_of_kegli in range(len(spisok_kegli)):
    if spisok_kegli[elem_of_kegli] != '.':
        spisok_kegli[elem_of_kegli] = 'I'
print(*spisok_kegli, sep='')

# Reference solution

n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))



