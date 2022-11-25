# n = input()
# s = 0
# while n > 10:
#     if n % 2 == 1:
#         s = n % 10
#     n //= 10
# print(s)

n = int(input())
total = 0

while n != 0:
    last_digit = n % 10
    if last_digit % 2 == 0:
        total += last_digit
    n //= 10
if total > 0:
    print(total)
else:
    print(0)