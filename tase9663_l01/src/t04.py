"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_food

k = read_food("Spanakopita|5|True|260")

print(k.__str__())

t = Food("blank", 5, True, 0)
