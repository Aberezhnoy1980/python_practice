# Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве выведет количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

list_1 = [int(i) for i in input('Enter numbers: ').split()[:abs(int(input('Enter array size: ')))]]
print(*list_1)

list_2 = [list_1[i] for i in range(1, len(list_1) - 1) if list_1[i] > list_1[i - 1] and list_1[i] > list_1[i + 1]]
print(len(list_2))

#  alt
print(sum([list_1[i - 1] < list_1[i] > list_1[i + 1]
           for i in range(1, len(list_1) - 1)]))
