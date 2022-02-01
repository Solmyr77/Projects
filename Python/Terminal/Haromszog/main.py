import threading
import time
import bettermath
eo = bettermath.iseven


def first():
    for i in range(15):
        print(i*'0')
            
def second():
    for i in reversed(range(14)):
        print(i*'0')

if __name__ == "__main__":
    first()
    second()