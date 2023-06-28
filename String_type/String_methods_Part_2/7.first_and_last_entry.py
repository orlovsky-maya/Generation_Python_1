s = input()
counter = s.count('f')

if counter == 1:
    print(s.find('f'))
elif counter > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')
