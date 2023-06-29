s = [i for i in input().split()]
new_s = []
for j in range(len(s)):
    sp_j = list(s[j])
    sp_j.append(sp_j[0])
    sp_j.append('ки')
    del sp_j[0]
    st_j = ''.join(sp_j)
    new_s.append(st_j)
print(*new_s)

# Second solution

words = [word[1:] + word[0] + "ки" for word in input().split()]

print(*words)



