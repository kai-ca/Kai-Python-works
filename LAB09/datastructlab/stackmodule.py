"""We implement a Stack data structure.

Stack is a LIFO = Last In First Out data 
structure, like a atack of plates. The last 
plate you put on the stack is the first plate 
that will be removed.

Tip: Print out all the test files in the tests 
directory and then get to work on the metods, 
one by one.

Use your Stack class to create an instance 
named mystack.

>>> mystack = Stack()

>>> isinstance(mystack, Stack)
True

The Stack has a push method.  Push a bunch of 
numbers onto the stack.

>>> for item in [90, 30, 50, 60, 20, 50]:
...     mystack.push(item)

Remove an item from the stack using the pop 
method you definfed for Stack. Notice that 
it's LIFO !

>>> mystack.pop()
50
>>> mystack.pop()
20

>>> mystack.is_empty()
False

"""


class Stack:
    """Stack data structure.

    >>> mystack = Stack()
    
    """

    def __init__(self):
        """Creates an instance of Stack with no items in it."""

        self.data = []


    def push(self, item):
        "Push item onto the stack."

        self.data.append(item)


    def pop(self):
        """Remove the item we put in last ( remember it's LIFO). """

        return self.data.pop()

    def is_empty(self):
        """Returns True if the stack is empty."""

        return self.data == []

    def peek(self):
        """Returns the top item of the stack but does not remove that item. Just peeking."""

        return self.data[-1]


    def __str__(self):
        """Method for casting Stack objects as str object. Used by print."""

        return "<Stack: {} items>".format(len(self.data))

        
   
if __name__ == '__main__':
    import doctest
    doctest.testmod()


