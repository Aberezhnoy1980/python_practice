# C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

list_of_strings = input('Enter numbers: ').split()
print(list_of_strings)

list_of_integers = [int(x) for x in list_of_strings]
print(list_of_integers)

#  alt
list_of_strings = list(map(int, list_of_strings))
print(list_of_strings)
