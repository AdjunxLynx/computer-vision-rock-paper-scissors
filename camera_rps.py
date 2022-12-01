import cv2
from keras.models import load_model
import numpy as np
import time
import random
import matplotlib.pyplot as plt


def get_winner(computer_choice, user_choice):
    
    computer = computer_choice
    player = user_choice
    print("Computer Chose " + str(computer))
    if computer == "Rock" and player == "Scissors":
        return "You lost"
    elif computer == "Rock" and player == "Rock":
        return "It is a tie!"
    elif computer == "Rock" and player == "Paper":
        return "You won!"
    elif computer == "Paper" and player == "Scissors":
        return "You won!"
    elif computer == "Paper" and player == "Rock":
        return "You lost"
    elif computer == "Paper" and player == "Paper":
        return "It is a tie!"
    elif computer == "Scissors" and player == "Scissors":
        return "It is a tie!"
    elif computer == "Scissors" and player == "Rock":
        return "You won!"
    else:
        return "You lost"


def get_prediction(model, cap):
 
    
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    before = time.time()
    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('Rock, Papers, Scissors', frame)
        # Press q to close the window
        if time.time() - before >= 3:
            options = ["Rock", "Paper", "Scissors", "Nothing"]
            index = np.argmax(prediction)
            index.astype(int)

            print(str(options[index]) + " Predicted")
            return (options[index])
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            quit()

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return(computer_choice)

def play():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    rounds_played = 0
    computer_wins=0
    user_wins=0
    options = ["Rock", "Paper", "Scissors", "Nothing"]
    
    while True:
        
        computer_choice = get_computer_choice()
        while True:
            user_choice = get_prediction(model, cap)
            if user_choice != "Nothing":
                break
            else:
                pass
                
            
        winner = get_winner(computer_choice, user_choice)
        if winner == "You lost":
            rounds_played += 1
            computer_wins += 1
        elif winner == "You won!":
            rounds_played += 1
            user_wins += 1
 
        else:
            rounds_played += 1
        print("The Computer has won " +str(computer_wins)+ " times and you have won " + str(user_wins) + " times so far")
        print(str(rounds_played) + " Games played so far")
        waste_time()
            
        
        if computer_wins == 3:
            print("Computer won best of 3")
            break
        elif user_wins == 3:
            print("You won best of 3")
            break
        else:
            print("5 Games played")

def waste_time():
    before = time.time()
    print("Press C To Continue")
    while True:
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            quit()

play()
