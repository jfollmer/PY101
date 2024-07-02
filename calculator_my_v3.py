"""I wanted to have fun with the calculator program from assignment 
7. "Walk-through: Calculator" and give it extra features. This version
was done after assignment 11. "Walk-through: Refactoring Calculator".


"Modifications to make (from v2):
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
    - rewrite check_validity() using a try-except block
        DONE
    - nested functions don't actually need to be nested functions
        DONE
    - remove check_divide() and just use its code inside calculate()
        DONE
    - ask if user wants to perform another calculation and start over if 
      so
        NOT DONE in this version
"""

# Unique terminal prompt:
def prompt(message):
    print(f"==> {message}")

prompt('Welcome to Calculator!')


# Get a number and check for correct format:
def get_number():
    number = input("==> ")

    try:
        float(number)
    except ValueError:
        prompt('Please enter a number (may include a decimal):  ')
        return get_number()
    return float(number)

# Get an operation and check for correct format:
def get_operation():
    operation = input("==> ")

    add = ['1', 'add', 'addition', '+', 'plus']
    subtract = ['2', 'subtract', 'subtraction', '-', 'minus']
    multiply = ['3', 'multiply', 'multiplication', '*', 'times']
    divide = ['4', 'divide', 'division', '/', 'divided by', 'divided']

    if operation.casefold() in add:
        return 'add'
    elif operation.casefold() in subtract:
        return 'subtract'
    elif operation.casefold() in multiply:
        return 'multiply'
    elif operation.casefold() in divide:
        return 'divide'
    else:
        prompt("Not a valid operation type.")
        prompt("Please enter the number, name, or symbol of the operation.")
        prompt("1. Add (+)  2. Subtract (-)  3. Multiply (*)  4. Divide (/):")
        return get_operation()


# Ask the user for the first number.
prompt("What's the first number?:   ")
number1 = get_number()

# Ask the user for the second number.
prompt("What's the second number?:  ")
number2 = get_number()

# Ask the user for an operation to perform.
prompt("What operation would you like to perform?")
prompt("1) Add (+)  2) Subtract (-)  3. Multiply (*)  4. Divide (/):  ")
operation = get_operation()


# Perform the operation on the two numbers and return the result.
def calculate(number1, number2, operation):
    match operation:
        case 'add':
            return number1 + number2
        case 'subtract':
            return number1 - number2
        case 'multiply':
            return number1 * number2
        case 'divide':
            if number2 == 0:
                prompt("Cannot divide by zero. "
                       "Please enter a different second number:")
                number2 = get_number()
            return number1 / number2


# Format the result to make the decimals look nicer:
def format_output(result):
    return int(result) if result % 1 == 0 else result

# Run calculation and and print to terminal.
result = format_output(calculate(number1, number2, operation))
prompt(f"The result is: {result}")