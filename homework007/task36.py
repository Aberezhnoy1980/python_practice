# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения

def print_operation_table(operation, num_rows=6, num_columns=6):
    if num_rows < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print(*[i for i in range(1, num_rows + 1)])
        for i in range(1, num_rows):
            print(f'{i + 1} ', end='')
            for j in range(1, num_columns):
                print(f'{operation(i + 1, j + 1)}', end=' ')
                if j == num_columns - 1:
                    print()


# print_operation_table(lambda x, y: x * y)

# print_operation_table(lambda x, y: x / y, 4, 4)

# print_operation_table(lambda x, y: x - y, 5, 5)

# print_operation_table(lambda x, y: x + y, 4, 4)

# print_operation_table(lambda x, y: x + y, 1, 2)


# alt
# def print_operation_table1(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         header = ' '.join([str(i) for i in range(1, num_columns + 1)])
#         print(header)
#         for i in range(2, num_rows + 1):
#             row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
#             print(' '.join(row))