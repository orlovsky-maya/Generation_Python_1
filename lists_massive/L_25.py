s = [int(i) for i in input().split()]
growth_petya = int(input())
new_s = []
for i in range(len(s)):
    if s[i] >= growth_petya:
        new_s.append(s[i])
    else:
        break
print(len(new_s) + 1)

