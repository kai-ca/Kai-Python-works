"""We generate a list of triples for hailstone 
seeds, showing seed, length, height.

Usage: import triples
Usage: from triples import triples

>>> triples(1, 6)
[(1, 1, 1), (2, 2, 2), (3, 8, 16), (4, 3, 4), (5, 6, 
16), (6, 9, 16)]

"""
import height
import length
from height import measure
from length import measure


def triples(minseed, maxseed):
    """Returns a list of triples(seed, length, height) for all seeds from minseed to maxseed.

    """

    return [(seed, length.measure(seed), 
height.measure(seed)) for seed in range(minseed, maxseed+1)]

