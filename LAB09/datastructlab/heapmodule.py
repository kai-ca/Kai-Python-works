""" We implement a heap data structure by 
creating a class Heap and then make instances 
of Heap.
 
Not going for efficiency here just the basic 
behavior of a Heap.
 
Create an empty heap. 
 
>>> myheap = Heap()
 
>>> isinstance(myheap, Heap)
True
 
Then, push several objects onto the heap.
 
>>> for x in [50, 60, 20, 50, 30]:
...     myheap.push(x)
 
Time to remove some items.
 
>>> myheap.pop()
60
 
>>> myheap.is_empty()
False
 
What's at the top of the heap now?
 
>>> myheap.peek()
50
 
We can also create a heap directly from a given list.
 
>>> mydata = [80, 90, 70]
 
>>> smallheap = Heap(mydata)
>>> smallheap.pop()
90
>>> smallheap.peek()
80
 
The mydata list should not change. Let's check that.
 
>>> mydata
[80, 90, 70]
"""


class Heap:
    """Heap data structure created from a datalist.
    >>> myheap = Heap([40, 90, 60, 60, 70])
    >>> myheap.peek()
    90
    """

    def __init__(self, datalist=None):

        if not datalist:
            self.data = []
        else:
            self.data = sorted(datalist)

    def push(self, x):
        "Push x onto the heap."

        self.data.append(x)
        self.data.sort()

    def pop(self):
        """Remove and return the "top item" (the biggest item) from the heap. """

        return self.data.pop()

    def is_empty(self):
        """Returns True if the heap is empty."""

        return self.data == []

    def peek(self):
        """Show the "top item" (the biggest item) of the heap. Do not remove that item."""

        return self.data[-1]        

    def __str__(self):

        return self.data
        
   
if __name__ == '__main__':
    import doctest
    doctest.testmod()


