"""We implement a Queue data structure.

Queue is a FIFO = First In First Out data structure, like people in line at a ticket office.

We create a class named Queue.

Then we can make instances of that class.

>>> myqueue = Queue()

>>> isinstance(myqueue, Queue)
True

>>> myqueue.push('Alice')
>>> myqueue.push('Eve')

Who is first in line?

>>> myqueue.peek()
'Alice'

Remove them in order (remember FIFO).

>>> myqueue.pop()
'Alice'
>>> myqueue.pop()
'Eve'
"""


class Queue:
    """Queue data structure.
       
    """

    def __init__(self):

        self.data = []
    
    def push(self, item):
        "Push item onto the Queue"

        self.data.append(item)

    def pop(self):
        """Remove the "top item" (the biggest item) from the Queue. """

        return self.data.pop(0)


    def is_empty(self):
        """Returns True if the Queue is empty."""

        return self.data == []

    def peek(self):
        """Return the item at "the front"  of the Queue. Do not remove that item."""

        return self.data[0]

    def __str__(self):

        return "<Queue: {} items>".format(len(self.data))

   
if __name__ == '__main__':
    import doctest
    doctest.testmod()


