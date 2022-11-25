# s = input()
# words = s.split()
# print(*words, sep='\n')

# s = input()
# F_I_O = s.split()
# inicials = []
# for el in range(len(F_I_O)):
#     data = list(F_I_O[el])
#     inicials.append(data[0])
# print('.'.join(inicials), end='.')


s = input()
F_I_O = s.split()
for i in F_I_O:
    print(i[0], end='.')