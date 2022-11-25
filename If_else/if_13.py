x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')


x = int(input())
if -3 < x < 7:
    print('Не принадлежит')
else:
    print('Принадлежит')



x = int(input())
if not -3 < x < 7:
    print('Принадлежит')
else:
    print('Не принадлежит')
