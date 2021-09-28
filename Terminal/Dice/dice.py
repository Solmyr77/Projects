from random import randint

repeat = True

yos = ['igen','igne', 'ige']

while repeat:

    print ('Dobókocka:', randint(1,6))

    repeat = str(input('Újra? (Igen, Nem): ')).lower() in yos