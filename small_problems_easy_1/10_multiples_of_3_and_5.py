# PY101-109 Small Problems, Easy 1, Problem 10. "Multiples of 3 and 5":

"""Write a function that computes the sum of all numbers between 1 and 
some other number, inclusive, that are multiples of 3 or 5. For 
instance, if the supplied number is 20, the result should be 98 
(3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.

Examples:
# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
"""


def multisum(end_number):
    numbers = []
    for num in range(1, end_number + 1):
        if num % 3 == 0 or num % 5 == 0:
            numbers.append(num)
    return sum(numbers)

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

# Given solution uses a helper function and says it makes the main
# function more readable, but I'm not sure I agree (but I'm still 
# learning what other people consider readable):

def is_multiple(number, divisor):
    return number % divisor == 0

def multisum(max_value):
    total_sum = 0
    for number in range(1, max_value + 1):
        if is_multiple(number, 3) or is_multiple(number, 5):
            total_sum += number
    return total_sum