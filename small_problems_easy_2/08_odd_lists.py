# PY101-109 Small Problems, Easy 2, Problem 8. "Odd Lists":

"""Write a function that returns a list that contains every other 
element of a list that is passed in as an argument. The values in the 
returned list should be those values that are in the 1st, 3rd, 5th, and 
so on elements of the argument list.

Examples:
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

Bonus question: Try to solve the problem using list slicing.
"""


def oddities(lst):
    odd_positions = []
    for i in range(0, len(lst), 2):
        odd_positions.append(lst[i])
    return odd_positions

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True


def oddities(lst):
    return lst[::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True