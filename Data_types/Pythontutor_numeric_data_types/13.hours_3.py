from math import floor

a = float(input())
time_h = floor(a / 30)
time_m = floor(60 * (a / 30 - time_h))
time_s = floor(60 * (a * 2 - time_h * 60 - time_m ))
print(time_h, time_m, time_s)
