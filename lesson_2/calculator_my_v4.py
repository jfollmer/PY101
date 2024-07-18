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
        DONE
More modifications I'd like:
    - rewrite check_validity() using a try-except block
        DONE
    - nested functions don't actually need to be nested functions
        DONE
    - remove check_divide() and just use its code inside calculate()
        DONE
    - support power and square root operations
        DONE
    - reorganize code
        DONE
"""

from math import sqrt

# Accept various operation inputs:
operations = {
    'add': {'1', '1)', '+', 'add', 'addition', 'plus'},
    'subtract': {'2', '2)', '-', 'subtract', 'subtraction', 'minus'},
    'multiply': {'3', '3)', '*', 'multiply', 'multiplication', 'times'},
    'divide': {'4', '4)', '/', 'divide', 'division', 'divided by', 'divided'},
    'power': {'5', '5)', '^', '**' 'power', 'to the power of'},
    'sqroot': {'6', '6)', '√', 'sqrt' , 'square root', 'squareroot', 'root',
               'sqroot'},
}

# Unique terminal prompt:
# Use prompt() instead of print()
def prompt(message):
    print(f"==> {message}")

# Use input_prompt() instead of input()
def input_prompt():
    return input("==>: ")

# import pdb
# Get a number, and if not correct format, get a new one:
def get_number(op=None):
    number = input_prompt()

    try:
        number = float(number)
        if op == 'divide' and number == 0:
            print(3, op, number)
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

    else:     # accidentally discovered for-else blocks, documentation confirms
        prompt("Not a valid operation type.")              # validity and usage
        prompt("Please enter the number, name, or symbol of the operation:")
        return get_operation()


# Get number(s) and the operation, plus some logic if divide or sqroot:
def get_inputs():
    prompt("What's the first number?")
    num1 = get_number()
    prompt("What operation would you like to perform?")
    op = get_operation()

    if op == 'sqroot':
        return (num1, None, op)
    else:
        prompt("What's the second number?")
        num2 = get_number(op)
        return (num1, num2, op)

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

def calculate_again():
    prompt("Would you like to do another calculation? (y/n)")
    answer = input_prompt()
    
    if answer.casefold() not in {'y', 'n', 'yes', 'no'}:
        prompt("Please enter 'y' or 'n':")
        answer = input_prompt()
    
    return answer[0] == 'y'

prompt('Welcome to Calculator!')

while True:

    number1, number2, operation = get_inputs()

    # Run calculation and and print to terminal.
    result = format_output(calculate(number1, number2, operation))
    prompt(f"The result is: {result}")

    answer = calculate_again()
    if answer == False:
        break