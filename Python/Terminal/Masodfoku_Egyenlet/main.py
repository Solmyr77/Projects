import math

#(-b+sqrt(b*b-4*a*c))/2

def egyenlet():
    a = int(input('Adja meg az A-t: '))
    b = int(input('Adja meg a B-t: '))
    c = int(input('Adja meg a C-t: '))

    sq_root = math.sqrt((b*b) - (4 * a * c))

    answer_plus = ((-b) + sq_root)/2

    answer_minus = ((-b) - sq_root)/2

    print('X1: ' + str(answer_plus))
    print('X2: ' + str(answer_minus))

if __name__ == "__main__":
    egyenlet()