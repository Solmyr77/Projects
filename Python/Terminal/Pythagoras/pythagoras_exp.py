from math import sqrt


class Pythagoras:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 0

    def main(self):
        self.c = round(sqrt(self.a**2 + self.b**2), 5)
        return self.c


triangle_1 = Pythagoras(1, 6).main()
triangle_2 = Pythagoras(7, 10).main()
triangle_3 = Pythagoras(8, 23).main()


print(triangle_1, triangle_2, triangle_3)
