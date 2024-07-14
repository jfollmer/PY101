# PY101, Lesson 2, 11. "Walk-through: Refactoring Calculator"
# assignment. Adds a unique prompt and checks the validity of each input
# (both numbers and the operation).

# Create a distinctive prompt:
def prompt(message):
    print(f"==> {message}")

prompt('Welcome to Calculator!')

# Function to check validity of number inputs:
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

# Ask the user for the first number.
prompt("What's the first number?")
number1 = input()

# Check validity of number1 input:
while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

# Ask the user for the second number.
prompt("What's the second number?")
number2 = input()

# Check validity of number2 input:
while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

# Ask the user for an operation to perform.
prompt("What operation would you like to perform?\n"
      "1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

# Check validity of operation input:
while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

# Perform the operation on the two numbers.
match operation:
    case '1':    # addition
        output = int(number1) + int(number2)
    case '2':  # subtraction
        output = int(number1) - int(number2)
    case '3':  # multiplication
        output = int(number1) * int(number2)
    case '4':  # division
        output = int(number1) / int(number2)

# Print the result to the terminal.
prompt(f"The result is: {output}")