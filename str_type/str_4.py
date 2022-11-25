# s = input()
# counter = 0
#
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         counter += 1
# print(counter)


s = input()
counter_gl = 0
counter_sg = 0

for c in s:
    if c in 'ауоыиэяюёеАУОЫИЭЯЮЕЁ':
        counter_gl += 1
    if c in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        counter_sg += 1
print('Количество гласных букв равно', counter_gl)
print('Количество согласных букв равно', counter_sg)


