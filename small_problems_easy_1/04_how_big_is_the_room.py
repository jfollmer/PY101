# PY101-109 Small Problems, Easy 1, Problem 4:

"""Build a program that asks the user to enter the length and width of a 
room, in meters, then prints the room's area in both square meters and 
square feet.

Note: 1 square meter == 10.7639 square feet
"""


def calculate_area(l, w):
    square_meters = l * w
    square_feet = l * w * 10.7639
    print(f'The area of the room is {square_meters} square meters '
          f'({square_feet} square feet).')

print("Please enter the dimensions of the room you'd like to calculate"
      "the area of.")
length = float(input("Length in meters: "))
width = float(input("Width in meters: "))

calculate_area(length, width)