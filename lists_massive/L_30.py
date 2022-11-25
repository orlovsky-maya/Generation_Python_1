s = [int(i) for i in input().split()]
s_2 = [j for j in input().split()]
k = int(s_2[0])
c = s_2[1]
s.insert(k, c)
print(*s)


a = [int(s) for s in input().split()]

# обратите внимание на множественное присваивание:
# справа от "=" стоит список из двух элементов,
# а слева -- две переменные,
# поэтому так делать можно
k, C = [int(s) for s in input().split()]

a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))