# h = int(input())
# m = int(input())
# s = int(input())
# time = h + (m / 60) + (s / 3600)
# print(30 * time)
#
# a = float(input())
# time_h = a / 30
# time_m = 60 * (time_h - a // 30)
# print(time_m * 360 / 60)
a = float(input())
time_h = a // 30
time_m = 60 * (a / 30 - time_h)
time_s = 60 * (time_m - int(time_m))
print(int(time_h), int(time_m), int(time_s))

from math import floor

a = float(input())
time_h = floor(a / 30)
time_m = floor(60 * (a / 30 - time_h))
time_s = floor(60 * (a * 2 - time_h * 60 - time_m ))
print(time_h, time_m, time_s)