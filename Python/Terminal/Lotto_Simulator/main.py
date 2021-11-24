import random


class Lotto:


    def __init__(self):
        self.won = 0
        self.tries = 0
        self.three = 0
        self.four = 0
        self.price = 300
        self.price_sum = 0


    @classmethod
    def match_lists(self, list1, list2):
        set_1 = set(list1)
        set_2 = set(list2)
        return len(set_1.intersection(set_2))
    

    def infinite_roll(self):
        while self.won == 0:
            lotto_numbers = []
            user_numbers = [1, 2, 3, 4, 5]
            
            for _ in range(5):
                lotto_numbers.append(random.randint(1, 90))

            if lotto_numbers == user_numbers:
                print('\nÖn nyert!\n\nNyereménye: 2,272 milliárd Ft\n')
                print(f'Sikerült {self.tries} próbálkozásból.')
                print(f'Hármas: {self.three}\nNégyes: {self.four}\n')
                print(f'{self.price_sum} Forintba került.')
                self.won = 1
            else:
                self.tries += 1
                self.won = 0
                self.price_sum += self.price
                
            if Lotto.match_lists(user_numbers, lotto_numbers) == 3:
                self.three += 1
            elif Lotto.match_lists(user_numbers, lotto_numbers) == 4:
                self.four += 1


if __name__ == '__main__':
    l = Lotto()
    l.infinite_roll()
