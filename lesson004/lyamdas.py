def math(func, arg1, arg2):
    print(func(arg1, arg2))


summator = lambda a, b: a + b
print(summator(5, 45))

math(lambda a, b: a * b, 2, 3)
