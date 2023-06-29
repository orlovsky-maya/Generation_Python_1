s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
print(*s, sep=' ')
s.sort(reverse=True)
print(*s, sep=' ')

# Second solution

s = input().split()
lst = []
for i in range(len(s)):
    lst.append(int(s[i]))
lst.sort()
print(*lst, sep=' ')
lst.sort(reverse=True)
print(*lst, sep=' ')

# Reference solution

seq = []
for el in input().split():
    seq.append(int(el))

seq.sort()
print(*seq)

seq.reverse()
print(*seq)