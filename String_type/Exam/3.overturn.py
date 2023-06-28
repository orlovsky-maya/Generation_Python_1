s = input()
first = s.find('h')
last = s.rfind('h')
srez = s[first:last + 1]
print(s[:first] + srez[::-1] + s[last + 1:])

