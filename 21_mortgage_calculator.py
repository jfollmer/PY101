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
        DONE but do this in a different way, str.format() maybe. Given
             solution uses f"{payment:2f}"
    - handle balloon loans
    - run through pylint
        DONE but do again if you change anything
    - International support:
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

        # don't accept excessively long input:
        if len(string) > 16:
            prompt("Input is too long. Please try again:")
            string = input_prompt()

        return string

    # Print welcome message:
    prompt("|--------------------------------------------|")
    prompt("| Welcome to Mortgage / Car Loan Calculator! |")
    prompt("|--------------------------------------------|")

    # Ask for loan amount and check input for validity:
    def get_loan_amount():

        # currency = # use UTC codes

        prompt("What is the total loan amount?")
        amount = input_prompt().strip('$ ').replace(',', '').replace('_', '')

        try:
            amount = Dec(amount)
            if amount < 0:
                prompt("Please enter a positive number:")
                amount = get_loan_amount()
            if len(str(amount % 1)) > 2:
                prompt("Fractional cents not accepted.")
                prompt("Please enter whole cents. Example: 4999.99:")
                amount = get_loan_amount()
        except decimal.InvalidOperation:
            prompt("Please enter a number.")
            prompt("You may optionally include a decimal and commas.")
            amount = get_loan_amount()

        return amount

    loan_amount = get_loan_amount()

    # Ask for APR and check input for validity:
    def get_apr_to_mpr():
        prompt("What is the annual percentage rate (APR)?")
        rate = input_prompt()
        
        # This needs to be outside of this function or written differently,
            # and this needs a Dec(rate) try/except block or something.
        # Don't accept excessively long numbers:
        # def check_rate_length(rate):
        #     if len(float(rate) % 1) > 3:
        #         prompt("Please try again. Decimals should be less than "
        #                " 3 digits.")
        #         prompt("What is the annual percentage rate (APR)?")
        #         rate = input_prompt()
        #         rate = check_rate_length()
        #         return rate
        # rate = check_length(rate)

        try:
            rate = Dec(rate)
            # rate should be a positive number or zero:
            if rate < 0:
                prompt("Please enter a positive number or zero.")
                rate = get_apr()
        except decimal.InvalidOperation:
            prompt("Please enter a number in one of the following formats:")
            prompt("Examples: 6, 6%, 5.9, 5.9%, 5.99, 5.99%")
            rate = get_apr()

        # return monthly percentage rate instead of APR:
        return rate

    monthly_rate = get_apr() * Dec(.01) / Dec(12)

    # Ask for loan duration and check inputs for validity:
    def get_loan_duration():

        def get_timeframe():
            prompt("Would you like to enter the loan duration in months or "
                   "years?")
            prompt("Enter 'm' for 'months' or 'y' for 'years':")
            timeframe = input_prompt().strip("' ").strip('"').casefold()

            if timeframe not in {'months', 'm', 'years', 'y'}:
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
                    prompt("Please enter a positive number.")
                    duration = get_duration()
                if timeframe == 'years':
                    duration = duration * 12
                return duration
            except decimal.InvalidOperation:
                prompt("Please enter a number.")
                duration = get_duration()
                return duration

        if duration > (100 * 12):
            prompt(f"Maximum loan duration is "
                   "{'100 years' if timeframe == 'years' else '1200 months'}.")
            duration = get_duration()

    duration_months = get_loan_duration()

    def get_balloon():
        pass # return amount or False

    # balloon = get_balloon()
    # if balloon:
    #     amount -= balloon

    # Calculate monthly payment
    def calculate(amount, mpr, duration):
        payment = amount * (mpr / (1 - (1 + mpr) ** (-duration)))
        return payment

    monthly_payment = calculate(loan_amount, monthly_rate, duration_months)

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
    prompt(f"{format_result(monthly_payment)}") # variable name might change
    prompt("Total interest:")
    prompt(f"{format_result(monthly_payment * duration_months - loan_amount)}")
    prompt(f"Total of {duration_months} payments:")
    prompt(f"{format_result(monthly_payment * duration_months)}")

    prompt("Would you like to calculate a new loan? (y/n)")
    answer = input_prompt()
    if answer != 'y':
        sysexit(1) # make sure passing correct argument