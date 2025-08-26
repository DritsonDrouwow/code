import random
from colorama import Fore, init
init(autoreset=True)

def get_computer_choice():
    choices = ["rock",  "paper", "scissors"]
    return random.choice(choices)

def win_condition(player, computer):
    if player == computer:
        print("It's a tie!")
    elif  (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print(f"{Fore.YELLOW} You win!!! ")
    else:
        print(f"{Fore.LIGHTBLACK_EX}You lost! ")

def rock_paper_scissors():
    user_name = input("Name: ")
    print("Welcome to Rock Paper Scissors!")
    print(f"Please enter {Fore.BLACK}'rock', {Fore.WHITE}'paper', {Fore.BLUE}'scissors' {Fore.WHITE} to play and type {Fore.RED}'end' {Fore.WHITE} or {Fore.MAGENTA}'bye' {Fore.WHITE} to quit the game")

    while True:
        player_choice = input("Your choice: ").lower()

        if player_choice == "quit":
            print(f"{Fore.CYAN}Thanks for playing ")
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print(f"{Fore.RED}Invalid choice. Please choose {Fore.BLACK}'rock', {Fore.LIGHTWHITE_EX}'paper',{Fore.WHITE} or {Fore.BLUE}'scissors'.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = win_condition(player_choice, computer_choice)
        print(result)
        print()

if __name__ == "__main__":
    rock_paper_scissors()
 
