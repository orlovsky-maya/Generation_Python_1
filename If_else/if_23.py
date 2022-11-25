m = int(input())
if m == 4 or m == 6 or m == 9 or m == 11:
    print(30)
elif m == 2:
    print(28)
else:
    print(31)



x = int(input())

if x == 2:
    print(28)
elif (x < 8 and x % 2 == 0) or (x > 7 and x % 2 != 0):
    print(30)
else:
    print(31)