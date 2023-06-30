n = int(input())

index = 1
power2 = 2
while power2 <= n:
    index += 1
    power2 *= 2

index -= 1
power2 //= 2
print(index, power2)
