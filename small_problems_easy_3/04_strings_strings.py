# PY101-109 Small Problems, Easy 3, Problem 4. "Strings Strings":

"""Write a function that takes one argument, a positive integer, and 
returns a string of alternating '1's and '0's, always starting with a 
'1'. The length of the string should match the given integer.

Exapmles:
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
"""


def stringy(n):
    string = ''

    while len(string) < n:
        if not string.endswith('1'):
            string = string + '1'
        else:
            string = string + '0'

    return string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True


# Given solution is nicer:

def stringy(size):
    result = ""
    for idx in range(size):
        digit = '1' if idx % 2 == 0 else '0'
        result += digit

    return result