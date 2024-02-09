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
from Food_utilities import read_foods

fv = open("Foods.txt", "r")

foods = read_foods(fv)

for i in foods:
    print(i.__str__())
    print("------------------------------")