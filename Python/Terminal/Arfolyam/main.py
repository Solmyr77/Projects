def custom():
    afa = int(input('Adja meg az ÁFA-t: '))
    termek = float(input('Adja meg a termék árát: '))

    ar = round(float(termek*(1+afa/100)), 3)

    print (ar)


def default():
    nemet = 19
    brit = 20
    cseh = 21
    lengyel = 23
    magyar = 27

    price = float(input('Mennyi egy valami? '))

    nemetprice = round(float(price*(1+nemet/100)), 3)
    britprice = round(float(price*(1+brit/100)), 3)
    csehprice = round(float(price*(1+cseh/100)), 3)
    lengyelprice = round(float(price*(1+lengyel/100)), 3)
    magyarprice = round(float(price*(1+magyar/100)), 3)

    nemetlist = str(nemetprice) + str(' pénz Németországban')
    britlist = str(britprice) + str(' pénz Nagy Britanniában')
    csehlist = str(csehprice) + str(' pénz Csehországban')
    lengyellist = str(lengyelprice) + str(' pénz Lengyelországban')
    magyarlist = str(magyarprice) + str(' pénz Magyarországon')

    pricelist = [nemetlist, britlist, csehlist, lengyellist, magyarlist]

    pricelist.sort()

    print ('Az árak növekvő sorrendben: ')
    print(*pricelist, sep="\n")

while True:

    valto = str(input('Custom vagy megadott?: ')).lower()

    if valto == 'megadott':
        default()
        break

    if valto == 'custom':
        custom()
        break

    else:
        print('Kérem a két lehetőség közül válasszon!')