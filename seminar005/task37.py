# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).


def get_reverse_sequence(n):
    if n == 0:
        return ''
    x = input(f'Enter {n - (n - 1)} element: ')
    return get_reverse_sequence(n - 1) + f' {x}'


print(get_reverse_sequence(abs(int(input('Enter any integer: ')))))
# get_reverse_sequence(2) -> x = 3 -> get_reverse_sequence(1) + ' 3' = ' 4' + ' 3'
#                                                 |
#                                     get_reverse_sequence(0) + ' 4' = '' + ' 4'
#                                                 |
#                                                 ''
