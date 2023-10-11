# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
def pow_rec(a, b):
    if b == 0:
        return 1
    return pow_rec(a, b - 1) * a


print(pow_rec(abs(int(input('Enter base number: '))), abs(int(input('Enter a power: ')))))

# pow_rec(5, 3) -> pow_rec(5, 2) * 5 = 1 * 5 * 5 * 5 = 125
#                       |
#                  pow_rec(5, 1) * 5 = 1 * 5 * 5
#                       |
#                  pow_rec(5, 0) * 5 = 1 * 5
#                       |
#                       1
