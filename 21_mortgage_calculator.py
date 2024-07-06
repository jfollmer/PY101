# PY101, Lesson 2, assignment 21. 'Mortgage / Car Loan Calculator'

# Basic version that basically works.
# To Do:
    # handle long decimal places
    # Handle leftover cents after n months. Maybe use decimal module.

# Custom prompts
def prompt(message):
    print(f"==> {message}")

def input_prompt():
    string = input(f"==>: ")

    # don't accept excessively long numbers
    if len(string) > 6:
        prompt("Input is too long. Please try again:")
        string = input_prompt()

    return string

# Print welcome message
prompt("Welcome to Mortgage / Car Loan Calculator!")

# Ask for loan amount

def get_loan_amount():
    prompt("What is the total loan amount?")
    amount = input_prompt().strip('$ ')

    try:
        amount = float(amount)
        if amount < 0:
            prompt("Please enter a positive number:")
            get_loan_amount()
    except Exception:
        prompt("Please enter a number.")
        prompt("You may optionally include a decimal and/or a dollar sign:")
        get_loan_amount()

    return amount

amount = get_loan_amount()

# Ask for APR
def get_apr():
    prompt("What is the annual percentage rate (APR)?")
    apr = input_prompt()

    try:
        # calculate monthly percentage rate
        return float(apr) * .01 / 12
    except Exception:
        prompt("Please enter a number in one of the following formats:")
        prompt("Examples: 5, 5%, 5.2, 5.2%")
        get_apr()

    return apr

mpr = get_apr()

# Ask for loan duration and check inputs for validity:
def get_loan_duration():
    prompt("Would you like to enter the loan duration in months or years?")
    prompt("Enter 'months' or 'years':")
    timeframe = input_prompt().strip("' ").strip('"').casefold()

    if timeframe != 'months' and timeframe != 'years':
        print('debug', timeframe)
        prompt("Please try again. Please enter 'months' or 'years':")
        timeframe = input_prompt().strip("' ").strip('"').casefold()

    prompt(f"How many {timeframe} long is the loan?")
    duration = input_prompt()

    try:
        duration = float(duration)
        if duration <= 0:
            prompt("Please enter a positive number:")
            duration = input_prompt()
        if timeframe == 'years':
            return duration / 12
        return duration
    except Exception:
        prompt("Please enter a number. How many {timeframe} long is the loan?")
        duration = input_prompt()

duration = get_loan_duration()

# Calculate monthly payment
def calculate(amount, mpr, duration):
    payment = amount * (mpr / (1 - (1 + mpr) ** (-duration)))
    return payment

result = calculate(amount, mpr, duration)

print(result * duration)

# Format result
def format(result):
    return f"${result}"
# handle long decimal places
# handle leftover cents after n months

prompt(f"The monthly payment is: {format(result)}") # variable name might change
prompt(f"The total amount of interest is {result * duration - amount}")
