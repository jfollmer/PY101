"""
Write out pseudocode (both casual and formal) that does the following:

1. a function that returns the sum of two numbers
2. a function that takes a list of strings, and returns a string that is 
    all those strings concatenated together
3. a function that takes a list of integers, and returns a new list with 
    every other element from the original list, starting with the first 
    element. For instance:
    every_other([1,4,7,2,5]) # => [1,7,5]
4. a function that determines the index of the 3rd occurrence of a given 
    character in a string. For instance, if the given character is 'x' 
    and the string is 'axbxcdxex', the function should return 6 (the 
    index of the 3rd 'x'). If the given character does not occur at 
    least 3 times, return None.
5. a function that takes two lists of numbers and returns the result of 
    merging the lists. The elements of the first list should become the 
    elements at the even indexes of the returned list, while the 
    elements of the second list should become the elements at the odd 
    indexes. For instance:
    merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
    You may assume that both list arguments have the same number of 
    elements.

You don't need to write any Python code here; just practice writing the 
    logic in English.
"""


"""1. a function that returns the sum of two numbers:

# Casual pseudocode:
Function definition with two parameters, one for each number
    Return the calculated sum

# Formal pseudocode:

START

Given two numbers: number1 and number2

DEF function(number1, number2):
    RETURN number1 + number2

END

"""

"""2. a function that takes a list of strings, and returns a string that is 
    all those strings concatenated together:

# Casual pseudocode:
Function definition with one parameter (list of strings):
    Initialize a new empty string
    For item in list:
        Concatenate item to the new string
    Return new string

# Formal pseudocode:

START

Given a list of strings, "list"

DEF function(list):
    SET newString = empty string
    FOR element in list:
        newString += element
    RETURN newString

END

"""

"""3. a function that takes a list of integers, and returns a new list with 
    every other element from the original list, starting with the first 
    element. For instance:
    every_other([1,4,7,2,5]) # => [1,7,5]

# Casual pseudocode:
Function definition with one parameter (list of integers):
    Initialize empty list
    For every other number in a range 0 to len(list):
        Add item at index of range number from original list to new list
    Return new list

# Formal pseudocode:

START

Given a list of integers, "list"

DEF function(list):
    SET newList = empty list
    FOR every other number in range(len(list)):
        newList.append( element from list at index position from range )
    RETURN newList

END

"""

"""4. a function that determines the index of the 3rd occurrence of a given 
    character in a string. For instance, if the given character is 'x' 
    and the string is 'axbxcdxex', the function should return 6 (the 
    index of the 3rd 'x'). If the given character does not occur at 
    least 3 times, return None.

# Casual pseudocode:
Function definition with two parameters (a string, character being searched for):
    Initialize counter
    For character in string:
        If character == desired character:
            Increase counter
        If counter == 3:
            Return index position of character
    Otherwise return None

# Formal pseudocode:

START

Given a string, "string", find 3rd occurrence of given charaacter

DEF function(string, desiredChar):
    SET counter = 0
    FOR character in string:
        IF character == desiredChar:
            counter += 1
        IF counter == 3:
            RETURN index position of character
    RETURN None

END

"""

"""5. a function that takes two lists of numbers and returns the result of 
    merging the lists. The elements of the first list should become the 
    elements at the even indexes of the returned list, while the 
    elements of the second list should become the elements at the odd 
    indexes. For instance:
    merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
    You may assume that both list arguments have the same number of 
    elements.

# Casual pseudocode:
Function definition with two parameters (lists of numbers):
    Initialize new empty list
    For number in range 0 to len(list1) (assume equal lengths for both lists):
        Add element from list2 to new list (should occupy odd index positions)
        Add element from list1 to new list (should occupy even index positions)
    Return new list

# Formal pseudocode:

START

Given two lists of numbers, "list1" and "list2"

DEF function(list1, list2):
    SET mergedList = empty list
    FOR number in range(0, len(list1):
        mergedList.append( element at index=number from list2 )
        mergedList.append( element at index=number from list1 )
    RETURN mergedList

END

"""