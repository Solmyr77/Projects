import operator

ops = {
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv
}


def Calculator():

    a = float(input('Adja meg az első számot: '))

    muvelet = input('Adja meg a műveleti jelet: ')

    muvelet_func = ops[muvelet]

    b = float(input('Adja meg a második számot: '))

    eredmeny = muvelet_func(a,b)

    eredmeny_rounded = round(eredmeny, 3)

    print ('Az eredmény: ' + str(eredmeny_rounded))


Calculator()
