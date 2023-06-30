# Examples

def factorial(n):
    res = 1
    for j in range(1, n + 1):
        res *= j
    return res


for i in range(1, 6):
    print(i, '! = ', factorial(i), sep='')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
