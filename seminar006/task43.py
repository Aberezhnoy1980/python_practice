# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

numbers = [int(i) for i in input('Enter numbers: ').split()]
print(*numbers)
count_numbers = {}
for i in numbers:
    if i not in count_numbers: # count_numbers.keys()
        count_numbers[i] = 1
    else:
        count_numbers[i] += 1
print(sum([i // 2 for i in count_numbers.values()]))
# print({i: i + 1 for i in range(5)})