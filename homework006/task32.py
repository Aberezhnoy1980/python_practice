# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

src_list = [int(i) for i in input('Enter list elements: ').split()]
min_value = int(input('Enter range min value: '))
max_value = int(input('Enter range max value: '))

print([i for i in range(len(src_list)) if min_value < src_list[i] < max_value])
