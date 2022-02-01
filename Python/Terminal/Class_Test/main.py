class Enemy:
    def __init__(self, health, level, enemy_name):
        self.health = health
        self.level = level
        self.enemy_name = enemy_name

    def name(self):
        print('Név: ' + str(self.enemy_name))
        print('Szint: ' + str(self.level))
        print('HP: ' + str(self.health))

Nev = str(input('Adja meg az ellenség nevét: '))
Szint = int(input('Adja meg az ellenség szintjét: '))
Hp = int(input('Adja meg az ellenség HP-ját: '))

enemy = Enemy(Hp, Szint, Nev)
enemy.name()
