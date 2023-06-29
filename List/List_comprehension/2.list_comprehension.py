# List comprehension 1

n = int(input())
lst = [num ** 2 for num in range(1, n + 1)]
print(*lst, sep='\n')

# List comprehension 2

s = input().split()
lst = [int(i) ** 3 for i in s]
print(*lst)

# List comprehension 3
# One line 1

print(*[c for c in input().split()], sep='\n')

# List comprehension 4
# One line 2

print(*[c for c in list(input()) if c in '0123456789'], sep='')

# List comprehension 5
# One line 3

print(*[int(c) ** 2 for c in input().split() if int(c) % 2 == 0 and int(c) ** 2 % 10 != 4])
