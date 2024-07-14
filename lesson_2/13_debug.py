# PY101, Lesson 2, assignment 15. Debugging Techniques


"""Program with no errors to practice with pdb (comment out to test 
the second program later):
"""

# import pdb

# counter = 1

# while counter <= 5:
#     print(counter)
#     pdb.set_trace() # add breakpoint
#     counter += 1


"""Program with an error for more practice (comment out to test the first
program instead):
"""

import pdb

cats = []

for name in ('Powder', 'Sky', 'Cheddar', 'Cocoa'):
    pdb.set_trace()
    cats + [name]

print(cats) # Expected Output: ['Powder', 'Sky', 'Cheddar', 'Cocoa'] 