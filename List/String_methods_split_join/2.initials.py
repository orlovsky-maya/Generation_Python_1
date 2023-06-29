s = input()
F_I_O = s.split()
init = []
for el in range(len(F_I_O)):
    data = list(F_I_O[el])
    init.append(data[0])
print('.'.join(init), end='.')
# Second solution

s = input()
F_I_O = s.split()
for i in F_I_O:
    print(i[0], end='.')

