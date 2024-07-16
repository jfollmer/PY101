# PY101-109 Small Problems, Easy 2, Problem 6. "The End Is Near But Not 
# Here":

"""Write a function that returns the next to last word in the string 
argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two 
words.

Examples:
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
"""


def penultimate(string):
    return string.split()[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")


"""Further Exploration: Our solution ignored two edge cases since we 
explicitly stated that you didn't have to handle them: strings that 
contain no words or just one word.

Suppose we need a function that retrieves the middle word of a 
phrase/sentence. What edge cases need to be considered? How would you 
handle those edge cases without ignoring them? Write a function that 
returns the middle word of a phrase or sentence. It should handle all 
of the edge cases you thought of.
"""

def middle_word(string):
    words = string.split(' ')
    try:
        if len(words) == 2:
            return string
        elif len(words) % 2 == 1: # handles len == 1 and odd lengths
            return words[len(words)//2]
        elif len(string) % 2 == 0:
            return ' '.join(words[len(words)//2 - 1 : len(words)//2 + 1])
        else:
            print('else')
    except IndexError: # handles 0
        print(4)
        return string

print(middle_word("one"))
print(middle_word("last word"))
print(middle_word("one two three"))
print(middle_word("one two three four"))

# I decided to return both of the middle words for even-length sentences
# so the user can decide which one they want.