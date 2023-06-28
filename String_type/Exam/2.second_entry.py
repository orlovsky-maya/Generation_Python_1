s = input()

if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    s = s.replace('f', '1', 1)
    print(s.find('f'))

