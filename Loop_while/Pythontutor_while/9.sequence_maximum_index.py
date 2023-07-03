num = int(input())
largest = 1
current_index = -1
index = -1

while num != 0:
    current_index += 1
    if num > largest:
        largest = num
        index = current_index
    num = int(input())
print(index)