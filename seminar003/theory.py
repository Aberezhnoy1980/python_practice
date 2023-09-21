# array - contain the same data types
# list - can contain different data types
# example = [1, 2.0, 'IVAN', True]
# print(*example) # * only n print

# set_1 = set()
# for i in 3, 56, 13, 26, 18, 9, 23:
#     set_1.add(i)
#
# print(set_1)

# dictionaries
data = {}
second_date = dict()

data['Kirill'] = 23
data['Marina'] = 20
print(data)
print(data['Kirill'])
print(data.keys())
# print(list(data.keys()))
# print(list(data.values()))

for i in data:  # <-> data.keys()
    print(i, end=' ')

print()

for i in data.values():  # <-> data.values()
    print(i, end=' ')
