# def reverse_order(num):
#     if num // 10 == 0:
#         return 0
#     return reverse_order(num % 10)
#
#
# num = int(input())
# numbers = ''
# while num != 0:
#     numbers += str(num)
#     num = int(input())
# numbers += '0'
# print(reverse_order(int(numbers)))