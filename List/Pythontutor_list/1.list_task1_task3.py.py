# Even indices

s = input()
lst = s.split()
for i in range(0, len(lst), 2):
    print(lst[i], end=' ')

# Even elements

s = input().split()
for elem in s:
    if int(elem) % 2 == 0:
        print(elem, end=' ')


s = input().split()
answer = []
previous_elem = s[0]

# More than previous

for current_elem in range(1, len(s)):
    if int(s[current_elem]) > int(previous_elem):
        answer.append(s[current_elem])
    previous_elem = int(s[current_elem])
print(*answer)
