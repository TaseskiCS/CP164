"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports

# Constants

from List_array import List
from utilities import array_to_list, list_to_array

llist = List()
array = [1, 2, 3, 4, 5]
print(f'List: {array}')
array_to_list(llist, array)

print(f'List object: {llist._values}')

target = []
list_to_array(llist, target)
print(f'Target: {target}')