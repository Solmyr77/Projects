import dict as d

marka = str(input("Adjon meg egy autómárkát: "))

pmarka = marka.lower()

if pmarka == "mercédesz":

    print ("Végsebesség: " + str(d.mercedes["topspeed"] + "\n" + "Származási ország: " + str(d.mercedes["country"])))

if pmarka == "lada":

    print ("Végsebesség: " + str(d.lada["topspeed"] + "\n" + "Származási ország: " + str(d.lada["country"])))

if pmarka == "chevrolet":

    print ("Végsebesség: " + str(d.chevrolet["topspeed"] + "\n" + "Származási ország: " + str(d.chevrolet["country"])))

if pmarka == "fiat":

    print ("Végsebesség: " + str(d.fiat["topspeed"] + "\n" + "Származási ország: " + str(d.fiat["country"])))