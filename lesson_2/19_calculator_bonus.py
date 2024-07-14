# PY101, Lesson 2, assignment 19. 'Calculator Bonus Features':

import json

LANGUAGE = 'es' # change to 'en' for English or 'es' for Spanish

# Load the messages from the JSON file
with open('19_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)
# Now 'MESSAGES' contains the loaded messages as a Python dictionary

# Support multiple languages
# (change LANGUAGE = 'en' to 'es' at the top of the program for Spanish)
def messages(message, lang='en'):
    return MESSAGES[lang][message]

while True:

    # Create a distinctive prompt:
    def prompt(message):
        print(f"==> {message}")

    prompt(messages('welcome', LANGUAGE))

    # Function to check validity of number inputs:
    def invalid_number(number_str):
        try:
            float(number_str)
        except ValueError:
            return True
        return False

    # Ask the user for the first number.
    prompt(messages('number_prompt_1', LANGUAGE))
    number1 = input()

    # Check validity of number1 input:
    while invalid_number(number1):
        prompt(messages('invalid_number', LANGUAGE))
        number1 = input()

    # Ask the user for the second number.
    prompt(messages('number_prompt_2', LANGUAGE))
    number2 = input()

    # Check validity of number2 input:
    while invalid_number(number2):
        prompt(messages('invalid_number', LANGUAGE))
        number2 = input()

    # Ask the user for an operation to perform.
    prompt(messages('operation_prompt', LANGUAGE))
    operation = input()

    # Check validity of operation input:
    while operation not in ['1', '2', '3', '4']:
        prompt(messages('invalid_operation', LANGUAGE))
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1':    # addition
            output = float(number1) + float(number2)
        case '2':  # subtraction
            output = float(number1) - float(number2)
        case '3':  # multiplication
            output = float(number1) * float(number2)
        case '4':  # division
            if float(number2) == 0:
                prompt(messages('division_by_zero', LANGUAGE))
                exit(1)
            output = float(number1) / float(number2)

    # Print the result to the terminal.
    prompt(messages('result', LANGUAGE).format(output=output))

    # Ask the user if they would like to perform another calculation
    prompt(messages('another_operation', LANGUAGE))
    answer = input()
    if answer and answer[0].lower() != 'y':
        break