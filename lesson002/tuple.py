# t = ()
#
# print(type(t))
#
# t = (1, 5, 3,)
#
# print(type(t))

# v = [1, 8, 9]
# print(*v)
# print(type(v))

# v = tuple(v)
# print(*v)
# print(type(v))

# a = 1
# b = 2

# a, b = 1, 2
#
# a = b = 12

# a, b, c = v
#
# print(a, b, c)
# print(v)

t = (1, 2, 3, 5,)
print(t[1])

# for i in t:
#     print(i, end=' ')
#
# print()
#
# for i in range(len(t)):
#     print(t[i], end=' ')

# t[0] = 2 TypeError: 'tuple' object does not support item assignment

list_1 = [1, 2, 3, 5]
list_1[2] = 2
print(list_1, end=' ')
