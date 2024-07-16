# PY101-109 Small Problems, Easy 2, Problem 2. "Greeting a User":

"""Write a program that asks for user's name, then greets the user. If 
the user appends a ! to their name, the computer will yell the greeting 
(print it using all uppercase).

Example 1:
What is your name? Sue
Hello Sue.

Example 2:
What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?
"""


def greet(name_input):
    if name_input[-1] == '!':
        print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {name_input}.")

name = input("What is your name?  ")

greet(name)

# Given solution uses .endswith() instead of [-1].