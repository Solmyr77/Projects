import faces as dice
import time
import random
import time
import os


def clear():
    os.system('CLS')


def roll():


    index_rolls = random.randint(2,5)
    sleep_for = 1


    for _ in range(index_rolls):

        time.sleep(sleep_for)
        index_dice = random.randint(0, 5)
        index_rolls-=1
        sleep_for -= 0.15
        clear()
        header = (f'\n--------{index_rolls}--------\n')
        rolled_value = dice.faces[index_dice]
        print (f'{header}\n{rolled_value}\n{header}\n')


if __name__ == "__main__":
    roll()