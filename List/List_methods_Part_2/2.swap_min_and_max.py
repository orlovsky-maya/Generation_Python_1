s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
minimum = min(s)
maximum = max(s)
position_min = s.index(minimum)
position_max = s.index(maximum)
s[position_min] = maximum
s[position_max] = minimum
print(*s, sep=' ')

# Second solution

s = input().split()
lst = []
for el in s:
    lst.append(int(el))
minimum = min(lst)
maximum = max(lst)
position_min = lst.index(minimum)
position_max = lst.index(maximum)
lst[position_min] = maximum
lst[position_max] = minimum
print(*lst, sep=' ')