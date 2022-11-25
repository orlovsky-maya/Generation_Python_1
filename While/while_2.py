text = input()
# while text != 'КОНЕЦ':
#     print(text)
#     text = input()


text = input()
while text != 'КОНЕЦ' and text != 'конец':
    print(text)
    text = input()


text = input()
total = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    total += 1
    text = input()
print(total)


num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())


num = int(input())
total = 0

while num >= 0:
    total += num
    num = int(input())
print(total)

num = int(input())
total = 0
while 5 >= num >= 0:
    if num == 5:
        total += 1
    num = int(input())
print(total)



