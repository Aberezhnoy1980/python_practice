# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# n = int(input())
# max_number = 1000 # max_number = n
# while n != 0: # 2 n % 10 != 0
#     n = int(input())
#     if max_number > n: # <
#         max_number = n
# print(max_number)
# 3 errors

# right decision
# n = int(input('Enter a number: '))
# max_element = n
# while n != 0:
#     n = int(input('Enter a number: '))
#     if n > max_element:
#         n = max_element
# print(max_element)

# n = int(input())
# max_number = -1
# while n < 0: #
#     n = int(input())
#     if max_number < n:
#         n = max_number #
# print(n) #

# right decision
n = int(input())
max_number = n
while n > 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
