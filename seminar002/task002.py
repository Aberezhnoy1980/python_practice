a = abs(int(input('Enter any integer: ')))

first_fib = 0
second_fib = 1
position = 2

while second_fib < a:
    next_fib = first_fib + second_fib
    first_fib = second_fib
    second_fib = next_fib
    position += 1
    if second_fib > a:
        position = -1

print(position)
