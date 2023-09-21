# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
source_list = [int(input(f'Enter {i + 1} number: ')) for i in range(int(input('Enter number count: ')))]

count = len(source_list)
for i in range(len(source_list)):
    for j in range(i + 1, len(source_list)):
        if source_list[i] == source_list[j]:
            count -= 1
print(count)

# alt decision
# print(len(set(source_list)))
