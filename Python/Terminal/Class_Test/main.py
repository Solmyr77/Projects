class Diak:

    def __init__(self, nev, kor, osztaly):
        self.nev = nev
        self.kor = kor
        self.osztaly = osztaly

    def output(self):
        print(f'Név: {self.nev}')
        print(f'Kor: {self.kor}')
        print(f'Osztály: {self.osztaly}')

    def valami(self):
        self.kor = ('10')
        print(self.kor)

diak_1 = Diak('Lajos', '5', '7')
diak_2 = Diak('Feri', '5', '7')
diak_3 = Diak('Jani', '5', '7')

diak_1.output()
diak_3.output()
diak_3.valami()
diak_3.output()