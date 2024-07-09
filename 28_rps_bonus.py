"""PY101, Lesson 2, assignment 28. 'Rock, Paper, Scissors Bonus Features

To Do:
    - handle empty strings input
    - get_user_choice and check_validity logic is too convoluted, simplify
"""

import random

CHOICES_DICT = {
    'r': 'Rock', 
    'p': 'Paper', 
    'l': 'Lizard',
    's': 'Scissors, Spock',
}

CHOICES = ', '.join([ value for value in CHOICES_DICT.values() ]).split(', ')

# key defeats values
CHOICE_DEFEATS = {
    'Rock': {'Scissors', 'Lizard'},
    'Paper': {'Rock', 'Spock'},
    'Scissors': {'Paper', 'Lizard'},
    'Lizard': {'Paper', 'Spock'},
    'Spock': {'Scissors', 'Rock'},
}

def prompt(message):
    print(f"==> {message}")

def check_validity(user_choice):
    try:
        user_choice = CHOICES_DICT.get(user_choice)
        while user_choice not in CHOICES:
            prompt("That's not a valid choice. Try again:")
            user_choice = CHOICES_DICT.get(input()[0])
    except IndexError:
        check_validity(user_choice)

    return user_choice

def get_user_choice():
    prompt(f"Choose one: {CHOICES}")
    prompt("You may enter the first letter or the whole word.")
    user_choice = input()[0].lower() # index error with empty strings

    if user_choice[0] == 's':
        while user_choice not in CHOICES_DICT['s'].split(', '):
            prompt(f"Choose one (enter whole word): "
                f"{CHOICES_DICT['s']:}")
            user_choice = input().lower().capitalize()
    else:
        user_choice = CHOICES_DICT.get(user_choice)
    # check_validity(user_choice)

    return user_choice

def determine_winner(user_choice, computer_choice):
    """Defining this up here improves readability/maintainability. 
    Encapsulates logic, allows you to limit your focus to work on this
    specific piece of the puzzle.
    """
    prompt(f"You chose {user_choice}, computer chose {computer_choice}")

    for key, values in CHOICE_DEFEATS.items():
        if (user_choice == key) and (computer_choice in values):
            return "You win!"
        elif (computer_choice == key) and (user_choice in values):
            return "Computer wins!"
    return "It's a tie!"

while True:

    user_choice = get_user_choice()

    computer_choice = random.choice(CHOICES)

    prompt(determine_winner(user_choice, computer_choice))

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    
    while answer not in ['y', 'n']:
        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()

    if answer[0] == 'n':
        break