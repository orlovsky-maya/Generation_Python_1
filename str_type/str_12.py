s = input()
counter_max = 0
answer = 0
for c in s:
    if s.count(c) >= counter_max:
        counter_max = s.count(c)
        answer = c
print(answer)