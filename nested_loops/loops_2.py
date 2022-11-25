# for n in range(1, 13):
#     for k in range(1, 12):
#         for m in range(1, 11):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print('n =', n, 'k =', k, 'm = ', m)


# for b in range(1, 11):
#     for k in range(1, 21):
#         for t in range(1, 201):
#             if 10 * b + 5 * k + 0.5 * t == 100:
#                 if b + k + t == 100:
#                     print('b =', b, 'k =', k, 't =', t)
import math

for a in range(1, 151):
    for b in range(a, 100):
        for c in range(b, 100):
            for d in range(c, 100):
                total = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = math.sqrt(total)
                if total == e ** 5:
                    print(a + b + c + d + e)


for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                for e in range(1, 150):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a + b + c + d + e)