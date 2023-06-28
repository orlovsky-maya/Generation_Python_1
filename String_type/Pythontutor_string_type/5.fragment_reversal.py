s = input()
first = s.find('h')
last = s.rfind('h')
slc = s[first:last + 1]
print(s[:first] + slc[::-1] + s[last + 1:])
