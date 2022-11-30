import random


def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return(computer_choice)

get_computer_choice()

def get_user_choice():
    options = ["rock", "paper", "scissors"]
    while True:
        choice = input("Enter 'rock', 'paper' or 'scissors' ")
        choice.lower()
        if choice in options:
            return choice
        else:
            print("Unknown input, please try again")
        
get_user_choice()
        