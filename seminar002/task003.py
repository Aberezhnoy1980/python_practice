watermelons_count = int(input('Enter a number of watermelons: '))
# watermelons = []
# for i in range(watermelons_count):
#     watermelons.append(int(input(f'Enter {i + 1} watermelon weight: ')))
# print(watermelons)
w = int(input('Enter watermelon weight: '))
max_weight, min_weight = w, w
for i in range(watermelons_count - 1):
    w = int(input(f'Enter {i + 1} watermelon weight: '))
    if max_weight < w:
        max_weight = w
    elif min_weight > w:
        min_weight = w

# min_weight = watermelons[0]
# max_weight = watermelons[0]
#
# for i in watermelons:
#     if i < min_weight:
#         min_weight = i
#     elif i > max_weight:
#         max_weight = i

# w1 = 1
# w2 = 22
# w3 = -3
#
# min_weight = w1
# max_weight = w1
#
# for i in w1, w2, w3:
#     if i < w1:
#         min_weight = i
#     elif i > max_weight:
#         max_weight = i

print(min_weight, max_weight)