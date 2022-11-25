from math import *

def distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

x_1, y_1, x_2, y_2 = float(input()), float(input()), float(input()), float(input())
print(distance(x_1, y_1, x_2, y_2))