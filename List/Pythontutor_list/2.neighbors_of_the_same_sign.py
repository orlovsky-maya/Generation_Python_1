s = input().split()
previous_elem = int(s[0])
counter = 0
for i in range(1, len(s)):
    if previous_elem >= 0:
        if int(s[i]) == previous_elem + 1 or int(s[i]) == previous_elem:
            counter += 1
            break
        else:
            previous_elem = int(s[i])
    else:
        if int(s[i]) == previous_elem - 1 or int(s[i]) == previous_elem:
            counter += 1
            break
        else:
            previous_elem = int(s[i])
if counter == 1:
    print(previous_elem, s[i])

# Second solution

a = [int(i) for i in input().split()]
for i in range(len(a) - 1):
    if a[i + 1] * a[i] > 0:
        print(a[i], a[i + 1], )
        break

# # Third solution

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break

