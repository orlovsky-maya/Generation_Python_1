# Until END 1

text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()

# Until END 2

text = input()
while text != 'КОНЕЦ' and text != 'конец':
    print(text)
    text = input()

# Number of members

text = input()
total = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    total += 1
    text = input()
print(total)

# Loop_while divided

num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())

# Sum of numbers
num = int(input())
total = 0

while num >= 0:
    total += num
    num = int(input())
print(total)

# Number of fives
num = int(input())
total = 0
while 5 >= num >= 0:
    if num == 5:
        total += 1
    num = int(input())
print(total)



