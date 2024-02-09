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
from Food_utilities import get_vegetarian, read_foods

fv = open("foods.txt", "r")

foods = read_foods(fv)

v = get_vegetarian(foods)

for i in v:
    print(i.__str__())
    print("----------------------")
