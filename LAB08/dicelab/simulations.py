""" Simulations. Roll until a certain type of 
roll comes up.

    Copyright (c)2015 Ulf Wostner <wostner@cyberprof.com>. All rights reserved.
"""

from dice import roll, rollpair, dice_sum 
from predicates import is_double, is_double_six, is_seven_eleven 
from predicates import sum_is, sum_is_at_least, sum_is_at_most


def rolls_until(goal):
    """Rolls of a pair of dice until goal is met. Returns a list of the rolls.

    >>> import random; random.seed('EV')
    >>> rolls_until(is_double_six)
    [(1, 2), (1, 2), (2, 6), (5, 6), (4, 4), (6, 1), (6, 2), (5, 2), (3, 1), (6, 6)]
    """

    goalList = []
    goalList.append(rollpair())
    i = 0
    while goal(goalList[i]) is False:
        goalList.append(rollpair())
        i += 1
    return goalList


def how_many_rolls_until(goal):
    """Rolls a pair of dice until goal is met. Returns how many rolls it took.

    >>> import random; random.seed('EV')
    >>> how_many_rolls_until(is_double_six)
    10
    """

    return len(rolls_until(goal))



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
