# print(5)

# n = 1.89

# print(n)

# n = 'fddf'

# print(n)

# n1 = "sasasas"

# a = 'st\'r'
# b = 'str'
# c = 'st"sdsdsdsdsd"r'
"""
print(type(a))
"""
# print(a, b, c)

# a = 5
# b = 5.89
# c = 'hello'

# print(a, b, c)
# print(a, ' - ', b, ' - ', c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))

# print("Enter first string: ")
# a = input()
# print(a)

# b = input('Enter second number: ')
# print(b)

# print(a, ' + ', b, ' = ', a + b)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))
# c = str(c)
# print(c + '89')
# print(type(c))
# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))

# print(f"a + b = {a + b}")
# print(f"{a} + {b} = {a + b}")

# a = 5.89
# b = 6.98
# print(round(a*b, 2))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5 (float)
# iter //= 5 # iter = iter // 5 (int)
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5 (POW)

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)


# username = input('Enter name: ')
# if username == 'Masha':
#     print('Hello, Masha!')
# elif username == 'Marina':
#     print('Marina hi! How are you?')
# elif username == 'Ilnar':
#     print('Ilnar are top)')
# else: print('Hello,', username)

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa += x
#     n = n // 10
# print(summa)

# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i += 1
# else:
#     print('It\'s enough!')
# print(i)

# n = int(input('Enter a number: '))
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

# r = range(5)
# r1 = range(2, 5)
# r2 = range(0, -5)
# r3 = range(1, 10, 2)
# r4 = range(100, 0, -20)

# ranges = [r, r1, r2, r3, r4]

# for i in ranges:
#     print()
#     for j in i:
#         print(j)

# a = 'qwerty'

# for i in a:
#     print(i)

# print()

# for i in range(len(a)):
#     print(a[i])

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё', 'ЕЩЁ'))

text = "Сьешь ещё этих мягких французских булок"
print(text[0])
# print(text[1])
# print(text[len(text) - 1])
# print(text[-5])
# print(text[:])
# print(text[:2])
# print(text[len(text) - 2 :])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9] + text[-5] + text[:2]
