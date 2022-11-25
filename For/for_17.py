n = int(input())
largest_1 = int(input())
largest_2 = int(input())
for i in range(n - 2):
    num = int(input())
    if largest_1 < num < largest_2:
        largest_1 = num
    elif largest_2 < num < largest_1:
        largest_2 = num
print(largest_1)
print(largest_2)

# n = int(input())
# largest = -1
# sub_largest = -1
#
# for i in range(n):
#     num = int(input())
#     if num > largest:
#         sub_largest = largest
#         largest = num
#     elif num > sub_largest:
#         sub_largest = num
#
# print(largest)
# print(sub_largest)
