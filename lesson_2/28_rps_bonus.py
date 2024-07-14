#PY101, Lesson 2, assignment 28. 'Rock, Paper, Scissors Bonus Features

import random

CHOICES_DICT = {
    'R': 'ROCK', 
    'P': 'PAPER', 
    'L': 'LIZARD',
    'S': 'SCISSORS, SPOCK',
}

CHOICES = ', '.join(list(CHOICES_DICT.values())).split(', ')

# key defeats values
CHOICE_DEFEATS = {
    'ROCK': {'SCISSORS', 'LIZARD'},
    'PAPER': {'ROCK', 'SPOCK'},
    'SCISSORS': {'PAPER', 'LIZARD'},
    'LIZARD': {'PAPER', 'SPOCK'},
    'SPOCK': {'SCISSORS', 'ROCK'},
}

def prompt(message):
    print(f"==> {message}")

def check_validity(choice):
    if choice is None or len(choice) < 1:
        choice = get_user_choice()

    elif len(choice) == 1:
        if choice[0] == 'S':
            while choice not in CHOICES_DICT['S'].split(', '):
                prompt(f"Choose one (enter whole word): "
                       f"{CHOICES_DICT['S']}:")
                choice = input().upper().strip('" ').strip("'")
        else:
            choice = CHOICES_DICT.get(choice)

    else:
        prompt("That's not a valid choice. Try again:")
        choice = get_user_choice()

    return choice

def get_user_choice():
    prompt(f"Choose one: {', '.join(CHOICES)}")
    prompt("You may enter the first letter or the whole word.")
    choice = input().upper().strip('" ').strip("'")

    while choice not in CHOICES:
        choice = check_validity(choice)
    return choice

def determine_winner(u_choice, c_choice):
    prompt(f"You chose {u_choice}, computer chose {c_choice}")

    for win, lose in CHOICE_DEFEATS.items():
        if (u_choice == win) and (c_choice in lose):
            victor = "You win!"
        elif (c_choice == win) and (u_choice in lose):
            victor = "Computer wins!"
        else:
            victor = "It's a tie!"

    return victor

user_score = 0
computer_score = 0

def track_winners(victor):
    global user_score, computer_score

    if max(user_score, computer_score) < 5:
        if victor == "You win!":
            user_score += 1
        if victor == "Computer wins!":
            computer_score += 1

    if user_score == 5 or computer_score == 5:
        if user_score == 5:
            prompt("*** Congratulations! You won Best of 5 Matches! ***")
        elif computer_score == 5:
            prompt("*** Computer won Best of 5 Matches! ***")
        user_score = 0
        computer_score = 0

while True:

    user_choice = get_user_choice()

    computer_choice = random.choice(CHOICES)

    winner = determine_winner(user_choice, computer_choice)
    prompt(winner)
    track_winners(winner)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    while answer not in ['y', 'n', 'yes', 'no']:
        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()

    if answer[0] == 'n':
        break