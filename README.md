# Computer Vision RPS

#MILESTONE 1

using googles teachable machine, i have created an ML model for my computer to detect the difference between rock, paper and scissors
this will be used later on to create a live RPS game where i can use my camera to input my choice instead of using a CLI or GUI
this model can then be exported as a .h5 file and .txt to allow python to manage and use the model created

#MILESTONE 2
I have downloaded my model from the goog teachable machine website. this included the labels.txt that contained the four different options. rock, paper, scissors or no readable data.
i have then used a program to quickly test my model if it works


#MILESTONE 3
I installed all the dependecies using conda and created a virtual environment to keep all modules seperate from my base python. i installed pip (which is a python module manager) and the using that i installed the rest of the dependencies
such as ipykernel, tensorflow( for the model predictions) and opencv-python for the computer vision aspect. I also used Numpy however this is already installed with python so didnt install uysing conda/pip


#MILESTONE 4
I created 4 functions. get_computer_choice() is used to return a random choice of the game RPS. it uses the random module to select a random choice from a list of "rock" "paper" "scissors"
get_user_choice() is used to return a choice that the user wants to iunput. i used a while loop to use data filtering so that the data type is the correct type for later functions. if the input is in the list of options:"rock, paper or scissors" otherwise it throws an error and tries again untill correct input is detected.
i then created the get_winner() function that uses alot of if, elifs and elses to use logic and find out who wins from the current inputs of the aforementioned functions.
finally, i created a play() function to wrap all my other functions in and create the final logic of my game


MILESTONE 5
i combined all my functions into a single function called play(). i also created an extra function called waste_time() so that i could allow the user to see the results of a single round instead of the game continuing without telling the user (or letting them see)
i finally updated my final logic to ensure the user could play the game in their own time by waiting for a "q" or "c" (for continue). i changed what "q" would do, so instead of breaking from the main loop, it quit the entire python program so i didnt have to alos quit the outer loop after the first loop.
i also ensured the player got updated with all data needed, including total games played, user wins and computer wins 

<img width="476" alt="image" src="https://user-images.githubusercontent.com/117390288/205148073-5a9158d1-a3dd-4dab-945c-0851dee829ab.png">

