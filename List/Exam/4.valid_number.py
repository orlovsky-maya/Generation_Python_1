number = [i for i in input().split('-')]
if number[0] == '7':
    del number[0]
if len(number[0]) == 3 and len(number[1]) == 3 and len(number[2]) == 4:
    numbers_st = ''.join(number)
    if numbers_st.isdigit():
        print('YES')
    else:
        print('NO')
else:
    print('NO')