fib = int(input())

if fib == 0:
    print(0)
else:
    fibon = False
    current_fib = 1
    previous_fib = 0
    n = 0
    while fib >= current_fib:
        n += 1
        current_fib, previous_fib = previous_fib, current_fib
        current_fib += previous_fib
        if fib == current_fib:
            fibon = True
    if fibon is True:
        print(n)
    else:
        print(-1)

# Second solution

fib = int(input())

if fib == 0:
    print(0)
else:
    current_fib = 1
    previous_fib = 0
    n = 1
    while fib >= current_fib:
        if fib == current_fib:
            print(n)
            break
        current_fib, previous_fib = previous_fib, current_fib
        current_fib += previous_fib
        n += 1
    else:
        print(-1)
