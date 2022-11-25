# n = int(input())
#
# largest_step = 1
# current_index = 0
# high_index = 0
#
# while largest_step <= n:
#     if 2 ** current_index >= largest_step:
#         high_index = current_index
#         largest_step = 2 ** current_index
#     current_index += 1
# print(high_index, 2 ** high_index)


n = int(input())

index  = 1
power2 = 2
while power2 <= n:
    index += 1
    power2 *= 2

index -= 1
power2 //= 2
print(index, power2)

# n = int(input())
#
# index = 0
#
# while 2 ** index <= n:
#     index += 1
# print((index-1), 2 ** (index-1))