# PY101-109 Small Problems, Easy 3, Problem 1. "Repeat Yourself":

"""Write a function that takes two arguments, a string and a positive 
integer, then prints the string as many times as the integer indicates.

Example:
repeat('Hello', 3)

Output:
Hello
Hello
Hello
"""

def repeat(string, times):
    for _ in range(times):
        print(string)

repeat('Hello', 3)