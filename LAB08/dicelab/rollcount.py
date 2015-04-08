""" Given a list of rolls of a pair of dice, we count how many rolls are of some kind,
    like is_double.

    Copyright (c) 2015 Ulf Wostner <wostner@cyberprof.com>. All rights reserved.
"""


def how_many(rolls, predicate):
    """For a given list of rolls, counts how many rolls satisfy the given predicate.

    >>> from predicates import is_double, is_seven_eleven
    >>> rolls = [(2, 6), (5, 3), (4, 5), (1, 2), (4, 1), (2, 3), (1, 6), (6, 1), (1, 4), (5, 4)]
    >>> len(rolls)
    10
    >>> how_many(rolls, is_double)
    0
    >>> how_many(rolls, is_seven_eleven)
    2
    """

    count = 0
    for pair in rolls:
        if predicate(pair):
            count += 1
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()

