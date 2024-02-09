"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2024-02-08"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import gcd

m = int(input("Enter an integer: "))
n = int(input("Enter another integer: "))
ans = gcd(m, n)

print("The greatest common denominator of", m, "and", n, "is", ans)