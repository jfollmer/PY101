# PY101-109 Small Problems, Easy 3, Problem 5. "Right Triangles":

"""Write a function that takes a positive integer, n, as an argument and 
prints a right triangle whose sides each have n stars. The hypotenuse of 
the triangle (the diagonal side in the images below) should have one end 
at the lower-left of the triangle, and the other end at the upper-right.

Example 1:
triangle(5)

Output for Example 1:
    *
   **
  ***
 ****
*****

Example 2:
triangle(9)

Output for Example 2:
        *
       **
      ***
     ****
    *****
   ******
  *******
 ********
*********
"""


def triangle(n):
    for i in range(1, n + 1):
        print((' ' * (n - i)) + ('*' * i))

triangle(5)
triangle(9)


# Given solution:

def triangle(height):
    for num in range(1, height + 1):
        spaces = height - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')

# Student solution I like:

def triangle(n):
    for i in range(1, n + 1):
        stars = "*" * i
        print(stars.rjust(n))