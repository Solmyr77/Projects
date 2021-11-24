from math import sqrt 
import os

def clear():
    os.system('CLS')

def main():
    clear()
    a = float(input('Adja meg az A oldal hosszát mm-ben: '))
    b = float(input('Adja meg a B oldal hosszát mm-ben: '))
    c = round(sqrt(a**2 + b**2), 3)
    print(f'C oldal: {c} mm')
    
if __name__ == '__main__':
    main()