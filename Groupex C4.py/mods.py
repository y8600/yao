#groupex rock paper Scissors
def get_user_choice():
    userinput= input("please enter your choice (Rock, Paper, Scissors, Exit):")
    if userinput in ["Rock", "Paper", "Scissors", "Exit"]:
        return userinput
    else:
        return "Invalid choice. please enter rock, paper, scissors, or Exit."
   
def get_computer_choice():
    import random
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if get_user_choice == get_computer_choice:
        return "it's a tie!"
    elif get_user_choice == "Rock" and get_computer_choice == "Scissors":
        return "You win!"
    elif get_user_choice == "Paper" and get_computer_choice == "Rock":
        return "You win!"
    elif get_user_choice == "Scissors" and get_computer_choice == "Paper":
        return "You win!"
    else:
        return "computer wins!"
