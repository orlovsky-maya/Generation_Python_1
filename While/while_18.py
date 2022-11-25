# from math import sqrt
# x = int(input())
#
# counter = 0
# total = 0
# total_squares = 0
#
# while x != 0:
#     counter += 1
#     total += x
#     average = total / counter
#     squares = (x - average) ** 2
#     total_squares += squares
#     x = int(input())
# print(sqrt(total_squares / (counter - 1)))



from math import sqrt

x = int(input())

total = 0
total_squares = 0

n = 0
while x != 0:
    n += 1
    total += x
    total_squares += x ** 2
    x = int(input())
print(sqrt((total_squares - total ** 2 / n) / (n - 1)))
