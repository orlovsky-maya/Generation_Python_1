# n = int(input())
# list = [num ** 2 for num in range(1, n + 1)]
# print(*list, sep='\n')

# s = input().split()
# list = [int(i) ** 3 for i in s]
# print(*list)


# print(*[c for c in input().split()], sep='\n')


# print(*[c for c in list(input()) if c in '0123456789'], sep='')

print(*[int(c) ** 2 for c in input().split() if int(c) % 2 == 0 and int(c) ** 2 % 10 != 4])
