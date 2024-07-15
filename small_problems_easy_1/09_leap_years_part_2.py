# PY101-109 Small Problems, Easy 1, Problem 9. "Leap Years (Part 2)":

"""In the previous exercise, we assumed that the Gregorian calendar has 
been in continuous use since the year 1. However, the Gregorian calendar 
wasn't adopted until much later; prior to that, much of the world used 
the Julian calendar, which observed leap year every 4 years.

in 1752, England, Ireland, and the British colonies all switched to the 
Gregorian calendar. Update the function from the previous exercise so it 
uses the Julian calendar prior to 1752, and the Gregorian calendar 
starting in 1752.

Examples:
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
"""

def is_leap_year(year):
    if year < 1752:
        return year % 4 == 0
    else:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return year % 4 == 0

print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

"""Further Exploration: Different regions adopted the Gregorian calendar 
at different times. Investigate when it was adopted in various countries 
and how that transition was managed. Consider how this would impact the 
leap year calculation and potentially adjust the solution based on the 
country of reference.
"""

"""It seems like this would involve significan research. You would have 
to figure out which calendar each supported country was using prior to 
the Gregorian calendar, whether it was even the Julian calendar or some 
other calendar. If you omit the non-Julian ones, you could create a 
dictionary for each country, listing the year the Gregorian calendar 
begins. You'd have to consider which month the calendar was adopted in 
and whether it was before or after February when entering years into the 
calendar. Then your if condition could be if year < dictionary.get(country). 
And put a condition that prints "country not supported" in case the 
country is not currently in the dictionary.
"""
