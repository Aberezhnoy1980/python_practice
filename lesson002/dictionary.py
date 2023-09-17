# d = {}
# d = dict()
#
# d['q'] = 'qwerty'
# print(d)
#
# d['w'] = 'werty'
# print(d)
# print(d['q'])

# dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)
# print(dictionary['left'])
# print(dictionary['up'])
# dictionary['left'] = '<='
# print(dictionary['left'])
# print(dictionary['type'])
del dictionary['left']
print(dictionary.items()) # list of tuples
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))

for (k, v) in dictionary.items():
    print(k, v)

dictionary[895] = 98989
print(dictionary)
