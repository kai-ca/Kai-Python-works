""" For a given list (or other iterable) we do a frequency count and returns a dict.

    Copyright (c)2015 Ulf Wostner <wostner@cyberprof.com>. All rights reserved.
    
    >>> d = freqdict(['a', 'b', 'a', 'a', 'd'])
    >>> d['a'] = 3
    >>> 'e' in d
    False

    >>> items = [(1, 3), (5, 5), (5, 5), (6, 6), (5, 5), (6, 1)]
    >>> f = freqdict(items)
    >>> f[(5, 5)]
    3
    >>> (4, 4) in f
    False

"""

from dice import rolls, rollpairs


def freqdict(items):
    """ Based on items, returns a dictionary with the frequency for each item.

    >>> items = [5, 2, 1, 1, 2, 6, 2, 2, 5, 1]
    >>> d = freqdict(items)
    >>> type(d)
    <class 'dict'>
    >>> d == {1: 3, 2: 4, 5: 2, 6: 1}
    True
    """

    itemsDict = {item: items.count(item) for item in items}
    return itemsDict



TEMPLATE = "{:>6s} {:>6s}"
TEMPLATE2 = "{:>6d} {:>6d}"

def print_freqtable(items, keys=None, label='item'):
    """Prints a frequency table for the items. If keys are provided, those are used in the table.

    >>> items = [1, 3, 4, 4, 4, 4, 4, 6, 6, 3, 4, 3, 4, 4, 1, 3, 4, 6, 4, 3]
    >>> print_freqtable(items)
      item   freq
         1      2
         3      5
         4     10
         6      3

    We can provide a set of keys so that missing values show up with frequency zero.

    >>> keys = [1, 2, 3, 4, 5, 6]
    >>> print_freqtable(items, keys=[1, 2, 3, 4 ,5 ,6])
      item   freq
         1      2
         2      0
         3      5
         4     10
         5      0
         6      3

     >>> items = [(6, 6), (6, 5), (5, 6), (5, 5), (6, 5), (6,6)]
     >>> print_freqtable(items, label='pair')
      pair   freq
       (5, 5)      1
       (5, 6)      1
       (6, 5)      2
       (6, 6)      2
    """

    itemDict = freqdict(items)  
    print(TEMPLATE.format(label, 'freq'))
    if keys:
        for key in keys:
            if key not in itemDict:
                itemDict[key] = 0
    for item in itemDict:
        print(TEMPLATE2.format(item, itemDict[item]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

