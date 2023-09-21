# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

line = 'a a a b c a a d c d d'.split()
counter = 0
# for i in range(len(line)):
#     for j in range(i):
#         if line[j] == line[i]:
#             counter += 1
#             current_counter = counter
#             line[i] += '_' + str(current_counter)
#     print(line[i])

#  create frequency dictionary
freq_dict = {}

# for i in set(line):
#     freq_dict[i] = 0

for i in range(len(line)):
    if line[i] in freq_dict.keys():
        freq_dict[line[i]] += 1
        print(f'{line[i]}_{freq_dict[line[i]]}', end=' ')
    else:
        freq_dict[line[i]] = 0
        print(line[i], end=' ')

# print(freq_dict)

# for i in range(len(line)):
#     if line[i] in freq_dict:
#         temp = line[i]
#         line[i] += '_' + str(freq_dict[line[i]])
#         freq_dict[temp] -= 1
#     print(line[i], end=' ')
