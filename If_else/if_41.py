n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n > m:
    if x < y:
        if m - x <= n - y:
            if (m - x) > x:
                print(x)
            else:
                print(m - x)
        elif m - x > n - y:
            if (n - y) < x:
                print(n - y)
            else:
                print(x)
    elif y < x:
        if m - x >= n - y:
            if (n - y) > y:
                print(y)
            else:
                print(n - y)
        elif m - x < n - y:
            if (m - x) > y:
                print(y)
            else:
                print(m - x)
elif m > n:
    if x < y:
        if n - x <= m - y:
            if (n - x) > x:
                print(x)
            else:
                print(n - x)
        elif n - x >= m - y:
            if (m - y) > x:
                print(x)
            else:
                print(m - y)
    if x > y:
        if n - x <= m - y:
            if (n - x) > y:
                print(y)
            else:
                print(n - x)
        elif n - x >= m - y:
            if (m - y) > x:
                print(x)
            else:
                print(m - y)
