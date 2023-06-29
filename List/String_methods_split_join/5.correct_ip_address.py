s = input()
ip = s.split('.')
answer = 'ДА'
for el in ip:
    if int(el) < 0 or int(el) > 255:
        answer = 'НЕТ'
        break
print(answer)