# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно
# два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

garden_bed = [int(input(f'Enter harvest from the {i + 1} bush: '))
              for i in range(int(input('Enter bush count in the bed: ')))]

max_harvested = 0

if len(garden_bed) < 3:
    max_harvested = sum(garden_bed)
else:
    for i in range(1, len(garden_bed)):
        if i == len(garden_bed) - 1:
            current_harvested = garden_bed[i - 1] + garden_bed[i] + garden_bed[0]
        else:
            current_harvested = garden_bed[i - 1] + garden_bed[i] + garden_bed[i + 1]
        if current_harvested > max_harvested:
            max_harvested = current_harvested
# print(max_harvested)


#  alt

print(max(garden_bed[i - 2] + garden_bed[i - 1] + garden_bed[i] for i in range(len(garden_bed))))

