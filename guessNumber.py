import random


def guess(x):
    random_number = random.randint(1, x)
    g = 0
    while g != random_number:
        g = int(input(f'Guess a number between 1 and {x}: '))
        if g < random_number:
            print('Too low')
        elif g > random_number:
            print('Too high')
    print(f'yay, correct, the number is {random_number}')


guess(12)
