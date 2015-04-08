""" Dice rolls. We roll dice. One die or a 
pair of dice. The dice usually have six 
sides
    numbered 1 thru 6, but we also allow 
dice with any nsides. See the test files 
for details.

    Copyright (c)2015 Ulf Wostner 
<wostner@cyberprof.com>. All rights 
reserved. """

import random

def roll(nsides=6):
    """Roll a die with nsides. Returns an 
int from 1 to nsides."""

    return random.randint(1, nsides)



def rollpair(nsides=6):
    """Roll a pair of nsided dice. Returns 
rolls as tuples, like (3, 6)."""

    return (roll(nsides), roll(nsides))



def rolls(ntimes=10, nsides=6):
    """Roll an nsided die ntimes. Returns a list.

    >>> import random; random.seed('downtown')
    >>> rolls()
    [2, 5, 4, 5, 4, 1, 6, 6, 2, 2]
    """

    rollList = []
    for i in range(ntimes):
        rollList.append(roll(nsides))
    return rollList

def rollpairs(ntimes=10, nsides=6):
    """Roll a pair of nsided die ntimes. 
Returns a list.

    >>> import random; random.seed('pythonistas')
    >>> rollpairs()
    [(2, 6), (6, 2), (6, 4), (5, 5), (6, 
3), (2, 4), (1, 3), (3, 4), (5, 6), (4, 
5)]
    """

    pairList = []
    for i in range(ntimes):
        pairList.append(rollpair(nsides))
    return pairList


def dice_sum(pair):
    """"Returns the sum of the values on 
the dice pair.

    >>> pair = (6, 1)
    >>> dice_sum(pair)
    7
    """

    return sum(pair)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

