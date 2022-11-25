a = input()
b = input()
c = input()
length_a = len(a)
length_b = len(b)
length_c = len(c)
d = min(length_a, length_b, length_c)
e = max(length_a, length_b, length_c)
if d == length_a and e == length_b:
    print(a)
    print(b)
elif d == length_a and e == length_c:
    print(a)
    print(c)
elif d == length_b and e == length_a:
    print(b)
    print(a)
elif d == length_b and e == length_c:
    print(b)
    print(c)
elif d == length_c and e == length_a:
    print(c)
    print(a)
elif d == length_c and e == length_b:
    print(c)
    print(b)
