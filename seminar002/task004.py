n = int(input('Enter a day count: '))
count = 0
max_count = 0
for i in range(n):
    temp = int(input('Enter the temperature: '))
    if temp >= 0:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0
print(max_count)
