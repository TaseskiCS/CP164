"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports

# Constants

from Priority_Queue_array import Priority_Queue

source = Priority_Queue()

source.insert(3)

source.insert(1)

source.insert(2)

source.insert(1)

source.insert(4)

target1, target2 = source.split_key(3)


print("Printing Target 1...")
while len(target1) > 0:
    print(target1.remove())

print("Printing Target 2...")
while len(target2) > 0:
    print(target2.remove())