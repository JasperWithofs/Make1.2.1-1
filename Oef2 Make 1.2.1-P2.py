#!/usr/bin/env python

#  Description
"""A program that checks if your number is even """
# Futures
# Libs

__author__ = "Jasper Withofs"
__email__ = "jasper.withofs@student.kdg.be"
__version__ = "1.0.1"
__status__ = "Development"

num = int(input("enter a number: "))

if (num % 2) == 0:
    print(num, " is even ")
else:
    print(num, " is odd")
