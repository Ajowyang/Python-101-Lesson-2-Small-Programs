import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
VALID_SHORTENED_INPUTS = ['r', 'p', 'sc', 'l', 'sp']
SHORTENED_INPUT_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}
WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors'],
}
WINS = {
    'player': 0,
    'computer': 0
}

def prompt(message):
    print(f"==> {message}")

def player_wins(player_choice, comp_choice):
    return comp_choice in WINNING_COMBOS[player_choice]

def computer_wins(player_choice, comp_choice):
    return player_choice in WINNING_COMBOS[comp_choice]

def display_winner(player_choice, comp_choice):
    prompt(f"You chose {player_choice}, computer chose {comp_choice}")
    if player_wins(player_choice, comp_choice):
        prompt("You win!")
    elif player_choice == comp_choice:
        prompt("It's a tie!")
    else:
        prompt("Computer wins!")

def prompt_and_validate_input():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    player_choice = input()
    if player_choice in VALID_SHORTENED_INPUTS:
        player_choice = SHORTENED_INPUT_CHOICES[player_choice]
    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        player_choice = input()
        if player_choice in VALID_SHORTENED_INPUTS:
            player_choice = SHORTENED_INPUT_CHOICES[player_choice]
    return player_choice

def prompt_play_again():
    prompt("Do you want to play again? (y/n)")
    y_or_n = input()
    while y_or_n.lower() not in ['y', 'n']:
        prompt("Enter a valid choice (y/n)")
        y_or_n = input().lower()
    return y_or_n

def is_round_finished():
    if WINS['player'] >= 3:
        prompt("Player has won the round")
        return True
    if WINS['computer'] >= 3:
        prompt("Computer has won the round")
        return True
    return False

while True:
    choice = prompt_and_validate_input()
    computer_choice = random.choice(VALID_CHOICES)

    if player_wins(choice, computer_choice):
        WINS['player'] += 1
    elif computer_wins(choice, computer_choice):
        WINS['computer'] += 1
    display_winner(choice, computer_choice)
    prompt(f"You have {WINS['player']} wins. "
           f"Computer has {WINS['computer']} wins.")

    ROUND_FINISHED = is_round_finished()
    if ROUND_FINISHED:
        break

    play_again = prompt_play_again()
    if play_again.lower() == 'n':
        break