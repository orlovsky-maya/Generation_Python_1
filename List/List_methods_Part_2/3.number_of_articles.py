s = input().split()

counter_a = s.count('a') + s.count('A')
counter_an = s.count('an') + s.count('An')
counter_the = s.count('the') + s.count('The')
print('Общее количество артиклей:', counter_the + counter_an + counter_a)