def get_fibonacci_row(n):
    print(0, 1, end=" ")
    f1 = 0
    f2 = 1
    for i in range(2, n):
        f = f1 + f2
        # f1 = f2
        # f2 = f
        (f1, f2) = (f2, f)
        print(f, end=" ")


get_fibonacci_row(10)
print()


def get_fibonacci_row_rec(n, f1=0, f2=1):
    if n == 0:
        return 0
    print(f1, end=' ')
    get_fibonacci_row_rec(n - 1, f2, f1 + f2)


get_fibonacci_row_rec(10)


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


print('\n' + str(0), end=' ')

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(*list_1)
