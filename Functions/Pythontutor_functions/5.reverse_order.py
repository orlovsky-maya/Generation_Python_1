def reverse_order():
    n = int(input())
    if n != 0:
        reverse_order()
    print(n)


reverse_order()
