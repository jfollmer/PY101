# PY101-109 Small Problems, Easy 2, Problem 9. "How Old is Teddy?":

"""Build a program that randomly generates and prints Teddy's age. To 
get the age, you should generate a random number between 20 and 100, 
inclusive.

Example Output:
Teddy is 69 years old!
"""


import random

age = random.randint(20, 100)

print(f'Teddy is {age} years old!')

"""Further Exploration: Modify this program to ask for a name, then 
print the age for that person. For an extra challenge, use "Teddy" as 
the name if no name is entered.
"""


name = input("Who's age would you like?: ")
age = random.randint(20, 100)

print(f"{name if name else 'Teddy'} is {age} years old!")