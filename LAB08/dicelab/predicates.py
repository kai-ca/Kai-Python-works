""" Dice predicates like is_double, is_seven_eleven, etc. 
    Copyright (c)2015 Ulf Wostner <wostner@cyberprof.com>. All rights reserved.

    >>> is_double((3, 3))
    True

"""

from dice import dice_sum

def is_double(pair):
    """Returns True if the numbers on the pair of dice is the same."""

    return pair[0] == pair[1]


def is_double_six(pair):
    """Returns True if the roll is double six. """
    
    return pair == (6, 6)


def is_seven_eleven(pair):
    """Returns True if the roll adds up to seven or eleven.

    >>> is_seven_eleven((6, 5)) and is_seven_eleven((3, 4))
    True
    """

    return dice_sum(pair) == 7 or dice_sum(pair) == 11



def sum_is(pair, n):
    """Returns True if the pair of dice has sum n.

    >>> sum_is((4,5), 9), sum_is((3, 2), 9)
    (True, False)
    """

    return dice_sum(pair) == n



def sum_is_at_least(pair, n):
    """Returns True if the sum of the dice pair is at least n.

    >>> pair1, pair2  = (5, 3), (6, 3)
    >>> sum_is_at_least(pair1, 8) and sum_is_at_least(pair2, 8) 
    True
    """

    return dice_sum(pair) >= n


def sum_is_at_most(pair, n):
    """Returns True if the sum of the pair of dice is 
at most n. """

    return dice_sum(pair) <= n



if __name__ == '__main__':
    import doctest
    doctest.testmod()
