s = [int(i) for i in input().split()]
i_maximum = s.index(max(s))
i_minimum = s.index(min(s))
s[i_minimum], s[i_maximum] = s[i_maximum], s[i_minimum]
print(*s)
