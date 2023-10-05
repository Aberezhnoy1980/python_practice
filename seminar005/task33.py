# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
from random import random


# size = abs(int(input('Enter journal size: ')))
# vasiliy_journal = [int(random() * size) for i in range(size)]
# print(vasiliy_journal)


# def get_new_journal(journal):
#     max_value = journal[0]
#     min_value = journal[0]
#     for i in journal:
#         if i > max_value:
#             max_value = i
#         elif i < min_value:
#             min_value = i
#     # new_journal = [min_value for i in journal if i == max_value]
#     new_journal = []
#     for i in vasiliy_journal:
#         if i == max_value:
#             new_journal.append(min_value)
#         else:
#             new_journal.append(i)
#
#     print(*new_journal)


# def get_new_journal1(journal):
#     max_value = journal[0]
#     min_value = journal[0]
#     for i in journal:
#         if i > max_value:
#             max_value = i
#         elif i < min_value:
#             min_value = i
#     new_journal = [min_value if i == max_value else i for i in journal]
#     print(*new_journal)


def get_new_journal2():
    n = int(input('Enter score count: '))
    marks = [int(i) for i in input('Enter scores: ').split()[:n]]
    print(*[min(marks) if i == max(marks) else i for i in marks])


def get_new_journal3():
    n = int(input('Enter score count: '))
    marks = [int(random() * n) for i in range(n)]
    print(*marks)
    print(*[min(marks) if i == max(marks) else i for i in marks])


# get_new_journal(vasiliy_journal)
# get_new_journal1(vasiliy_journal)
# get_new_journal2()
get_new_journal3()
