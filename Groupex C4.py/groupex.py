from mods import *


gameon=True

print("Hello, welcome to play rock paper scissors, please enter your choice")

while gameon:
    user_choice = get_user_choice()
    print("You choose:", user_choice)

    if user_choice == "Exit":
        gameon = False
        print("Thanks for playing!")
        exit()

    computer_choice = get_computer_choice()
    print("computer choose:", computer_choice)
    result = get_winner(user_choice, computer_choice)
    print(result)






























