num = int(input())

largest_second = num
largest = 0

while num != 0:
    if num > largest:
        largest_second = largest
        largest = num
    else:
        if num > largest_second:
            largest_second = num
    num = int(input())
print(largest_second)
