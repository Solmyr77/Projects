import timeit
from typing_extensions import runtime

def sort(lista):
    done = True
    while done:
        done = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                done = True
    runtime = timeit.timeit()
    print(f'Sort: {runtime}')

lista = [6, 3, 9, 15, 7, 1, 4]

sort(lista)

def def_sort(lista):
    lista.sort()
    runtime = timeit.timeit()
    print(f'Def_Sort: {runtime}')

def_sort(lista)