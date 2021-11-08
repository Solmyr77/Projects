from math import sqrt

formula = input("Adja meg a kiszámolandó oldalt: ")

if formula == 'c':

    formc()
    sidea = int(input("Adja meg az A oldal hosszát: "))
    sideb = int(input("Adja meg a B oldal hosszát: "))

    answercs = sidea * sidea + sideb * sideb

    answerc = sqrt(answercs)

    roundedc = round (answerc, 3)
    print ('A C oldal hossza: ')
    print (roundedc)

elif formula == 'b':

    sidea = int(input("Adja meg az A oldal hosszát: "))
    sidec = int(input("Adja meg a C oldal hosszát: "))

    answerbs = sidea * sidea + sidec * sidec
        
    answerb = sqrt(answerbs)

    roundedb = round (answerb, 3)
    print ('A B oldal hossza: ')
    print (roundedb)

elif formula == 'a':

    sideb = int(input("Adja meg a B oldal hosszát: "))
    sidec = int(input("Adja meg a C oldal hosszát: "))

    answeras = sideb * sideb + sidec * sidec

    answera = sqrt(answeras)

    roundeda = round (answera, 3)
    print ('Az A oldal hossza: ')
    print (roundeda)

else : 

    print ("Kérem adja meg az A, B vagy a C oldalt!")