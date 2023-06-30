n = int(input())
num = n
counter = 0
while n != 0:
    last_digit = n % 10
    counter += 1
    n //= 10
print(num // 10 ** (counter - 2) % 10)

# Second solution

n = int(input())
while n > 99:
    n //= 10
print(n % 10)