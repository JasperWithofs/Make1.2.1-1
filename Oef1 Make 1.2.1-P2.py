#!/usr/bin/env python

# Description
"""
A program for a school project that gives you a personalized message that wil calculate
in what year you will turn 100 years old
"""
# Futures
# Libs
# Imports
import datetime

__author__ = "Jasper Withofs"
__email__ = "jasper.withofs@student.kdg.be"
__version__ = "1.0.1"
__status__ = "Development"


def calc_100():
    name = input("Enter name: ")
    today = datetime.date.today()
    age = int(input("Give your age: "))

    age_100 = int(today.year) + 100 - age
    print(name, ", you will be 100 years old in the year", str(age_100))
    restart = input("Do you want to restart the program? (Y/N)")

    if restart.lower() == "y":
        calc_100()
    elif restart.lower() == "n":
        exit()


calc_100()
