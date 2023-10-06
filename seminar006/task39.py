# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит  число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов
# во втором массиве. Затем элементы второго массива

list_1 = [abs(int(input(f'Enter {i + 1} element: '))) for i in range(abs(int(input('Enter n-array size: '))))]
list_2 = [abs(int(input(f'Enter {i + 1} element: '))) for i in range(abs(int(input('Enter m-array size: '))))]

for i in range(len(list_1)):
    if list_1[i] not in list_2:
        print(f'{list_1[i]} ', end='')

# alt
list_3 = [i for i in list_1 if i not in list_2]
print('\n\b', *list_3)