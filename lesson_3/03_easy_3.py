# PY101, Lesson 3, Assignment 4. "Practice Problems: Easy 3":

# Come back to / repeat questions 1
# Give feedback for explanation for question 4

# Question 1: Write two different ways to remove all of the elements 
# from the following list:
numbers = [1, 2, 3, 4]

numbers.clear()
print('numbers:', numbers)

# Given solution uses a while loop. Try this.

numbers = [1, 2, 3, 4]
while numbers:
    numbers.pop()
print('numbers:', numbers)

# Question 2: What will the following code output?
print([1, 2, 3] + [4, 5])
# Try to answer without running the code.

# The two lists passed to print() are concatenated, so [1, 2, 3, 4, 5]
# prints.

# Question 3: What will the following code output?
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
# Try to answer without running the code.

# "hello there" prints, because although we assign str1 to str2 as a 
# reference on the second line, we perform reassignment to a new string
# object on the third line.

# Given solution mentions mutability, which I almost mentioned but 
# didn't since reassignment would happen even with mutable objects such 
# as lists, so the main concept seems to be pass-by-reference.

# Question 4: What will the following code output?
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
# Try to answer without running the code.

# The second line performs a shallow copy, which only copies the 
# references to any nested collections. So when we reassign the key
# 'first' of the first dictionary (the object at my_list[0]), it mutates
# the object pointed to by both lists, so both lists will reflect this
# change. The final line will print:
# [{"first": 42}, {"second": "value2"}, 3, 4, 5]

# Question 5: The following function unnecessarily uses two return 
# statements to return boolean values. Can you rewrite this function so 
# it only has one return statement and does not explicitly use either 
# True or False?
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
# Try to come up with two different solutions.

def is_color_valid(color):
    return color in {"blue", "green"}
print(is_color_valid("blue"))
print(is_color_valid("red"))

def is_color_valid(color):
    return color == "blue" or color == "green"
print(is_color_valid("blue"))
print(is_color_valid("red"))