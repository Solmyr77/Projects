from operator import le, ge

def bsort(lista, direction):
    
    """[Sorts a list in ascending or descending order, defaults to ascending
        if incorrect value is given]

    Args:
        lista ([list of integers or floats]): [list to sort]

        order ([int 0 or 1]): [Ascending or descending order,
         0 for ascending 1, for descending]
    """

    if direction == 1:
        sign = le
    else:
        sign = ge

    done = True
    while done:
        done = False
        for i in range(len(lista)-1):
            if sign(lista[i], lista[i + 1]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                done = True