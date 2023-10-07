# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).

numbers = [int(i) for i in input('Enter numbers: ').split()]
print(numbers)

print({i: i ** 2 for i in numbers if i % 2 == 0})

#  alt
res = list()
for i in numbers:
    if i % 2 == 0:
        res.append((i, i ** 2))

print(res)


# lambda
def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


result = select(int, numbers)
print(result)
result = where(lambda x: x % 2 == 0, result)
print(result)
result = list(select(lambda x: (x, x ** 2), result))
print(result)

# map
result = map(int, numbers)
print(result)
result = where(lambda x: x % 2 == 0, result)
print(result)
result = list(map(lambda x: (x, x ** 2), result))
print(result)

# map + filter
result = map(int, numbers)
result = filter(lambda x: x % 2 == 0, result)
result = list(map(lambda x: (x, x ** 2), result))
print(result)
