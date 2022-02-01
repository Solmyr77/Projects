import time
from functools import cache

lower = int(input("Adja meg az alsó határt: "))
upper = int(input("Adja meg a felső határt: "))

start = time.time()

primelist = []

@cache
def primes():

    for num in range(lower,upper+1):
        if num>1:
            for i in range(2, num):
                if (num%i)==0:
                    break
            else:
                print(num)
                primelist.append(str(num))
                
primes()

end = time.time()

end_time = (end - start)

end_rounded = round(end_time, 3)

print (str(lower) + str(' és ') + str(upper) + str(' között ') + str((len(primelist))) + str(' Prímszám van'))

print (str('A program lefutott ' + str(end_rounded) + str(' Másodperc alatt')))