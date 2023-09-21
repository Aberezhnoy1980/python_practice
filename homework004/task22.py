# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.

list_1 = set([int(input(f'Enter {i + 1} element: ')) for i in range(int(input('Enter first array size: ')))])
list_2 = set([int(input(f'Enter {i + 1} element: ')) for i in range(int(input('Enter second array size: ')))])
#
dst_list = list(list_1.intersection(list_2))  # List. In general, for some reason the set & list sorts itself
# dst_list = list_1.intersection(list_2)  # set

for i in range(len(dst_list) - 1):
    minPosition = i
    for j in range(i + 1, len(dst_list)):
        if dst_list[j] < dst_list[minPosition]:
            minPosition = j
    (dst_list[i], dst_list[minPosition]) = (dst_list[minPosition], dst_list[i])
    # temp = dst_list[i]
    # dst_list[i] = dst_list[minPosition]
    # dst_list[minPosition] = temp

print(dst_list)

# alt
# print(dst_list.sort())
