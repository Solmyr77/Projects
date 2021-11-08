import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

a = float(input('Add meg az első számot: '))

muvelet = input('Add meg a műveleti jelet: ')

muvelet_func = ops[muvelet]

b = float(input('Add meg a második számot: '))

eredmeny = muvelet_func(a, b)

print (round(eredmeny, 3))