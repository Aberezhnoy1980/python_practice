# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

src_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3

# for i in range(len(src_list)):
#     print(src_list[-k + i])

# alt decision
# print(src_list[k - 1:len(src_list)])

n = int(input('Enter k offset size: ')) % len(src_list)
if n == 0:
    print(src_list)
else:
    print(src_list[-n:] + src_list[:len(src_list) - n])
