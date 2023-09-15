# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

first_number = abs(int(input('Enter a first secret integer: ')))
second_number = abs(int(input('Enter a second secret integer: ')))

s = first_number + second_number
p = first_number * second_number

#  second_number = p // first_number -> first_number = s - p // first_number -> first_number ** 2 - s * first_number + p = 0

y = int((s + (s ** 2 - 4 * p) ** (1 / 2)) // 2)
x = s - y

print(x, y)

#  alt
for i in range(1001):
    for j in range(1001):
        if i + j == s and i * j == p:
            print(i, j)
