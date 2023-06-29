li = []
n = int(input())
for _ in range(n):
    number = int(input())
    li.append(number)
smallest = min(li)
largest = max(li)
for i in range(len(li)):
    if li[i] == smallest:
        smallest = i
del li[smallest]
for i in range(len(li)):
    if li[i] == largest:
        largest = i
del li[largest]
print(*li, sep='\n')
