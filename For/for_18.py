# counter = 0
#
# for i in range(10):
#     num = int(input())
#     if num % 2 == 0:
#         counter += 1
# if counter == 10:
#     print('YES')
# else:
#     print('NO')
flag = True
for i in range(10):
    num = int(input())
    if num % 2 != 0:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')
#
# flag = 'YES'
# for _ in range(10):
#     a = int(input())
#     if a % 2 != 0:
#         flag = 'NO'
# print(flag)
