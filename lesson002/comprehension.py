list_1 = []
for i in range(1, 11):
    list_1.append(i)
print(list_1)

list_2 = [i for i in range(1, 11)]
print(list_2)

list_3 = []
for i in range(1, 11):
    if i % 2 == 0:
        list_3.append(i)
print(list_3)

list_4 = [i for i in range(1, 11) if i % 2 == 0]
print(list_4)

list_5 = [(i, i ** 2) for i in range(1, 11) if i % 2 == 0]
print(list_5)
list_6 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_6)
