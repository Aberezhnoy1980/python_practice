n = int(input('Enter a day mileage: '))
m = int(input('Enter a route mileage: '))
dayCount = (m + n - 1) // n
dayCountThroughNegativeDiv = m // -n
print(f'A car will cover a route {m} rm long in {dayCount} days')
print(f'A car will cover a route {m} rm long in {-dayCountThroughNegativeDiv} days')

#  Отрицательное деление
#  -7 // 2 = (-4) * 2 + 1
#  -12 // 5 = (-3) * 5 + 3