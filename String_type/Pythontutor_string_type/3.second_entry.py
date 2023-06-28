s = input()
counter = s.count('f')
if counter == 1:
    print(-1)
elif counter == 0:
    print(-2)
else:
    i = s.find('f') + 1
    print(s.find('f', i))