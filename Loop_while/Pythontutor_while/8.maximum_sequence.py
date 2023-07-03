num = int(input())
largest = 1

while num != 0:
    if num >= largest:
        largest = num
    num = int(input())
print(largest)
