next_num = int(input())
previous_num = next_num
counter = 0

while next_num != 0:
    if next_num > previous_num:
        counter += 1
    previous_num = next_num
    next_num = int(input())
print(counter)

