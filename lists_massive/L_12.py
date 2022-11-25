# s = input()
# ip_adress = s.split('.')
# answer = 'ДА'
# for el in ip_adress:
#     if int(el) < 0 or int(el) > 255:
#         answer = 'НЕТ'
#         break
# print(answer)


# s_text = input()
# s_separator = input()
# print(s_separator.join(list(s_text)))
#



s = input().split()
counter_pair = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            counter_pair += 1
print(counter_pair)