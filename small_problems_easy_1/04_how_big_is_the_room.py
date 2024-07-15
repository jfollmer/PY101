# PY101-109 Small Problems, Easy 1, Problem 4:

"""Build a program that asks the user to enter the length and width of a 
room, in meters, then prints the room's area in both square meters and 
square feet.

Note: 1 square meter == 10.7639 square feet
"""


def get_length():
    l = input("Length in meters: ")

    try:
        l = float(l)
    except ValueError:
        print("Please try again.")
        l = get_length()

    return l

def get_width():
    w = input("Width in meters: ")

    try:
        w = float(w)
    except ValueError:
        print("Please try again.")
        w = get_width()

    return w

def calculate_area(l, w):
    square_meters = l * w
    square_feet = l * w * 10.7639
    return square_meters, square_feet

print("Please enter the dimensions of the room you'd like to calculate"
      "the area of.")

length = get_length()
width = get_width()

sq_meters, sq_feet = calculate_area(length, width)

print(f'The area of the room is {sq_meters} square meters '
          f'({sq_feet} square feet).')

# Given solution does not use functions or input validation but works
# basically the same way.