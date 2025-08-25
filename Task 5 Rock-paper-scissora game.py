import random

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    while True:
        user_input = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_input == 'exit':
            return None
        if user_input in choices:
            return user_input
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            print("Thanks for playing!")
            break
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()