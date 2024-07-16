# PY101-109 Small Problems, Easy 3, Problem 9. "Clean up the words":

"""Given a string that consists of some words and an assortment of 
non-alphabetic characters, write a function that returns that string 
with all of the non-alphabetic characters replaced by spaces. If one or 
more non-alphabetic characters occur in a row, you should only have one 
space in the result (i.e., the result string should never have 
consecutive spaces).

Example:
print(clean_up("---what's my +*& line?") == " what s my line ")
# True
"""


def clean_up(string):
    cleaned = ''
    for char in string:
        if char.isalpha() and char.isascii():
            cleaned += char
        elif not cleaned.endswith(' '):
            cleaned += ' '
    return cleaned

print(clean_up("---what's my +*& line?") == " what s my line ") # True
# Given solution presents this problem, so I added and char.isascii():
print(clean_up("Καλωσήρθες") == "Καλωσήρθες")   # was True now False


# Given solution:

def is_ascii_letter(char):
    return char.isalpha() and char.isascii()

def clean_up(text):
    clean_text = ''

    for idx, char in enumerate(text):
        if is_ascii_letter(char):
            clean_text += char
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '

    return clean_text

print(clean_up("---what's my +*& line?") == " what s my line ") # True
print(clean_up("Καλωσήρθες") == "Καλωσήρθες")   # False

# Not sure why you need a new function when you can just add it as a 
# condition.