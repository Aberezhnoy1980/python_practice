# colors = ['red', 'green', 'blue', 'grey']
# data = open('file.txt', 'a', encoding='utf-8')
# data.writelines(colors)
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
