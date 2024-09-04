"""PY101, Lesson 2, assignment 21. 'Mortgage / Car Loan Calculator'

Basic version that basically works.
To Do:
    - accept percent sign after apr
        - NOT DONE
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
    - consider using while True loops for some of the recursions
    - consider moving function definitions outside the main while loop
"""

import decimal
from decimal import Decimal as Dec
from sys import exit as sysexit

import json

# Translations:
with open('21_mortgage_calculator_messages.json', 'r') as file:
    MSGS = json.load(file)

def msg(message, lang):
    return MSGS[lang][message]

# Custom prompts:

def prompt(message):
    print(f"==> {message}")

def input_prompt():
    string = input("==>: ")

    # don't accept excessively long input:
    if len(string) > 16:
        prompt(msg('input_too_long', LANG))
        string = input_prompt()

    return string

# Print welcome message:
prompt("┌────────────────────────────────────────────┐")
prompt("│ Welcome to Mortgage / Car Loan Calculator! │")
prompt("└────────────────────────────────────────────┘")

languages = {
    'en': "English",
    'es': 'Español',
}

def get_language(): 
    prompt("Select a language:")
    prompt(f"  'en' ({languages['en']})")
    prompt(f"  'es' ({languages['es']})")
    language = input_prompt().strip("' ").strip('"').casefold()

    if language not in languages:
        prompt(f"Please enter 'en' or 'es'.")
        language = get_language()

    return language

LANG = get_language()

decimal.getcontext().rounding = decimal.ROUND_05UP

