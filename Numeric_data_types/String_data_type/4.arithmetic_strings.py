a = input()
b = input()
c = input()
length_a = len(a)
length_b = len(b)
length_c = len(c)
d = min(length_a, length_b, length_c)
e = max(length_a, length_b, length_c)
f = (length_a + length_b + length_c) - (d + e)
if e - f == f - d:
    print('YES')
else:
    print('NO')
