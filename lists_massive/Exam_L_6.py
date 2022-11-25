# s = [list(i) for i in input().split()]
# for j in range(len(s)):
#     s[j].append(s[j][0])
#     s[j].append('ки')
#     del s[j][0]
#     ''.join(i[j])
# print(' '.join(s))


# s = [i for i in input().split()]
# new_s = []
# for j in range(len(s)):
#     sp_j = list(s[j])
#     sp_j.append(sp_j[0])
#     sp_j.append('ки')
#     del sp_j[0]
#     st_j = ''.join(sp_j)
#     new_s.append(st_j)
# print(*new_s)

print(*[i[1:] + i[0] + 'ки' for i in input().split()], sep=' ')