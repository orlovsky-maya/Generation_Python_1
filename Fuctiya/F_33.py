# def reverse_order(num):
#     if num == 0:
#         return num
#     n = int(input())
#     return reverse_order(n)
#
#
# number = int(input())
# print(reverse_order(number))


def reverse_order():
    n = int(input())
    if n != 0:
        reverse_order()
    print(n)
reverse_order()