a = float(input())
time_h = a / 30
time_m = 60 * (time_h - a // 30)
print(time_m * 360 / 60)