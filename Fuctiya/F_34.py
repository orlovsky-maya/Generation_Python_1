def fib(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


n = int(input())
print(fib(n))
