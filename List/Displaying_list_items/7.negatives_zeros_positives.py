li_positive = []
li_zero = []
li_negative = []
n = int(input())
for i in range(n):
    number = int(input())
    if number > 0:
        li_positive.append(number)
    elif number == 0:
        li_zero.append(number)
    else:
        li_negative.append(number)
li_all = []
li_all.extend(li_negative)
li_all.extend(li_zero)
li_all.extend(li_positive)
print(*li_all, sep='\n')
