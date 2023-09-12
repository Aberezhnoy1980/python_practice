class1 = int(input('Enter a first class students count: '))
class2 = int(input('Enter a second class students count: '))
class3 = int(input('Enter a third class students count: '))

# deskCount = class1 // -2 + class2 // -2 + class3 // -2
# print(-deskCount)

# deskCount = (class1 + 2 - 1) // 2 + (class2 + 2 - 1) // 2 + (class3 + 2 - 1) // 2
# print(deskCount)

deskCount = class1 // 2 + class1 % 2 + class2 // 2 + class2 % 2 + class3 // 2 + class3 % 2
print(deskCount)