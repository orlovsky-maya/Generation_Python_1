s = [int(i) for i in input().split()]
counter = 0
previous_elem = s[0]
for i in range(1, len(s) - 1):
    if previous_elem < s[i] > s[i + 1]:
        counter += 1
    previous_elem = s[i]
print(counter)



