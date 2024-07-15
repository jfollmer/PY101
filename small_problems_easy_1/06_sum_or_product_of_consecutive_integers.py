# PY101-109 Small Problems, Easy 1, Problem 6. "Sum or Product of
# Consecutive Integers":

"""Write a program that asks the user to enter an integer greater than 
0, then asks whether the user wants to determine the sum or the product 
of all numbers between 1 and the entered integer, inclusive.

Example 1:

Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.

Example 2:

Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.
"""


# Comment out whichever version you're not testing, or just let both run

def get_number():
    number = input('Please enter an integer greater than 0: ')

    try:
        number = int(number)
    except ValueError:
        print('Please try again.')
        number = get_number()

    return number

def get_operation():
    op = input('Enter "s" to compute the sum, or "p" to compute the '
               'product. ').lower().strip('" ').strip("'")

    if op not in {'s', 'p'}:
        print('Please try again.')
        op = get_operation()

    if op == 's':
        op = 'sum'
    if op == 'p':
        op = 'product'
    return op

def calculate_result(number, op):
    if op == 'sum':
        rslt = sum(range(1, number + 1))
    if op == 'product':
        rslt = 1
        for num in range(1, number + 1):
            rslt *= num

    return rslt

integer = get_number()

operation = get_operation()

result = calculate_result(integer, operation)

print()
print(f'The {operation} of the integers between 1 and {integer} is {result}.')

# Given solution looks different but works the same way, except it 
# doesn't try to get new input if the input is wrong or format the
# input.
# Given solution uses sum(range(...)), which I implemented.

"""Further Exploration: Suppose the input was a list of space separated 
integers instead of just a single integer? How would your compute_sum 
and compute_product functions change?
"""

def get_numbers():
    print('Please enter the integers you would like to compute together, '
          'separated by spaces:')
    numbers = input().strip(' ').split(' ')

    try:
        numbers = [ int(number) for number in numbers ]
    except ValueError:
        print('Please try again.')
        numbers = get_numbers()

    return numbers

def get_operation():
    op = input('Enter "s" to compute the sum, or "p" to compute the '
               'product. ').lower().strip('" ').strip("'")

    if op not in {'s', 'p'}:
        print('Please try again.')
        op = get_operation()

    if op == 's':
        op = 'sum'
    if op == 'p':
        op = 'product'
    return op

def calculate_result(numbers, op):
    if op == 'sum':
        rslt = sum(numbers)
    if op == 'product':
        rslt = 1
        for num in numbers:
            rslt *= num

    return rslt

integers = get_numbers()

operation = get_operation()

result = calculate_result(integers, operation)

print()
print(f"The {operation} of the integers "
      f"{', '.join([ str(n) for n in integers ])} is {result}.")