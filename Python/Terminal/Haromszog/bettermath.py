import math

def iseven(num):
    
    """
        Checks if a number is even or odd,
        returns True if even, False if odd.

        Args:
            num (int, float): The input number
    """

    if num%2:
        return False
    else:
        return True

def fact(num):

    """
        Finds factorial, returns factorial

        Args:
            num (int, float): The input number
    """

    fact = 1
    for i in range (1, num + 1):
        fact = fact*i
    return fact