while True:

    def check_amount_validity(amount):
        try:
            amount = Dec(amount)
            if amount < 0:
                prompt(msg('enter_pos_num', LANG))
                amount = get_loan_amount()
            if len(str(amount % 1)) > 2:
                prompt(msg('no_fractional_cents', LANG))
                prompt(msg('enter_whole_cents', LANG))
                amount = get_loan_amount()
        except decimal.InvalidOperation:
            prompt(msg('enter_number', LANG))
            prompt(msg('may_enter_dec_commas', LANG))
            amount = get_loan_amount()
        
        return amount

    # Ask for loan amount and check input for validity:
    def get_loan_amount():

        # currency = # use UTC codes?

        prompt(msg('enter_loan_amount', LANG))
        amount = input_prompt().strip('$ ').replace(',', '').replace('_', '')

        amount = check_amount_validity(amount)

        return amount

    LOAN_AMOUNT = get_loan_amount()
    
    # This needs to be outside of this function or written differently,
    #     and this needs a Dec(rate) try/except block or something.
    # Don't accept excessively long numbers:
    def check_apr_length(rate):
        if len(str(Dec(rate) % 1)) > 6:
            prompt(msg('decimal_length', LANG))
            prompt(msg('enter_apr', LANG))
            rate = input_prompt().strip('%')
            rate = check_apr_length(rate).strip('%')

        return rate

    def check_apr_validity(rate):
        try:
            rate = check_apr_length(rate)
            rate = Dec(rate)
            # rate should be a positive number or zero:
            if rate < 0:
                prompt(msg('enter_pos_num_zero', LANG))
                rate = get_apr()
        except decimal.InvalidOperation:
            prompt(msg('enter_num_format', LANG))
            prompt(msg('apr_examples', LANG))
            rate = get_apr().strip('%')
        
        return rate

    # Ask for APR and check input for validity:
    def get_apr():
        prompt(msg('enter_apr', LANG))
        rate = input_prompt()
        rate = check_apr_validity(rate)
        return rate

    MONTHLY_RATE = get_apr() * Dec(.01) / Dec(12)

    def get_timeframe():
        prompt(msg('choose_months_years', LANG))
        prompt(msg('months_years_examples', LANG))
        timeframe = input_prompt().strip("' ").strip('"').casefold()

        if timeframe not in {'months', 'm', 'years', 'y'}:
            prompt(msg('try_again', LANG))
            timeframe = get_timeframe()

        if timeframe in {'months', 'm'}:
            timeframe = 'months'
        elif timeframe in {'years', 'y'}:
            timeframe = 'years'

        return timeframe

    def check_duration_validity(timeframe, duration):
        try:
            duration = Dec(duration)
            # don't divide by zero:
            if duration <= 0:
                prompt(msg('enter_pos_num', LANG))
                duration = get_total_duration(timeframe)
            # convert years to months:    
            if timeframe == 'years':
                duration = duration * 12
        except decimal.InvalidOperation:
            prompt(msg('enter_number', LANG))
            duration = get_total_duration(timeframe)

        return duration

    def get_total_duration(timeframe):
        prompt(msg('how_long_loan', LANG).format(timeframe=timeframe))
        duration = input_prompt()
        duration = check_duration_validity(timeframe, duration)
        return duration

    # Ask for loan duration and check inputs for validity:
    def get_loan_duration():
        timeframe = get_timeframe()
        total_duration = get_total_duration(timeframe)

        # put this in one of the supporting functions
        if total_duration > (100 * 12):
            prompt(f"Maximum loan duration is "   # figure out language support
                   "{'100 years' if timeframe == 'years' else '1200 months'}.")
            total_duration = get_total_duration(timeframe)

        return total_duration

    MONTHS_DURATION = get_loan_duration()

    def get_balloon():
        pass # return amount or False

    # balloon = get_balloon()
    # if balloon:
    #     amount -= balloon

    # Calculate monthly payment
    def calculate(amount, mpr, duration):
        payment = amount * (mpr / (1 - (1 + mpr) ** (-duration)))
        return payment

    MONTHLY_PAYMENT = calculate(LOAN_AMOUNT, MONTHLY_RATE, MONTHS_DURATION)

    # if balloon:
    #     result += balloon
        # WRONG - maybe create new variable(s), change results that are printed

    # add commas into result
    def add_comma(lst, neg_i):
        lst.insert(neg_i - 3, ',')
        neg_i = neg_i - 4

        if len(lst) > (abs(neg_i) + 3):
            lst = add_comma(lst, neg_i)

        return lst, neg_i

    # for format_currency(result) to use
    def add_commas(long_number):
        # turn into a list for processing
        digits_list = list(str(long_number))

        i = digits_list.index('.')
        neg_i = i - len(digits_list) # -3, the decimal point

        if len(digits_list) > (abs(neg_i) + 3):
            add_comma(digits_list, neg_i)

        # turn digits_list into a string to return to outer function
        commas_added = ''.join(digits_list)

        return commas_added

    # Format result
    def format_currency(result):
        # round result to even cents
        result = result.quantize(Dec("1.00"))

        if len(str(result)) > 6:
            result = add_commas(result)

        # add dollar sign into result
        return f"${result}"

    prompt(msg('results', LANG))
    
    prompt(msg('monthly_payment', LANG))
    prompt(f"{format_currency(MONTHLY_PAYMENT).rjust(36)}") 
    # variable name might change
    
    prompt(msg('total_interest', LANG))
    prompt(f"{format_currency(MONTHLY_PAYMENT * MONTHS_DURATION - LOAN_AMOUNT).rjust(36)}")

    # LINE TOO LONG ^^^

    prompt(msg('total_paid', LANG).format(MONTHS_DURATION=MONTHS_DURATION))
    
    # ^^^ .format NOT WORKING (it was working before MONTHS_DURATION change)
    
    prompt(f"{format_currency(MONTHLY_PAYMENT * MONTHS_DURATION).rjust(36)}")
    
    prompt('------------------------------------')

    prompt(msg('calculate_new_loan', LANG))
    answer = input_prompt()
    if answer not in {'y', 's'}:   # don't accept wrong language ('y' vs 's')
        sysexit(1) # make sure passing correct argument