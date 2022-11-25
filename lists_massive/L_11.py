# s = input()
# words = s.split('\\')
# print(*words, sep='\n')

s = input()
numbers = s.split()
for el in numbers:
    print(int(el) * '+')