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

from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test
# Constants
print('Array to queue...')
queue = Queue()
source = [1, 2, 3, 4, 5]
print(f'Before: {source}')
print(f'Empty queue: {queue.is_empty()}')
array_to_queue(queue, source)
print(f'After: {source}')
print('Queue contents:')
for i in queue:
    print(i)
print('End of queue')
print('-' * 50)
queue_test(queue)
print(f'Empty queue: {queue.is_empty()}')
print('-' * 50)
print('Queue to array...')
print('Queue contents:')
for i in queue:
    print(i)
target = []
print(f'Target before: {target}')
queue_to_array(queue, target)
print(f'Target after: {target}')
print(f'Empty queue: {queue.is_empty()}')