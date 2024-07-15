# PY101, Lesson 3, Assignment 6. "Practice Problems: Hard 1":

# Question 1: Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# Try to answer without running the code or looking at the solution.

"""No, because first() has a dictionary that begins on the same line as 
the return statement, so that's what's returned and passed to print(). 
But second() has the dictionary beginning on the next line after the 
return statement, and no code after a return statement executes, so it 
returns the default, None.
"""


# Question 2: What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# Try to answer without running the code or looking at the solution.

"""It prints {'first: [1, 2]}. On the second line, the reference to the
value associated with the key 'first', which is a nested list, is 
assigned to num_list. Since it's nested, the dictionary only contains a
pointer to this list, as does num_list. So when this object is mutated 
on the third line, both variables reflect this change.
"""


# Question 3: Given the following similar sets of code, what will each 
# code snippet print?

# A)

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# This prints:
# ["one"]
# ["two"]
# ["three"]
# because of variable shadowing. The variables are passed into 
# parameters of the same names within the function, which shadown the 
# global variables, so although the variables are reassigned within the
# function, the global variables are not reassigned.

# B)

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# This prints:
# ["one"]
# ["two"]
# ["three"]
# because of the same reason, variable shadowing. The reassignments 
# within the function do not affect the global variables.

# C)

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# This prints:
# ["two"]
# ["three"]
# ["one"]
# because the index reassignments inside the function are mutating the
# lists, so the global variables reflect this change.
# Given solution mentions "pass-by-reference". This is how a function is
# able to modify a global variable.


"""Question 4: Ben was tasked to write a simple Python function to 
determine whether an input string is an IP address using 4 dot-separated 
numbers, e.g., 10.4.5.11.
Alyssa supplied Ben with a function named is_an_ip_number. It determines 
whether a string is a numeric string between 0 and 255 as required for 
IP numbers and asked Ben to use it. Here's the code that Ben wrote:
"""

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True

"""Alyssa reviewed Ben's code and said, "It's a good start, but you 
missed a few things. You're not returning a false condition, and you're 
not handling the case when the input string has more or less than 4 
components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be 
invalid."
Help Ben fix his code.
"""

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")

    if len(dot_separated_words) != 4:
        return False
    
    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address('10.4.5.11'))
print(is_dot_separated_ip_address('4.5.5'))
print(is_dot_separated_ip_address('1.2.3.4.5'))
print(is_dot_separated_ip_address('1.2.3.a'))


# Question 5: What do you expect to happen when the greeting variable is 
# referenced in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

"""This will raise a NameError, because the if False block will never
execute, so greeting is never initialized and doesn't exist in the 
namespace.
"""