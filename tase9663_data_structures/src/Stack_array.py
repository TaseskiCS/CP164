"""
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-01-15"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy
from pickle import TRUE


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the stack is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self._values) == 0
        
        
        
        
    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        
        self._values.append(deepcopy(value))
        
       

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"

        return int(self._values.pop())

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"
        
        return deepcopy(self._values[-1])
    
    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._values[::-1]
        return
    
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        shortest_stack = None
        other_stack = None
        if len(source1._values) > len(source2._values):
            shortest_stack = source2
            other_stack= source1
        else:
            shortest_stack = source1
            other_stack = source2
            
        while len(shortest_stack._values) > 0:
            val1 = shortest_stack._values[-1]
            val2 = other_stack._values[-1]
            self._values.append(deepcopy(val1))
            self._values.append(deepcopy(val2))
            del shortest_stack._values[-1]
            del other_stack._values[-1]
            
        for element in other_stack._values:
            self._values.append(deepcopy(element))
            del other_stack._values[-1]
        return


    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value