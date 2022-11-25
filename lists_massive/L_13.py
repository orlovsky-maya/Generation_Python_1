# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers = numbers * 2
# numbers.insert(3, 25)
# print(numbers)


# s = input().split()
# for i in range(len(s)):
#     s[i] = int(s[i])
# minimum = min(s)
# maximum = max(s)
# position_min = s.index(minimum)
# position_max = s.index(maximum)
# s[position_min] = maximum
# s[position_max] = minimum
# print(*s, sep=' ')

s = input().split()

counter_a = s.count('a') + s.count('A')
counter_an = s.count('an') + s.count('An')
counter_the = s.count('the') + s.count('The')
print('Общее количество артиклей:', counter_the + counter_an + counter_a)