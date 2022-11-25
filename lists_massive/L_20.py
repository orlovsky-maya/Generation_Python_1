# A = [1, 2, 3, 4, 5, 6,  7]
# A[::-2] = [10, 20, 30, 40]
# print(A)

# s = input()
# list = s.split()
# for i in range(0, len(list), 2):
#     print(list[i],end=' ')

#
# s = input().split()
# for elem in s:
#     if int(elem) % 2 == 0:
#         print(elem, end=' ')


s = input().split()
answer = []
previous_elem = s[0]

for current_elem in range(1, len(s)):
    if int(s[current_elem]) > int(previous_elem):
        answer.append(s[current_elem])
    previous_elem = int(s[current_elem])
print(*answer)
