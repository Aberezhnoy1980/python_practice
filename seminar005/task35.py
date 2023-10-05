# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i:
            return False
    return True


print(is_prime(abs(int(input('Enter any integer: ')))))
