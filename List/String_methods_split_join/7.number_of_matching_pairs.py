s = input().split()
counter_pair = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            counter_pair += 1
print(counter_pair)
