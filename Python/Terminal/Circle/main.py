import data as d
import math


class Circle:

    while True:


        unit = str(input('Mm vagy Cm: '))


        if unit.lower() == 'mm':

            diameter = float(input('Adja meg a kör átmérőjét: '))
            d.out["Átmérő"].append(diameter)

            radius = diameter/2
            d.out["Sugár"].append(radius)

            circumference = 2 * math.pi * radius
            d.out["Kerület"].append(circumference)

            area = math.pi * radius * radius
            d.out["Terület"].append(area)

            for key, value in d.out.items():
                print(key, ' : ', (str(value)[1:-1]), 'mm')
            break


        elif unit.lower() == 'cm':
            
            diameter = float(input('Adja meg a kör átmérőjét: '))
            d.out["Átmérő"].append(diameter)

            radius = diameter/2
            d.out["Sugár"].append(radius)

            circumference = 2 * math.pi * radius
            d.out["Kerület"].append(circumference)

            area = math.pi * radius * radius
            d.out["Terület"].append(area)

            for key, value in d.out.items():
                print(key, ' : ', (str(value)[1:-1]), 'cm')
            break


        else:
            print('A kettő közül válasszon!')
