import math

def iseven(num):
    
    """
        Checks if a number is even or odd,
        returns True if even, False if odd.

        Args:
            num (int, float): The input number
            
        Returns:
            [bool]: True if even, false if odd
    """

    if num%2:
        return False
    else:
        return True

def fact(num):

    """
        Finds factorial, returns factorial

        Args:
            num (float): The input number
            
        Returns:
            [float]: Factorial
    """

    fact = 1
    for i in range (1, num + 1):
        fact = fact*i
    return fact

def pythagoras(a, b):
    
    """
        Pythagoras theorem

        Args:
            num (int, float): The input numbers
        
        Returns:
            [float]: Hypotenuse
    """
    
    c = float(math.sqrt(a**2 + b**2))
    return c
