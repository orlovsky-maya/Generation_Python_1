num = int(input())
a = num % 10
b = (num // 10) % 10
c = (num // 100) % 10
d = num // 1000
print('Цифра в позиции тысяч равна', d)
print('Цифра в позиции сотен равна', c)
print('Цифра в позиции десятков равна', b)
print('Цифра в позиции единиц равна', a)