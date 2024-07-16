# PY101-109 Small Problems, Easy 3, Problem 8. "Grade Book":

"""Write a function that determines the mean (average) of the three 
scores passed to it, and returns the letter associated with that grade.

Numerical score letter grade list:

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'

Tested values are all between 0 and 100. There is no need to check for 
negative values or values greater than 100.

Examples:
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
"""


def get_grade(score1, score2, score3):
    avg_grade = (score1 + score2 + score3) / 3
    if avg_grade < 60:
        letter_grade = 'F'
    elif avg_grade < 70:
        letter_grade = 'D'
    elif avg_grade < 80:
        letter_grade = 'C'
    elif avg_grade < 90:
        letter_grade = 'B'
    else:
        letter_grade = 'A'
    return letter_grade

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True


# Given solution uses return statements in each if statement, but I
# didn't since pylint was unhappy about "too many return statements" 
# before.