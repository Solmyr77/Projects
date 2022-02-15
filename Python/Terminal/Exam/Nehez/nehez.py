import allat

állatfajok_lista = []

for _ in range(3):
    fajnév = input('Adja meg az állat nevét: ')
    tömeg = input('Adja meg az állat tömegét: ')
    állatfaj_class = allat.Állatfaj(fajnév,tömeg)
    állatfajok_lista.append(állatfaj_class)

legnehezebb_allat = állatfajok_lista[0]

for állatfaj_class in állatfajok_lista:
    print('A(z) ' + állatfaj_class.fajnév + ' tömege ' + állatfaj_class.tömeg + ' kg ')
    if állatfaj_class.tömeg > legnehezebb_allat.tömeg:
        legnehezebb_allat = állatfaj_class

output = open('output.txt', 'w')
print('A(z)', legnehezebb_allat.fajnév, 'a legnehezebb.', file=output)
output.close()