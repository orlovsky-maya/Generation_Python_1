n = input().split('#')
n.remove('')
for i in range(len(n)):
    n[i] = int(n[i])
for el in range(n[i]):
    s = input()
    if '#' in s:
        s = list(s)
        position = s.index('#')
        del s[position:]
        s = ''.join(s)
        print(s.rstrip())
    else:
        print(s.rstrip())

# Second solution

n = input().split('#')
n.remove('')
for el in range(int(n[0])):
    s = input()
    if '#' in s:
        s = list(s)
        position = s.index('#')
        del s[position:]
        s = ''.join(s)
        print(s.rstrip())
    else:
        print(s.rstrip())

# Reference solution

n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())