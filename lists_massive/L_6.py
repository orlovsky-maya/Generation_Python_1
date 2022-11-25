# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# li_numbers_2 = []
# for num in numbers:
#     li_numbers_2.append(num ** 2)
# print(sum(li_numbers_2))

# li_numbers = []
# li_function = []
# n = int(input())
# for i in range(n):
#     numbers = int(input())
#     li_numbers.append(numbers)
#     el_function = numbers ** 2 + 2 * numbers + 1
#     li_function.append(el_function)
# print(*li_numbers, sep='\n')
# print()
# print(*li_function, sep='\n')

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
