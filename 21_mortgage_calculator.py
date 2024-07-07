"""PY101, Lesson 2, assignment 21. 'Mortgage / Car Loan Calculator'

Basic version that basically works.
To Do:
    - Handle leftover fractional cents after n months. Maybe use decimal 
      module.
        DONE
    - handle long decimal places
        DONE
    - Compare results with official mortgage calculator. Fix the math. 
      Something broke when you fixed something else.
        DONE
    - accept commas in numbers
        DONE
    - add commas back into results
        DONE but do this in a different way, str.format() maybe
    - handle balloon loans
    - run through pylint
    International support:
        - language support
        - accept commas as decimal points and periods as denomination
          separators
        - accept alternate currency symbols
"""

import decimal
from decimal import Decimal as Dec
from sys import exit as sysexit

decimal.getcontext().rounding = decimal.ROUND_05UP

while True:

    # Custom prompts
    def prompt(message):
        print(f"==> {message}")

    def input_prompt():
        string = input("==>: ")

        # don't accept excessively long numbers
        if len(string) > 15:
            prompt("Input is too long. Please try again:")
            string = input_prompt()

        return string

    # Print welcome message
    prompt("Welcome to Mortgage / Car Loan Calculator!")

    # Ask for loan amount
    def get_loan_amount():

        # currency = # use UTC codes

        prompt("What is the total loan amount?")
        amount = input_prompt().strip('$ ').replace(',', '').replace('_', '')

        try:
            amount = Dec(amount)
            if amount < 0:
                prompt("Please enter a positive number:")
                get_loan_amount()
        except decimal.InvalidOperation:
            prompt("Please enter a number.")
            prompt("You may optionally include a decimal and commas.")
            get_loan_amount()

        return amount

    amount = get_loan_amount()

    # Ask for APR
    def get_apr():
        prompt("What is the annual percentage rate (APR)?")
        apr = input_prompt()

        try:
            # calculate monthly percentage rate
            return Dec(apr) * Dec(.01) / Dec(12)
        except decimal.InvalidOperation:
            prompt("Please enter a number in one of the following formats:")
            prompt("Examples: 5, 5%, 5.2, 5.2%")
            get_apr()

        return apr

    mpr = get_apr()

    # Ask for loan duration and check inputs for validity:
    def get_loan_duration():

        def get_timeframe():
            prompt("Would you like to enter the loan duration in months or "
                   "years?")
            prompt("Enter 'months' or 'years':")
            timeframe = input_prompt().strip("' ").strip('"').casefold()

            if timeframe not in {'months', 'years'}:
                prompt("Please try again.")
                return get_timeframe()
            return timeframe

        timeframe = get_timeframe()

        def get_duration():
            prompt(f"How many {timeframe} long is the loan?")
            duration = input_prompt()

            try:
                duration = Dec(duration)
                # don't divide by zero:
                if duration <= 0:
                    prompt("Please enter a positive number:")
                    duration = get_duration()
                return duration
            except decimal.InvalidOperation:
                prompt("Please enter a number.")
                duration = get_duration()
                return duration

        if timeframe == 'years':
            return get_duration() * 12
        return get_duration()

    duration = get_loan_duration()

    def get_balloon():
        pass # return amount or False

    # balloon = get_balloon()
    # if balloon:
    #     amount -= balloon

    # Calculate monthly payment
    def calculate(amount, mpr, duration):
        payment = amount * (mpr / (1 - (1 + mpr) ** (-duration)))
        return payment

    result = calculate(amount, mpr, duration)

    # if balloon:
    #     result += balloon
        # WRONG - maybe create new variable(s), change results that are printed

    # for format_result(result) to use
    def add_commas(long_number):
        # turn into a list for processing
        digits_list = list(str(long_number))

        i = digits_list.index('.')
        neg_i = i - len(digits_list) # -3, the decimal point

        # add commas into result
        def add_comma(lst, neg_i):
            lst.insert(neg_i - 3, ',')
            neg_i = neg_i - 4

            if len(lst) > (abs(neg_i) + 3):
                lst = add_comma(lst, neg_i)

            return lst, neg_i

        if len(digits_list) > (abs(neg_i) + 3):
            add_comma(digits_list, neg_i)

        # turn digits_list into a string to return to outer function
        commas_added = ''.join(digits_list)

        return commas_added

    # Format result
    def format_result(result):
        # round result to even cents
        result = result.quantize(Dec("1.00"))

        if len(str(result)) > 6:
            result = add_commas(result)

        # add dollar sign into result
        return f"${result}"

    prompt("Monthly payment:")
    prompt(f"{format_result(result)}") # variable name might change
    prompt("Total interest:")
    prompt(f"{format_result(result * duration - amount)}")
    prompt(f"Total of {duration} payments:")
    prompt(f"{format_result(result * duration)}")

    prompt("Would you like to calculate a new loan? (y/n)")
    answer = input_prompt()
    if answer != 'y':
        sysexit(1) # make sure passing correct argument