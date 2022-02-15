import timeit

lower = int(input("Adja meg az alsó határt: "))
upper = int(input("Adja meg a felső határt: "))

def primes():

    for num in range(lower,upper+1):
        if num>1:
            for i in range(2, num):
                if (num%i)==0:
                    break
                
primes()

print (f'A program lefutott: {timeit.timeit()} másodperc alatt')