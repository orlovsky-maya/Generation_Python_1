num = int(input())
num_2 = str()

while num != 0:
    if num % 2 != 0:
        num_2 += str('1')
    else:
        num_2 += str('0')
    num //= 2
for i in range(len(num_2) - 1, -1, -1):
    print(num_2[i], end='')

# Second solution

n = int(input())
d = str()
while n != 0:
    d = str(n % 2) + d
    n //= 2
print(d)