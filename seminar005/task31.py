# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# n = abs(int(input('Enter index of Fibonacci number: ')))


# 1, 2, 3, 4, 5, 6, 7, 8
# 0, 1, 1, 2, 3, 5, 8, 13

# def get_fib_number_index(idx, f1=0, f2=1):
#     f = 0
#     if idx == 1:
#         return f1
#     elif idx in [2, 3]:
#         return f2
#     position = 2
#     while position < idx:
#         f = f1 + f2
#         position += 1
#         (f1, f2) = (f2, f)
#     return f


# def get_fib_number_index_rec(idx, f1=0, f2=1, position=2):
#     f = f1 + f2
#     if idx == 1:
#         return f1
#     elif idx in [2, 3]:
#         return f2
#     elif position < idx:
#         position += 1
#         # (f1, f2) = (f2, f)
#         print(f)
#         get_fib_number_index_rec(idx, f2, f, position)
#     return f


# print(get_fib_number_index_rec(n))
# print(get_fib_number_index(n))


def fib_rec(n):
    if n in (0, 1):
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


# print(fib_rec(abs(int(input('Enter index of Fibonacci number: ')))))
# 0, 1, 2, 3, 4
# 0, 1, 1, 2, 3
#               fib(4) ->       fib(3)         +         fib(2)         =          3
#                                 |                        |
#                        fib(2)   +   fib(1)      fib(1)   +   fib(0)
#                          |            |           |            |
#                   fib(1) + fib(0)     1           1            0
#                     |        |
#                     1        0
#  O(2**n)


def fib_line(n):
    f1, f2 = 0, 1
    for i in range(n):
        f = f1 + f2
        (f1, f2) = (f2, f)
    print(f1)


fib_line(abs(int(input('Enter index of Fibonacci number: '))))
#  O(n)
