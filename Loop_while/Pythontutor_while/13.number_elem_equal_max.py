num = int(input())
largest = 1
counter = 0

while num != 0:
    if num > largest:
        largest = num
        counter = 1
    elif num == largest:
        counter += 1
    num = int(input())
print(counter)

