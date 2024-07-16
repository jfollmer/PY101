# PY101-109 Small Problems, Easy 3, Problem 2. "ddaaiillyy ddoouubbllee":

"""Write a function that takes a string argument and returns a new 
string that contains the value of the original string with all 
consecutive duplicate characters collapsed into a single character.

Examples:
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
"""


def crunch(string):
    if string:
        crunched = string[0]
        prev_char = string[0]
        for char in string:
            if char != prev_char:
                crunched += char
                prev_char = char
        return crunched
    else:
        return string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')


"""Further Exploration: Regular expressions are also available in Python 
through the re module. If you're familiar with regular expressions, you 
can try to solve this problem using that module. Additionally, can you 
think of any other solutions that don't involve regular expressions, 
perhaps using Python's built-in string or list methods?
"""

# I am not familiar with regular expressions.

def crunch(string):
    if not string:
        return string
    crunched = string[0]
    for char in string:
        if not crunched.endswith(char):
            crunched += char
    return crunched

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')