s = [int(i) for i in input().split()]
answer = []
for i in range(len(s)):
    counter = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            counter += 1
    if counter == 1:
        answer.append(s[i])
print(*answer)

# Reference solution 1

a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')

# Reference solution 2

a = [int(i) for i in input().split()]
for i in a:
    if a.count(i) == 1:
        print(i, end=' ')

