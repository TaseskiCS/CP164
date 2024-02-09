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

from Queue_circular import Queue

queue = Queue(3)

print(len(queue))

print(queue.is_empty())

queue.insert(100)

print(len(queue))

value = queue.peek()

print(value)

removed = queue.remove()

print(removed)



queue.insert(100)
queue.insert(200)
queue.insert(300)
print(queue.is_full())