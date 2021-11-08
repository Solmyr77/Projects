import allat

állatfajok = []

for _ in range(3):
    fajnév = input('Adja meg az állat nevét: ')
    tömeg = input('Adja meg az állat tömegét: ')
    állatfaj = allat.Állatfaj(fajnév,tömeg)
    állatfajok.append(állatfaj)

legnehezebb_allat = állatfajok[0]

for állatfaj in állatfajok:
    print('A(z) ' + állatfaj.fajnév + ' tömege ' + állatfaj.tömeg + ' kg ')
    if állatfaj.tömeg > legnehezebb_allat.tömeg:
        legnehezebb_allat = állatfaj

output = open('output.txt', 'w')
print('A(z)', legnehezebb_allat.fajnév, 'a legnehezebb.', file=output)
output.close()