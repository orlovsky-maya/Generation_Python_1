# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

#
# s = input()
#
# for c in s:
#     print(ord(c), end=' ')


n = int(input())
s = input()
for c in s:
    if ord(c) - n < 97:
        i_c = chr(ord(c) - n + 26)
    else:
        i_c = chr(ord(c) - n)
    print(i_c, end='')