while True:

    list_hetfo = ['Töri', 'IKT', 'Matek', 'Magyar', 'Infotáv', 'Infotáv', 'Tesi', 'Tesi']
    list_kedd = ['Angol', 'IKT', 'IKT', 'Magyar', 'Fizika', 'Matek']
    list_szerda = ['Progalap', 'Progalap', 'Ofő', 'Magyar', 'Matek', 'Pénzügy', 'Angol']
    list_csut = ['Infotáv', 'Infotáv', 'Fizika', 'Töri', 'Tesi', 'Angol', 'Magyar', 'Digitkult']
    list_pentek = ['Matek', 'Töri', 'Angol', 'Magyar', 'Tesi']

    var_hetfo = ['Hétfő', 'Hetfo', 'hétfő', 'hetfo']
    var_kedd = ['Kedd', 'kedd']
    var_szerda = ['Szerda', 'szerda']
    var_csut = ['Csütörtök', 'Csutortok', 'csütörtök', 'csutortok']
    var_pentek = ['Péntek', 'Pentek', 'péntek', 'pentek']

    orarend = ['ORAREND', 'ÓRAREND']
    kereses = ['KERESÉS', 'KERESES']

    tipus = str(input('Órarend vagy keresés?: '))

    tipusU = tipus.upper()

    if tipusU in kereses:

        ora = str(input('Melyik óra?: '))

        oraU = ora.upper()

        if oraU == 'TÖRI':

            print ('Hétfő, Csütörtök')
            break

        if oraU == 'IKT':

            print ('Hétfő, Kedd')
            break

        if oraU == 'MATEK':

            print ('Hétfő', 'Kedd', 'Szerda', 'Péntek')
            break

        if oraU == 'MAGYAR':

            print ('Minden nap')
            break

        if oraU == 'INFOTÁV':

            print ('Hétfő, Csütörtök')
            break

        if oraU == 'TESI':

            print ('Hétfő, Csütörtök, Péntek')
            break

        if oraU == 'ANGOL':

            print ('Kedd, Szerda, Csütörtök, Péntek')
            break

        if oraU == 'FIZIKA':

            print ('Kedd, Csütörtök')
            break

        if oraU == 'PROGALAP':

            print ('Szerda')
            break

        if oraU == 'PÉNZÜGY':

            print ('Szerda')
            break

        if oraU == 'DIGITKULT':

            print ('Csütörtök')
            break

    elif tipusU in orarend:

        nap = str(input('Add meg a napot: '))

        if nap in var_hetfo:

            print (list_hetfo)
            print (str('Órák száma: ') + str(len(list_hetfo)))
            break


        elif nap in var_kedd:

            print (list_kedd)
            print (str('Órák száma: ') + str(len(list_kedd)))
            break


        elif nap in var_szerda:

            print (list_szerda)
            print (str('Órák száma: ') + str(len(list_szerda)))
            break


        elif nap in var_csut:

            print (list_csut)
            print (str('Órák száma: ') + str(len(list_csut)))
            break


        elif nap in var_pentek:

            print (list_pentek)
            print (str('Órák száma: ') + str(len(list_pentek)))
            break


        else:

            print('Helytelen nap, próbáld újra!')

    else: 

        print ('Kérlek a két lehetőség közül válassz!')