import multiprocessing as mp
from functools import cache
import random
import ctypes
import time
import os


class Lottery:
    def __init__(self):
        self.clear()
        self.cores = os.cpu_count()
        self.win = self.pretty_input_int('Hány találatig?: ')
        self.user_numbers = [self.pretty_input_int(f'Add meg az {i+1}. számot: ') for i in range(5)]
        self.total = mp.Value(ctypes.c_int, 0)
        self.complete_flag = mp.Value(ctypes.c_int, 0)
        self.repeat = mp.Value(ctypes.c_int, 0)


    def clear(self):
        os.system('cls')


    def pretty_input_int(self, title):
        while 1:
            try:
                var_to_return = int(input(title))
                if 1 <= var_to_return <= 90:
                    break
                else:
                    print('1 és 90 között!')
            except Exception:
                print('Hibás adat!')
        return var_to_return
 

    def create_workers(self):
        core_dict = {f'core_{i}': mp.Process(target=self.worker_process) for i in range(self.cores)}
        for i in range(self.cores): core_dict[f'core_{i}'].start()


    @cache
    def worker_process(self, numbers = range(1, 90)):
        start = time.time()
        while self.complete_flag.value == 0:
            
            random_numbers = random.sample(numbers, k=5)
            
            counter = 0
            for data in random_numbers:
                if data in self.user_numbers:
                    counter += 1
                    self.total.value += 1

            if counter == self.win:
                self.complete_flag.value += 1
                end = time.time()
                print('\nNyertél!')
                print(f'A számaid: {", ".join(str(x) for x in self.user_numbers)}')
                print(f'A kihúzott számok: {", ".join(str(x) for x in random_numbers)}')
                print(f'{self.total.value} pörgetésből.')
                print(f'{self.total.value*300} Ft-ba került.')
                print(f'A program lefutott: {round(end-start, 3)} Mp alatt.\n')


    def build(self):
        self.create_workers()


if __name__ == '__main__':
    lt = Lottery()
    lt.build()
