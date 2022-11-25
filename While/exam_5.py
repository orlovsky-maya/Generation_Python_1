num = int(input())
while num > 99:
    last_digit = num % 10
    num //= 10
print(last_digit)



#
# n = int(input())
# num = n
# counter = 0
# while n != 0:
#     last_digit = n % 10
#     counter += 1
#     n //= 10
# print(num // 10 ** (counter - 3) % 10)