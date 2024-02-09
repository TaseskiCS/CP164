"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_table
from Food import Food
def main():
    food = Food("BBQ Pork",1,False,920)
    food1 = Food("Beef with Green Pepper",1,False,251)
    foods = [food1,food]
    print(food_table(foods))
main()