"""Calculator version 2

I wanted to have fun with the calculator program from assignment 
7. 'Walk-through: Calculator' and give it extra features.

Modifications to make:
    - handle divide by zero
        DONE
    - allow floats for inputs
        DONE
    - make if-else block into a function
        DONE
    - handle words entered for operations
        DONE
    - drop the decimal in ouput if .0
        DONE
    - handle non-digit characters for numbers (causes error now)
        DONE but can be nicer (fixed in v3)
    - call check_divide() inside calculate()
        DONE
    - convert words to numbers (for fun, more advanced handling of 
      strings)
        NOT DONE for this version
Done with this version. See calculator_my_v3.py for more changes.
"""


print('Welcome to Calculator!')


# Get a number and check for correct format:
def get_number():
    number = input()

    # handle non-digit inputs for numbers:
    for char in number:
        if not (char.isdigit() or char == '.'):
            print('Unsupported format. Please enter a number (may include a '
                  'negative sign and/or a decimal):  ', end='')
            return get_number()
    return float(number)

# Get an operation and check for correct format:
def get_operation():
    operation = input()

    add = ['1', '1)', 'add', 'addition', '+', 'plus']
    subtract = ['2', '2)', 'subtract', 'subtraction', '-', 'minus']
    multiply = ['3', '3)', 'multiply', 'multiplication', '*', 'times']
    divide = ['4', '4)', 'divide', 'division', '/', 'divided by', 'divided']

    if operation.casefold() in add:
        return 'add'
    elif operation.casefold() in subtract:
        return 'subtract'
    elif operation.casefold() in multiply:
        return 'multiply'
    elif operation.casefold() in divide:
        return 'divide'
    else:
        print("Operation type not supported.\nPlease enter the number, name, "
              "or symbol of the operation you wish to perform.\n1. Add (+)  "
              "2. Subtract (-)  3. Multiply (*)  4. Divide (/):  ", end='')
        return get_operation()


# Ask the user for the first number.
print("What's the first number?:   ", end='')
number1 = get_number()

# Ask the user for the second number.
print("What's the second number?:  ", end='')
number2 = get_number()

# Ask the user for an operation to perform.
print("What operation would you like to perform?\n"
      "1) Add (+)  2) Subtract (-)  3. Multiply (*)  4. Divide (/):  ", 
      end='')
operation = get_operation()


# handle divide by zero:
def check_divide(number2):
    if number2 == 0:
        print("Can't divide by zero. Enter a new second number:  ", end='')
        return get_number()
    return number2

# Perform the operation on the two numbers and return the result.
def calculate(number1, number2, operation):
    if operation == 'add':
        return number1 + number2
    elif operation == 'subtract':
        return number1 - number2
    elif operation == 'multiply':
        return number1 * number2
    elif operation == 'divide':
        number2 = check_divide(number2)
        return number1 / number2


# Format the result to make the decimals look nicer:
def format_output(result):
    return int(result) if result % 1 == 0 else result

# Run calculation and and print to terminal.
result = format_output(calculate(number1, number2, operation))
print(f"The result is:\n"
      f"{result}")