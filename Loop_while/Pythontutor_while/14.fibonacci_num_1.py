n = int(input())
current_fib = 1
previous_fib = 0
index = 0

while n > index:
    index += 1
    current_fib, previous_fib = previous_fib, current_fib
    current_fib += previous_fib
print(previous_fib)
