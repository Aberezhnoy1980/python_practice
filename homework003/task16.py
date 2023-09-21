# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
list_1 = [int(input(f'Enter {i + 1} element: ')) for i in range(int(input('Enter array size: ')))]
x = int(input('Enter a number for search: '))

count = 0
for i in range(len(list_1)):
    if list_1[i] == x:
        count += 1
print(count)

#  alt decision
count = 0
for i in list_1:
    if i == x:
        count += 1
print(count)
