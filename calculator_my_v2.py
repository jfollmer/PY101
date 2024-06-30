"""Modifications to make:
    - handle divide by zero
        DONE
    - make if-else block into a function
        DONE
    - handle words entered for operations
        DONE but make it nicer
    - drop the decimal if .0
        DONE
    - handle non-digit characters for numbers (causes error now)
        DONE but can be nicer
    - convert words to numbers (for fun, more advanced handling of strings)
"""


print('Welcome to Calculator!')


# Get a number and check for correct format (convert to try-except block later):
def get_number():
    number = input()

    # handle non-digit inputs for numbers:
    def format_number(number):
        for char in number:
            if char.isdigit():
                continue
            elif char == '.':
                continue
            else:
                print('Please enter a number. Numbers may include decimals:  ')
                return get_number()
        return float(number)
    
    return format_number(number)


# Ask the user for the first number.
print("What's the first number?:   ", end='')
number1 = get_number()

# Ask the user for the second number.
print("What's the second number?:  ", end='')
number2 = get_number()

# Ask the user for an operation to perform.
print("What operation would you like to perform?\n"
      "1. Add 2. Subtract 3. Multiply 4. Divide:  ", end='')
operation = input()


# Handle numbers, words, and symbols as operations:
def format_operation(operation):
    
    add = ['1', 'add', 'addition', '+', 'plus']
    subtract = ['2', 'subtract', 'subtraction', '-', 'minus']
    multiply = ['3', 'multiply', 'multiplication', '*', 'times']
    divide = ['4', 'divide', 'division', '/', 'divided by', 'divided']
    
    if operation.isdigit():
        return operation
    elif operation.casefold() in add:
        return '1'
    elif operation.casefold() in subtract:
        return '2'
    elif operation.casefold() in multiply:
        return '3'
    elif operation.casefold() in divide:
        return '4'
    # else: # for future development
    #     print("Operation type not supported. Please run the program again")
    #     return '5'
    
operation = format_operation(operation)
    

# handle divide by zero:
def check_divide(operation, number2):
    if operation == '4' and number2 == 0:
        print("Cannot divide by zero. Please enter a different second number.\n"
              "What's the new second number?:  ", end='')
        number2 = float(input())
        return number2
    else:
        return number2

number2 = check_divide(operation, number2)


# Perform the operation on the two numbers and return the result.
def calculate(number1, number2, operation):
    if operation == '1':    # addition
        return number1 + number2
    elif operation == '2':  # subtraction
        return number1 - number2
    elif operation == '3':  # multiplication
        return number1 * number2
    elif operation == '4':  # division
        return number1 / number2
    else:
        pass # handle '5' from format_operation


# Format the result to make the decimals look nicer:
def format_output(result):
    return int(result) if result % 1 == 0 else result


# Run calculation and and print to terminal.
result = format_output(calculate(number1, number2, operation))
print(f"The result is:\n"
      f"{result}")