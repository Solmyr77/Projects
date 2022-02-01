termek = float(input('Adja meg a termék árát: '))
afa = float(input('Adja meg az ÁFÁ-t: '))

afacalc = round((termek*(1+afa/100)), 3)

print ('A teljes ár: ' + str(afacalc))