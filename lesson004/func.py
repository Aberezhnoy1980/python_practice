# def f(x):
#     return x * x
#
#
# print(f(5))
# print(type(f))
#
# a = f
# print(type(a))
# print(a(5))


def calc1(a):
    return a + a


def calc2(a):
    return a * a


def math(op, x):
    print(op(x))


math(calc1, 5)
math(calc2, 5)
