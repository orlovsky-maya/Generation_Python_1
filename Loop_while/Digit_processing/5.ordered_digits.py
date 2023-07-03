num = int(input())
answer = 'YES'

while num != 0:
    last_digit = num % 10
    pre_last_digit = num // 10 % 10
    if last_digit > pre_last_digit != 0:
        answer = 'NO'
    num //= 10
print(answer)

# Other Solutions
# 1
n = int(input())
last = n % 10
flag = True

while n != 0:
    t = n % 10
    if last > t:
        flag = False
    else:
        last = t
    n //= 10
if flag is True:
    print('YES')
else:
    print('NO')

num = int(input())
answer = 'YES'

# 2

while num // 10 != 0:
    last_digit = num % 10
    pre_last_digit = num // 10 % 10
    if last_digit > pre_last_digit:
        answer = 'NO'
    num //= 10
print(answer)

# 3

n = int(input())
while n % 10 <= n % 100 // 10:
    n = n // 10
if n < 10:
    print('YES')
else:
    print('NO')
