import faces as dice
import time
import random


def roll():

    index_rolls = random.randint(0,5)

    for _ in range(index_rolls):

        time.sleep(1)
        index_dice = random.randint(0, 5)
        index_rolls-=1
        header = (f'\n--------{index_rolls}--------\n')
        rolled_value = dice.faces[index_dice]
        print (f'{header}\n{rolled_value}\n{header}\n')


if __name__ == "__main__":
    roll()