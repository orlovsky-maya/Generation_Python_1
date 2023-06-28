s = input()

first_i = s.find('h')
last_i = s.rfind('h') + 1
print(s[:first_i] + s[last_i:])