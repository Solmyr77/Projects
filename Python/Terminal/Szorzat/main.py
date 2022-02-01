print ('Szorzatkereső')

szam = float(input('Adja meg a szorzandó számot: '))
szorzo = int(input('Hanyadik szorzatig?: '))

def szorzatfind():
    
    for i in range (1, szorzo):

        out = i * szam

        print (out)

szorzatfind()