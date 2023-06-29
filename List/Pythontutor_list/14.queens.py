vert_s = []
horizon_s = []
not_cross = True
for _ in range(8):
    vert, horizon = [int(p) for p in input().split()]
    vert_s.append(vert)
    horizon_s.append(horizon)
for i in range(8):
    for j in range(i + 1, 8):
        if vert_s[i] == vert_s[j] or horizon_s[i] == horizon_s[j] or abs(vert_s[i] - vert_s[j]) == abs(
                horizon_s[i] - horizon_s[j]):
            not_cross = False
            break
if not not_cross:
    print('YES')
else:
    print('NO')
