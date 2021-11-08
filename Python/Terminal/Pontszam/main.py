while True:

    pont = int(input('Adja meg a pontszámot: '))

    egy = range(0,49)
    ketto = range(50,59)
    harom = range(60,69)
    negy = range(70,79)
    ot = range(80-999)

    if pont in egy:
        print('A dolgozat 1-es')
        break

    elif pont in ketto:
        print('A dolgozat 2-es')
        break

    elif pont in harom:
        print('A dolgozat 3-mas')
        break

    elif pont in negy:
        print('A dolgozat 4-es')
        break

    elif pont in ot:
        print ('A dolgozat 5-ös')
        break

    else:
        print('Helytelen')