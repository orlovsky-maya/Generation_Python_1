# s = []
# ind = 1
# for i in range(97, 123):
#     el = chr(i) * ind
#     s.append(el)
#     ind += 1
# print(s)

# s = []
# n = int(input())
# for i in range(n):
#     numbers = int(input())
#     el = numbers ** 3
#     s.append(el)
# print(s)

# s =[]
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         s.append(i)
# print(s)

s = []
n = int(input())
current_number = int(input())
for i in range(n - 1):
    summa = 0
    number = int(input())
    summa = current_number + number
    current_number = number
    s.append(summa)
print(s)





