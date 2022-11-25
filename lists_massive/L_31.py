s = [int(i) for i in input().split()]
counter = 0
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            counter += 1
print(counter)
