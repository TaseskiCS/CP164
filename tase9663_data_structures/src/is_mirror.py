"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2024-01-16"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants
CHARS = 'abc'
MIRROR = 'm'
def is_mirror(string):
    """
    -------------------------------------------------------
    Determines if string is mirror string or not. 
    (uses a stack)
    Use: b = is_mirror(string)
    -------------------------------------------------------
    Parameters:
        string - string to test (string)
    Returns:
        mirror - True if string is mirror, False otherwise (bool)
    ------------------------------------------------------
    """
    mirror = True
    stack = Stack()
    n = len(string)
    i = 0
    
    while i < n and string[i] != MIRROR:
        stack.push(string[i])
        print(string[i])
        i +=1
    i+=1
    
    while mirror and i < n and not stack.is_empty():
        c = stack.pop()
    
        if string[i] != c:
            mirror = False
    
    if not (stack.is_empty() and i == n):
        mirror = False
        
    return mirror
        
        
        
string = 'abcmcba'
print(is_mirror(string))