import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors'],
}
PLAYING = True

def prompt(message):
    print(f"==> {message}")

def player_wins(player_choice, comp_choice):
    return comp_choice in WINNING_COMBOS[player_choice]

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
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        player_choice = input()
    return player_choice

def prompt_play_again():
    prompt("Do you want to play again? (y/n)")
    y_or_n = input()
    while y_or_n.lower() not in ['y', 'n']:
        prompt("Enter a valid choice (y/n)")
        y_or_n = input().lower()
    return y_or_n

while PLAYING:
    choice = prompt_and_validate_input()
    computer_choice = random.choice(VALID_CHOICES)
    display_winner(choice, computer_choice)

    play_again = prompt_play_again()
    if play_again.lower() == 'n':
        PLAYING = False