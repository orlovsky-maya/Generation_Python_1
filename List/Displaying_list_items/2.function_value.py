li_numbers = []
li_function = []
n = int(input())
for i in range(n):
    numbers = int(input())
    li_numbers.append(numbers)
    el_function = numbers ** 2 + 2 * numbers + 1
    li_function.append(el_function)
print(*li_numbers, sep='\n')
print()
print(*li_function, sep='\n')

