"""Calculator version 2.1
I wanted to have fun with the calculator program from assignment 
7. 'Walk-through: Calculator' and give it extra features. This version
was done after assignment 11. 'Walk-through: Refactoring Calculator'.
Modifications to make (from v2):
    - handle divide by zero
        DONE
    - make if-else block into a function
        DONE
    - handle words entered for operations
        DONE
    - drop the decimal in ouput if .0
        DONE
    - handle non-digit characters for numbers
        DONE
    - convert words to numbers (for fun, more advanced handling of 
      strings)
        NOT DONE in this version
More modifications as per assignment 11:
    - create a unique terminal prompt
        DONE
    - make if-else block a match-case block
        DONE for calculate() but not get_operation() (doesn't work with 
        'in')
    - ask if user wants to perform another calculation and start over if 
      so
        NOT DONE in this version
More modifications I'd like:
    - rewrite check_validity() using a try-except block
        DONE
    - nested functions don't actually need to be nested functions
        DONE
    - remove check_divide() and just use its code inside calculate()
        DONE
    - support power and square root operations
        DONE
"""

from math import sqrt

# Unique terminal prompt:
# Use prompt() instead of print()
def prompt(message):
    print(f"==> {message}")

# Use input_prompt() instead of input()
def input_prompt():
    string = input("==>: ")
    return string

prompt('Welcome to Calculator!')

# Get a number, and if not correct format, get a new one:
def get_number():
    number = input_prompt()

    try:
        float(number)
    except ValueError:
        prompt("Unsupported format. Accepted characters include numbers 0-9, "
               "a negative sign (-), and a decimal (.). Please enter a new "
               "second number.")
        return get_number()

    return float(number)

# Accept various operation inputs:
add = ['1', '1)', 'add', 'addition', '+', 'plus']
subtract = ['2', '2)', '-', 'subtract', 'subtraction', 'minus']
multiply = ['3', '3)', '*', 'multiply', 'multiplication', 'times']
divide = ['4', '4)', '/', 'divide', 'division', 'divided by', 'divided']
power = ['5', '5)', '^', '**' 'power', 'to the power of']
sqroot = ['6', '6)', '√', 'sqrt', 'square root', 'squareroot', 'root',
          'sqroot']

# Get an operation, and if not correct format, get a new one:
def get_operation():
    prompt("1) Add (+)  2) Subtract (-)  3. Multiply (*)  4. Divide (/)")
    prompt("5) Power (^ or **)  6) Square Root (√)")
    operation = input_prompt()

    if operation.casefold() in add:
        return 'add'
    elif operation.casefold() in subtract:
        return 'subtract'
    elif operation.casefold() in multiply:
        return 'multiply'
    elif operation.casefold() in divide:
        return 'divide'
    elif operation.casefold() in power:
        return 'power'
    elif operation.casefold() in sqroot:
        return 'sqroot'
    else:
        prompt("Not a valid operation type.")
        prompt("Please enter the number, name, or symbol of the operation:")
        return get_operation()

# Get number(s) and the operation, plus some logic if divide or sqroot:
def get_inputs():

    # Ask the user for the first number.
    prompt("What's the first number?")
    number1 = get_number()

    # Ask the user for an operation to perform.
    prompt("What operation would you like to perform?")
    operation = get_operation()

    if operation == 'sqroot':
        return (number1, None, operation)

    else:
        # Ask the user for the second number.
        prompt("What's the second number?")
        number2 = get_number()

        # Don't divide by zero:
        if operation == 'divide' and number2 == 0:
            prompt("Can't divide by zero. Please enter a new second number.")
            number2 = get_number()

        return (number1, number2, operation)

number1, number2, operation = get_inputs()

# Perform the operation, and don't divide by zero:
def calculate(number1, number2, operation):
    match operation:
        case 'add':
            return number1 + number2
        case 'subtract':
            return number1 - number2
        case 'multiply':
            return number1 * number2
        case 'divide':
            return number1 / number2
        case 'power':
            return number1**number2
        case 'sqroot':
            return sqrt(number1)

# Format the result to make the decimals look nicer:
def format_output(result):
    return int(result) if result % 1 == 0 else result

# Run calculation and and print to terminal.
result = format_output(calculate(number1, number2, operation))
prompt(f"The result is: {result}")