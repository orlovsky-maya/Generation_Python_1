# #  в десятичную систему счисления
#
#
# from math import *
#
# base = int(input())
# number_2 = input()
# number_2 = number_2[::-1]
# num_10 = 0
#
# for i in range(len(number_2)):
#     num_10 += int(number_2[i]) * pow(base, i)
# print(int(num_10))


# из 16 й системы счисления в десятичную // нужно переделать

# base = int(input())
# number_16 = input()
# number_16 = number_16[::-1]
# num_10 = 0
#
# for i in range(len(number_16)):
#     if number_16[i].isdigit():
#         num_10 += int(number_16[i]) * pow(base, i)
#     else:
#         if number_16[i] == 'A':
#             num_10 += 10 * pow(base, i)
#         if number_16[i] == 'F':
#             num_10 += 15 * pow(base, i)
#
# print(int(num_10))


# из 10й системы счисления в другую

# base_new = int(input())
# number_10 = int(input())
# alphabet_16 = ['A', 'B', 'C', 'D', 'E', 'F']
# number_with_new_base = []
#
# while number_10 >= base_new:
#     remainder_of_the_division = number_10 % base_new
#     if remainder_of_the_division >= 10:
#         index_of_alphabet = remainder_of_the_division % 10
#         number_with_new_base.append(alphabet_16[index_of_alphabet])
#     else:
#         number_with_new_base.append(remainder_of_the_division)
#     number_10 //= base_new
# number_with_new_base.append(number_10)
# number_with_new_base.reverse()
# print(* number_with_new_base, sep='')

chars = [c for c in 'abcdefg']
print(chars)
