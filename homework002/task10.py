# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


def find_flip_count():
    coin_count = int(input('Enter the number of coins: '))
    head = 0
    tail = 0
    for i in range(coin_count):
        coin = int(input('Enter heads (1) or tails (0) coin: '))
        if coin == 1:
            head += 1
        elif coin == 0:
            tail += 1
        else:
            print('Invalid input, please try again')
            return
    if head < tail:
        print(f'Flip {head} coins from head to tail')
    elif tail == 0 or head == 0:
        print('All coins on one side')
    elif head == tail:
        print('Equal amount of coins')
    else:
        print(f'Flip {tail} coins from tail to head')


find_flip_count()
