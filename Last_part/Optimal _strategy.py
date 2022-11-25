# import random
#
# #
# # left = 1
# # right = 100
# # middle = (left + right) // 2
# # while
# #
# #     def is_digit_more_then_zero(num):
# #         if num.isdigit():
# #             if int(num) > 0:
# #                 return True
# #         return False
# #
# # chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_.'
# # print(len(chars))
#
# text_to_encrypt = input()
#
# counter_of_not_letter = 0
# for word_to_encrypt in text_to_encrypt:
#     if word_to_encrypt.isalpha():
#         length_of_word = len(word_to_encrypt)
#     else:
#         length_of_word = len(word_to_encrypt)
#         for symbol in word_to_encrypt:
#             if not symbol.isalpha():
#                 counter_of_not_letter += 1
#     length_of_word = length_of_word - counter_of_not_letter
#     print(length_of_word)

my_answer = 'Gdb, qmgi. "Ciev" ku b tpzahrl!'
answer = 'Gdb, qmgi. "Ciev" ku b tpzahrl!'

if my_answer == answer:
    print('Yes')