n = int(input())

counter = 0
for i in range(1, n + 1):
    counter = i ** 2
    if counter <= n:
        print(counter, end=' ')

n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1