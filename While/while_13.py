# num = int(input())
# counter = 0
#
# while num != 0:
#     counter += 1
#     num = int(input())
# print(counter)


# num = int(input())
# # total = 0
# #
# # while num != 0:
# #     total += num
# #     num = int(input())
# # print(total)

#
# num = int(input())
# counter = 0
# total = 0
#
# while num != 0:
#     counter += 1
#     total += num
#     num = int(input())
# print(total / counter)


# num = int(input())
# largest = 1
#
# while num != 0:
#     if num >= largest:
#         largest = num
#     num = int(input())
# print(largest)


# num = int(input())
# largest = 1
# current_index = -1
# index = -1
#
# while num != 0:
#     current_index += 1
#     if num > largest:
#         largest = num
#         index = current_index
#     num = int(input())
# print(index)


max = 0
index_of_max = -1
element = -1
len = 0
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)
