# PY101-109 Small Problems, Easy 1, Problem 2. "Odd Numbers":

"""Print all odd numbers from 1 to 99, inclusive, with each number on a 
separate line.

Bonus Question: Can you solve the problem by iterating over just the odd 
numbers?
"""

for i in range(1, 100, 2):
    print(i)

"""Further Exploration: Consider adding a way for the user to specify 
the starting and ending values of the odd numbers printed.
"""

def print_odds(s, e):
    for i in range(s, e + 1):
        if i % 2 == 1:
            print(i)

print('Please enter the start and end values of the odd numbers you '
      'would like to print.')
start = int(input('Start: '))
end = int(input('End: '))

print_odds(start, end)