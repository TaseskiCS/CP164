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

from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test
# Constants

# First
source = [1, 3, 5, 9]
print(f'Source before: {source}')
pq = Priority_Queue()
array_to_pq(pq, source)
print('Contents of Priority Queue object...')
for i in pq:
    print(i)
print(f'Source after: {source}')
print('-' * 50)

# Second
target = []
print('Target before: ')
pq_to_array(pq, target)
print(f'Target after: {target}')
print(f'pq empty: {pq.is_empty()}')

# Third
a = [10, 20, 30, 40, 50]
priority_queue_test(a)
print('-' * 50)

