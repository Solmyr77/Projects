from random import randint

print('Random generált szám kereső téma')

szaminput = int(input("Melyik számot szeretnéd megkeresni?: "))

def randomszam():
    probaszam = 0
    szam = 0

    while szam != szaminput:
        szam = randint(0, 999999)
        print(szam, end="\n")
        probaszam += 1

    return f"\nSikerült {probaszam} próbálkozás alatt."


if input("Mehet? [I/N]: ").lower() == "i":

    print(randomszam())

    while input("\nÚjra? [I/N]: ").lower() == 'i':
        print(randomszam())