# PY101-109 Small Problems, Easy 2, Problem 10. "When Will I Retire?":

"""Build a program that displays when the user will retire and how many 
years she has to work till retirement.

Example:

What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
"""


import datetime

age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))
years_to_go = retirement_age - age

this_year = datetime.date.today().year
retirement_year = this_year + years_to_go

print()
print(f"It's {this_year}. You will retire in {retirement_year}. "
      f"You have only {years_to_go} years of work to go!")