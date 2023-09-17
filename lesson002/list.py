# list_1 = []
# list_2 = list()
# print(list_1)
# list_3 = [1, 2, 3, 8]
# print(list_3)
# print(*list_3)

# for i in list_3:
#     print(i)

# print(len(list_3))

# print(list_3[-1])

# list_4 = [1, 5]
# # print(list_4)
# # list_4.append(8)
# # print(list_4)
# # list_4.append(85)
# # print(list_4)

# list_5 = []
# print(list_5)
# for i in range(5):
#     list_5.append(i)
#     print(list_5)

# list_6 = [12, 7, -1, 21, 0]
# a = list_6.pop()
# print(a) # 0
# print(list_6) # [12, 7, -1, 21]
# print(list_6.pop()) # 21
# print(list_6) # [12, 7, -1]
# print(list_6.pop()) # -1
# print(list_6) # [12, 7]
# print(list_6.pop(0)) # 12
# print(list_6) # [7]
# list_6.insert(1, 121)
# print(list_6) # [7, 121]
# list_6.insert(1, -5)
# print(list_6) # [7, -5, 121]

list_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_7[0])                 # 1
print(list_7[1])                 # 2
print(list_7[len(list_7) - 1])   # 10
print(list_7[-5])                # 6
print(list_7[:])                 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_7[:2])                # [1, 2]
print(list_7[len(list_7) - 2:])  # [9, 10]
print(list_7[2:9])               # [3, 4, 5, 6, 7, 8, 9]
print(list_7[6:-18])             # []
print(list_7[0:len(list_7):6])   # [1, 7]
print(list_7[::6])               # [1, 7]