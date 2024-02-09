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
from Food_utilities import write_foods

fv = open("foods.txt", "w")

k = Food("Biryani", 2, False, 130)
y = Food("Beaver Tail", 0, True, 500)

l = [k, y]

write_foods(fv, l)