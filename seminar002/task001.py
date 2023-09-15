n = abs(int(input('Enter any integer: ')))
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print(factorial)