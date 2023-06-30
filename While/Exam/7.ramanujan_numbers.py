for a in range(1, 33):
    for b in range(1, 33):
        num_1 = a ** 3 + b ** 3
        for c in range(1, 33):
            for d in range(1, 33):
                num_2 = c ** 3 + d ** 3
                if a != c and a != d and b != c and b != d:
                    if num_1 == num_2:
                        print(num_1)

# Second solution

for a in range(4, 33):
    for c in range(3, a):
        for d in range(2, c):
            for b in range(1, d):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    print(a ** 3 + b ** 3)