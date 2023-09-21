# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

data = [int(input(f'Enter {i + 1} element: ')) for i in range(int(input('Enter array size: ')))]
x = int(input('Enter comparison value '))
search_number = data[0]
diff = x - search_number
for i in data:
    if abs(x - i) < diff:
        diff = x - i
        search_number = i
print(search_number)
