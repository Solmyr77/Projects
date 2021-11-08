def eta():
    
    distance = float(input('Add meg a távolságot: '))
    elapsed = float(input('Mennyi van meg?: '))
    time = float(input('Meddig tartott?: '))

    distance_remaining = distance-elapsed
    time_unit = elapsed/time
    eta = distance_remaining/time_unit

    rounded_eta = round(eta, 3)
    rounded_distance_remaining = round(distance_remaining, 3)
    minute = rounded_eta/60

    print (f'{rounded_distance_remaining} m van még hátra, {rounded_eta} mp/ {minute} perc múlva érsz oda.')

if __name__ == '__main__':
    eta()