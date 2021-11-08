import bettersort
bsort = bettersort.bsort


lista = [1, 7, 3, 9]


bsort(lista, 0)
print(f'Ascending: {lista}')


bsort(lista, 1)
print(f'Descending: {lista}')
