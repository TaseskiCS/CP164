"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_combine
from Stack_array import Stack
# Constants

source1 = Stack()
source2 = Stack()

# Populate source1 and source2 stacks
for value in [5, 8, 12, 8]:
    source1.push(value)

for value in [3, 6, 1, 7, 9, 14]:
    source2.push(value)

# Call the stack_combine function
target = stack_combine(source1, source2)

# Display the contents of the target stack
while not target.is_empty():
    print(target.pop())

