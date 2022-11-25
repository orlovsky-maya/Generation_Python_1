# n = int(input())
# total = 0
# for i in range(n + 1):
#     for j in range(i):
#         total += 1
#         print(total, end='')
#     print()


# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for k in range(i - 1, 0, -1):
#         print(k, end='')
#     print()


a = int(input())
b = int(input())

current_total = 0
largest_total = a
largest_num = 0

for current_num in range(a, b + 1):

    # обнулить текущий score
    current_total = 0

    # calc curr score
    for denominator in range(1, current_num + 1):
        if current_num % denominator == 0:
            current_total += denominator

    # compare scores save largest
    if current_total >= largest_total:
        largest_total = current_total
        largest_num = current_num
print(largest_num, largest_total)


