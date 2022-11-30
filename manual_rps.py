import random


def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return(computer_choice)

get_computer_choice()

def get_user_choice():
    options = ["Rock", "Paper", "Scissors"]
    while True:
        choice = input("Enter 'rock', 'paper' or 'scissors' ")
        if choice in options:
            return choice
        else:
            print("Unknown input, please try again")
        
get_user_choice()
        

def get_winner(computer_choice, user_choice):
    
    computer = computer_choice
    player = user_choice
    if computer == "Rock" and player == "Scissors":
        print("You lost")
    elif computer == "Rock" and player == "Rock":
        print("It is a tie!")
    elif computer == "Rock" and player == "Paper":
        print("You won!")
    elif computer == "Paper" and player == "Scissors":
        print("You won!")
    elif computer == "Paper" and player == "Rock":
        print("You lost")
    elif computer == "Paper" and player == "Paper":
        print("It is a tie!")
    elif computer == "Scissors" and player == "Scissors":
        print("It is a tie!")
    elif computer == "Scissors" and player == "Rock":
        print("You won!")
    else:
        print("You lost")
        
def play():
