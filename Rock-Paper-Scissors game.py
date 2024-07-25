import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print("\nRound", round_number)
        print("Your score:", user_score, "| Computer score:", computer_score)

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("\nYou chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nFinal Scores:")
            print("You:", user_score, "| Computer:", computer_score)
            if user_score > computer_score:
                print("Congratulations! You are the winner!")
            elif computer_score > user_score:
                print("Computer wins! Better luck next time.")
            else:
                print("It's a tie overall!")
            print("Thanks for playing!")
            break
        
        round_number += 1

if __name__ == "__main__":
    rock_paper_scissors_game()
