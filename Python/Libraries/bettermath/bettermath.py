import math
from functools import cache


def iseven(num):
    """
        Checks if a number is even or odd,
        returns True if even, False if odd.

        Args:
            num (int, float): The input number

        Returns:
            [bool]: True if even, false if odd
    """

    if num % 2:
        return False
    else:
        return True


def fact(num):
    """
        Finds factorial, returns factorial

        Args:
            num(int, float): The input number

        Returns:
            [float]: Factorial
    """

    fact_variable = 1
    for i in range(1, num + 1):
        fact_variable = fact_variable * i
    return fact_variable


def pythagoras(a, b):
    """
        Pythagoras theorem

        Args:
            a, b (int, float): The input numbers

        Returns:
            [float]: Hypotenuse
    """

    c = float(math.sqrt(a ** 2 + b ** 2))
    return c


@cache
def fib(num):
    """
    Fibonacci sequence

    Args:
        num (int, float): The input numbers

    Returns:
        [int]: The number at the location of [num]
        in the fibonacci sequence
    """

    if num <= 1:
        return num
    return fib(num - 1) + fib(num - 2)
