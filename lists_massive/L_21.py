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

