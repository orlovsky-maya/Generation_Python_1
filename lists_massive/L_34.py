vert_s = []
goriz_s = []
not_cross = True
for _ in range(8):
    vert, goriz = [int(p) for p in input().split()]
    vert_s.append(vert)
    goriz_s.append(goriz)
for i in range(8):
    for j in range(i + 1, 8):
        if vert_s[i] == vert_s[j] or goriz_s[i] == goriz_s[j] or abs(vert_s[i] - vert_s[j]) == abs(
                goriz_s[i] - goriz_s[j]):
            not_cross = False
            break
if not_cross != True:
    print('YES')
else:
    print('NO')
