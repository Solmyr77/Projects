import math


m = math.factorial
a = float(input('A: '))
b = float(input('B: '))


def egyenlet():

    #ab5 = (a+b)^5

    ab5 = (a+b)**5
    print(f'Rövid egyenlet: {ab5}')


def egyenlet_long():

    #ab5 = (a+b)^5

    ab5 = a**5+b**5+(m(5)/m(4))*a**4*b+(m(5)/m(4))*a*b**4+(m(5)/m(3)/m(2))*a**3*b**2+(m(5)/m(3)/m(2))*a**2*b**3
    print(f'Hosszú egyenlet: {ab5}')


egyenlet()
egyenlet_long()