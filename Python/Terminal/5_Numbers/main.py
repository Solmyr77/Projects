import bettermath
import os

#Lőrincz Loránd 3-4. feladat

eo = bettermath.iseven

numbers = []
even = []
odd = []


def clear():
    os.system('CLS')


def main():

    clear()

    for i in range(5):
        while True:

            loopback = True
            while loopback:
                try:
                    user_input = float(input('Adjon meg egy számot 1 és 99 között: '))
                    loopback = False
                except:
                    print('Számot adjon meg!')
                    loopback = True

            if 1 <= user_input <= 99:
                numbers.append(user_input)
                if eo(user_input):
                    even.append(user_input)
                else:
                    odd.append(user_input)
                break

            else:
                print('Helytelen szám!')

def odd_print():
    if odd:
        print(f'Páratlan számok: {str(odd)[1:-1]}')
    else:
        print('Nincsenek páratlan számok')
def even_print():
    if even:
        print(f'Páros számok: {str(even)[1:-1]}')
    else:
        print('Nincsenek páros számok')

def output():
    print(f'Számok: {str(numbers)[1:-1]}')
    odd_print()
    even_print()


if __name__ == '__main__':
    main()
    output()