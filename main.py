import random

print("Welcome to Rock, Paper, Scissors!")
print("In this game, Rock crushes Scissors, Scissors cuts Paper, and Paper covers Rock.")
print("To win the game, be the first to win two rounds.")

choices = ["Rock", "Paper", "Scissors"]

def rock_paper_scissors_EZGI_KARA():

    while True:
        player_score = 0
        computer_score = 0

        while player_score < 2 and computer_score < 2:

            print(f"Current Score - Player: {player_score}, Computer: {computer_score}")
            player_choice = input("Choice Rock, Paper, or Scissors: ").capitalize()

            if player_choice not in choices:
                print("Invalid choice! Please choose 'Rock', 'Paper', or 'Scissors'.")
                continue

            computer_choice = random.choice(choices)
            print(f"Computer selected: {computer_choice.capitalize()}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "paper") or \
                    (player_choice == "paper" and computer_choice == "scissors") or \
                    (player_choice == "scissors" and computer_choice == "rock"):
                print("Computer wins this round!")
                computer_score += 1
            else:
                print("You win this round!")
                player_score += 1

        if player_score == 2:
            print("Congratulations! You won the game!")
        else:
            print("The computer won the game. Better luck next time!")

        play_again = input("Would you like to play another game? (Yes/No): ").capitalize()
        if play_again != 'Yes':
            print("Thank you for playing. Goodbye!")
            break

rock_paper_scissors_EZGI_KARA()
