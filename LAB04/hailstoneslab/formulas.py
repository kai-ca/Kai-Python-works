"""Formulas used for calculating hailstone numbers.

Usage: from formulas import ulam

>>> ulam(5)
>>> 16
>>> ulam(7)
22
    
"""

def ulam(n):
    """Returns the next hailstone number after n.
    """
    if (n % 2 == 1):    # n odd
        return 3*n + 1
    else:               # n even
        return n//2


