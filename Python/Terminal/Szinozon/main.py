manual = """
A játék lényege, hogy a gép által elrejtett 4 golyó színét 
és ezek sorrendjét kitaláljuk. 

Minden egyes tippünk után a gép fekete és/vagy fehér "tüskékkel" válaszol. 

A fehér tüske jelentése: egy golyó színét eltaláltuk (de a helyét nem), 
a fekete tüske jelentése: egy golyó színét és helyét is eltaláltuk. 

Azt, hogy melyik golyóra vonatkoznak az egyes tüskék, 
azt nem árulja el a gép, ezt nekünk kell kitalálnunk 
az egyes tippekre adott válaszokból.

A játék során a következő színeket lehet bemondani 
(Figyelem, pontosan ezeket a szavakat kell használni!): 
"piros", "fehér", "kék", "rózsaszín", "narancs", "lila", "sárga", "zöld".

Ha egy sorban mind a négy színt bemondtuk, akkor a "rendben" szóval lehet 
a tippet értékeltetni a géppel.

Az utoljára bemondott tippet a "mégsem" szóval lehet érvényteleníteni.

A "súgó" vagy a "segítség" parancsokat bármikor kiadva 
egy új ablakban megjelenik a játék leírása, 
valamint a használati útmutató. 

A parancsok ismételt kiadásával az ablak bezáródik.

A "szabad a gazda" parancsot bármikor kiadva 
a helyes megfejtés megjelenik a kérdőjelek helyén.

Az "új játék" paranccsal bármikor elölről kezdhetjük a játékot.

A "kilépés" hatására befejezhetjük a játékot.

Ez utóbbi három parancsot a gép kérdésére meg kell erősíteni 
az "igen" vagy a "nem" szóval.
"""


import random
import platform
import os


class Szinozon:
    def __init__(self):
        self.palette = ["piros", "fehér", "kék", "rózsaszín", "narancs", "lila", "sárga", "zöld"]
        self.generated_palette = [random.choice(self.palette) for _ in range(4)]
        self.tries = 1
        self.user_palette = None


    def clear_screen(self):
        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        elif system in ['Darwin', 'Linux']:
            os.system('clear')

    
    def reset(self):
        self.clear_screen()
        self.__init__()
        self.build()
    
    
    def pretty_input_str(self, input_name):
        while 1:
            try:
                var_to_return = str(input(f'{input_name}'))
                break
            except Exception:
                print('Hibás adat!')
        return var_to_return


    def take_input(self, manual_flag = 0, count_flag = 0):
        if self.tries == 11:
            print('Vesztettél!')
            exit()
        print(f'{self.tries}. Próbálkozás, még van {11-self.tries} próbálkozásod.')


        self.user_palette = []


        while count_flag < 4:
            if self.user_palette == None:
                print('Még nem adtál meg színt!')
            else:
                print(f'Eddig megadott színek: {", ".join(self.user_palette)}')
            command = (self.pretty_input_str('Parancs: '))


            if command.lower() in ['súgó', 'segítség']:

                self.clear_screen()

                if manual_flag == 0:
                    print(manual)
                    manual_flag += 1
                elif manual_flag == 1:
                    manual_flag = 0


            elif command.lower() == 'szabad a gazda':
                confirm = self.pretty_input_str('Biztos?: ')
                if confirm.lower() == 'igen':
                    print(f'Ezt kellet volna kitalálnod: {", ".join(self.generated_palette)}')
                else:
                    continue
            
            
            elif command.lower() == 'új játék':
                confirm = self.pretty_input_str('Biztos?: ')
                if confirm.lower() == 'igen':
                    self.reset()
                else:
                    continue
            
            
            elif command.lower() == 'kilépés':
                confirm = self.pretty_input_str('Biztos?: ')
                if confirm.lower() == 'igen':
                    exit()
                else:
                    continue


            elif command.lower() == 'mégsem':
                try:
                    del self.user_palette[-1]
                except IndexError:
                    print('A listád üres!')
                if count_flag > 0:
                    count_flag -= 1
                continue


            elif command.lower() not in self.palette:
                print('Tessék?')


            else:
                self.user_palette.append(command.capitalize())
                count_flag += 1


        print(f'A megadott színek: {", ".join(self.user_palette)}')
        self.check_input()


    def check_input(self, correct_pos_color = 0, correct_color = 0):
        self.tries += 1
        
        for i in range(4):
            if self.user_palette[i].lower() in self.generated_palette:
                correct_color += 1
                if self.user_palette[i].lower() == self.generated_palette[i]:
                    correct_pos_color += 1

        result = f'{"*"*correct_pos_color}{"-"*(correct_color-correct_pos_color)}'
        print('\nHelyes pozícó és szín: *\nHelyes szín: -\n')
        print(f'|======|\n|{result.center(6)}|\n|======|\n')

        
        if correct_pos_color == 4:
            print('Vége a játéknak!')
            exit()
        else:
            self.take_input()
            
    
    def build(self):
        self.clear_screen()
        self.take_input()


Szinozon().build()
