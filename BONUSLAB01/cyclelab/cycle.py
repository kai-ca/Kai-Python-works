""" Cycle data structure.

This assignment is challenging.

You need to do some research and figure out what methods are needed to get the behavior 
we want of Cycle objects.


GAMEPLAN:

    Read the tests in tests/testA.txt
    Write code in cycle.py until tests/testA.txt is OK.

    Read the tests in tests/testBtxt
    Write code in cycle.py until tests/testB.txt is OK.

    Read the tests in tests/testC.txt
    Write code in cycle.py until tests/testC.txt is OK.


>>> from data import SEASONS
>>> SEASONS
['Spring', 'Summer', 'Fall', 'Winter']

Create a cyclic data structure using your Cycle class.

>>> seasons = Cycle(SEASONS)

>>> isinstance(seasons, Cycle)
True

This attribute knows how many items are in the Cycle object.

>>> seasons.n
4

This is a pointer at the cyclic "wheel" of items.
It points to the "current" item. We started with Spring.

>>> seasons.item()
'Spring'

>>> seasons.pointer
0

>>> seasons.rotate()

>>> seasons.pointer
1
>>> seasons.item()
'Summer'


"""

class Cycle:
    """Our user-defined class Cycle for creating 
    a Cyclic datastructure from a list of items like week days.

    >>> week = Cycle(['M','T', 'W', 'R', 'F', 'Sa', 'Su'])

    """

    def __init__(self, datalist):
        "Create a Cycle based on the datalist."

        self.data = datalist
        self.n = len(self.data)
        self.pointer = 0
        
    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return self.n


    def item(self):
        "return the current item"

        i = self.pointer % self.n
        return self.data[i]

    def rotate(self, num=1):
        "update the index to the next item"

        self.pointer += num


if __name__ == '__main__':
    import doctest
    doctest.testmod()

        
