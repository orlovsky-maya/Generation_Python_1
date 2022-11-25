s = [int(i) for i in input().split()]
summa = sum(s)
st = [str(j) for j in s]
print('+'.join(st), '=', summa, sep='')

number = [i for i in input().split('-')]
if number[0] == 7:
    del number[7]
if len(number[0]) == 3 and len(number[1]) == 3 and len(number[2]) == 4:
    numbers_st = ' '.join(number)
    if not numbers_st.isdigit():
        print('NO')
    else:
        print('YES')