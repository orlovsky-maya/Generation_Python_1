s = [int(i) for i in input().split()]
counter = 1
previous_elem = s[0]
for i in range(1, len(s)):
    if s[i] != previous_elem:
        counter += 1
    previous_elem = s[i]
print(counter)