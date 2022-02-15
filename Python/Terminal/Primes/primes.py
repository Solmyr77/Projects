import time

lower = int(input("Adja meg az alsó határt: "))
upper = int(input("Adja meg a felső határt: "))

start = time.time()

primelist = []

def main():

    for num in range(lower,upper+1):
        if num>1:
            for i in range(2, num):
                if (num%i)==0:
                    break
            else:
                print(num)
                primelist.append(str(num))
    
    end_time = (time.time() - start)

    print (f'{lower} és {upper} között {(len(primelist))} Prímszám van')
    print (f'A program lefutott {round(end_time, 3)} mp alatt')


if __name__ == '__main__':
    main()