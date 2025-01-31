import random

VALID_CHOICES = ['rock', 'paper', 'scissors']
PLAYING_AGAIN = True

def prompt(message):
    print(f"==> {message}")

def display_winner(player_choice, comp_choice):
    prompt(f"You chose {player_choice}, computer chose {comp_choice}")
    if ((player_choice == "rock" and comp_choice == "scissors") or
        (player_choice == "paper" and comp_choice == "rock") or
        (player_choice == "scissor" and comp_choice == "paper")):
        prompt("You win!")
    elif ((player_choice == "rock" and comp_choice == "paper") or
        (player_choice == "paper" and comp_choice == "scissors") or
        (player_choice == "scissors" and comp_choice == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while PLAYING_AGAIN:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    prompt("Do you want to play again? (y/n)")
    play_again = input()

    while play_again.lower() not in ['y', 'n']:
        prompt("Enter a valid choice (y/n)")
        play_again = input().lower()

    if play_again.lower() == 'n':
        PLAYING_AGAIN = False