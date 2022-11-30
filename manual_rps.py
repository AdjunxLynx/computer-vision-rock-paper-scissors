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
        