"""Calculator version 4 - final version! (pretty much ...)

I wanted to have fun with the calculator program from assignment 
7. 'Walk-through: Calculator' and give it extra features. This version
was done after completing PY101.

Modifications to make in this version:
    - make valid operations a dictionary, adjust function to accommodate
        DONE
    - reorganize order of code so it makes more sense
        DONE
    - convert words to numbers (for fun, more advanced handling of 
      strings)
        NOT DONE in this version
Modifications as learned in various assignments:
    - make final changes pylint recommended (per assignment 10)
        DONE
    - ask if user wants to perform another calculation and start over if 
      so (per assignment 11)
        DONE
    - make functions shorter by condensing logic / putting it in more
      logical places / making function responsibilities make more sense
      (per coding tips assignments 22 & 27)
        DONE
    - add banner to welcome message (see bannerizer exercise), make
      things prettier in general
        DONE
    - add translations (per assignment 19)
        NOT DONE
"""

from math import sqrt

# Accept various operation inputs:
operations = {
    'add': {'1', '1)', '+', 'add', 'addition', 'plus'},
    'subtract': {'2', '2)', '-', 'subtract', 'subtraction', 'minus'},
    'multiply': {'3', '3)', '*', 'multiply', 'multiplication', 'times'},
    'divide': {'4', '4)', '/', 'divide', 'division', 'divided by', 'divided'},
    'power': {'5', '5)', '^', '**', 'power', 'to the power of'},
    'sqroot': {'6', '6)', '√', 'sqrt' , 'square root', 'squareroot', 'root',
               'sqroot'},
}

# Put welcome message in banner:
def print_welcome_message(message):
    prompt('+--' + '-' * len(message) + '--+')
    prompt('|  ' + ' ' * len(message) + '  |')
    prompt('|  ' + message + '  |')
    prompt('|  ' + ' ' * len(message) + '  |')
    prompt('+--' + '-' * len(message) + '--+')

# Unique terminal prompts:
# Use prompt() instead of print()
def prompt(message=''):
    print(f"==> {message}")

# Use input_prompt() instead of input()
def input_prompt(message=''):
    return input(f"==>: {message}")

# Get a number, and if not correct format, get a new one:
def get_number(op=None):
    number = input_prompt()

    try:
        number = float(number)
        if op == 'divide' and number == 0:
            prompt("Can't divide by zero. Please enter a new second number.")
            number = get_number(op)
        return number

    except ValueError:
        prompt("Unsupported format. Accepted characters include numbers 0-9, ")
        prompt("a negative sign (-), and a decimal (.). Please try again. ")
        return get_number(op)

# Get an operation, and if not correct format, get a new one:
def get_operation():
    prompt("1) Add (+)  2) Subtract (-)  3. Multiply (*)  4. Divide (/)")
    prompt("5) Power (^ or **)  6) Square Root (√)")
    op = input_prompt()

    for key, value_set in operations.items():
        if op.casefold() in value_set:
            return key

    prompt("Not a valid operation type.")
    prompt("Please enter the number, name, or symbol of the operation:")
    return get_operation()

# Get number(s) and the operation, plus some logic if divide or sqroot:
def get_inputs():
    prompt()
    prompt("What's the first number?")
    num1 = get_number()
    prompt()
    prompt("What operation would you like to perform?")
    op = get_operation()

    if op == 'sqroot':
        return (num1, None, op)

    prompt()
    prompt("What's the second number?")
    num2 = get_number(op)
    return (num1, num2, op)

# Perform the operation, and don't divide by zero:
def calculate(num1, num2, op):
    match op:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            return num1 / num2
        case 'power':
            return num1**num2
        case 'sqroot':
            return sqrt(num1)

# Format the result to make the decimals look nicer:
def format_output(rslt):
    return int(rslt) if rslt % 1 == 0 else rslt

def calculate_again():
    prompt()
    prompt("Would you like to do another calculation? (y/n)")
    ans = input_prompt()

    if ans.casefold() not in {'y', 'n', 'yes', 'no'}:
        prompt("Please enter 'y' or 'n':")
        ans = input_prompt()

    return ans[0] == 'y'

while True:
    prompt()
    print_welcome_message('Welcome to Calculator!')

    number1, number2, operation = get_inputs()

    result = format_output(calculate(number1, number2, operation))

    prompt()
    prompt(f"The result is: {result}")

    answer = calculate_again()
    if answer is False:
        prompt("Thank you for using Calculator!")
        break