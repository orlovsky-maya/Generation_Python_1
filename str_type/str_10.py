# n = int(input())
# counter_s = 0
# for i in range(n):
#     s = input()
#     counter_11 = s.count('11')
#     if counter_11 >= 3:
#         counter_s += 1
# print(counter_s)


s = input()
counter = 0
for c in s:
    if c in '0123456789':
        counter += 1
print(counter)

s = input()
counter = 0
for i in range(10):
    counter += s.count(str(i))
print(counter)