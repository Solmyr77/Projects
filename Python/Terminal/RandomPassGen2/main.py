import dict as d
import random
import time
import os

def clear():
    os.system('CLS')

def Pass_gen():

    length = int(input('Adja meg a jelszó hosszát: '))

    random.shuffle(d.lowercase_letter_list)
    random.shuffle(d.uppercase_letter_list)
    random.shuffle(d.symbol_list)
    random.shuffle(d.digit_list)
    random.shuffle(d.letter_list)


    generator_list = d.lowercase_letter_list + d.symbol_list + d.uppercase_letter_list + d.digit_list + d.letter_list
    random.shuffle(generator_list)


    generated_list = []

    for i in range (length):

        generated_list.append(random.choice(generator_list))


    random.shuffle(generated_list)

    print ('A generált jelszó: ')
    print ("".join(generated_list))


if __name__ == "__main__":
    Pass_gen()
    time.sleep(10)
    clear()