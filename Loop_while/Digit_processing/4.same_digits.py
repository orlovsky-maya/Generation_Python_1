num = int(input())

the_same = True
left_num = num // 10
last_digit = num % 10

while left_num != 0:
    last_digit_1 = left_num % 10
    if last_digit_1 != last_digit:
        the_same = False
    left_num //= 10

if not the_same:
    print('NO')
else:
    print('YES')

# Second solution

n = int(input())
m = n % 10
answer = 'YES'
while n != 0:
    if m != n % 10:
        answer = 'NO'
    n = n // 10
print(answer)
