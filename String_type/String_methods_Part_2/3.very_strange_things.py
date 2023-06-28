n = int(input())
counter_s = 0
for i in range(n):
    s = input()
    counter_11 = s.count('11')
    if counter_11 >= 3:
        counter_s += 1
print(counter_s)