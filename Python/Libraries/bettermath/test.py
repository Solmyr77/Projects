import bettermath
import math
import timeit

def def_fact():
    fact = math.factorial(999999)
    runtime = timeit.timeit()
    print(f'Math: {runtime}')

def fact():
    fact = bettermath.fact(999999)
    runtime = timeit.timeit()
    print(f'Bettermath: {runtime}')

fact()
def_fact()