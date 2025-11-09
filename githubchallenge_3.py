# Program to play game:  Stone, Paper, Scissors

import random
user_score = 0
computer_score = 0

while True:
    x=["stone","paper","scissors"]
    print(x)
    user_choice=input("Enter your choice: ")
    computer_choice = random.choice(x)

    #If user choice equals computer choice, user wins.  Else user loses
    if user_choice == computer_choice:
        print("User choice: ",user_choice,", Computer choice: ",computer_choice)
        print("Computer choice: ",computer_choice)
        print("you won!")
        user_score += 1
        print("User score:",user_score,", Computer score:",computer_score)
    else:
        print("Computer choice:",computer_choice,", user choice: ",user_choice)
        print("You didn't win. Try again!")
        computer_score += 1
        print("User score:",user_score,", Computer score:",computer_score)

    #Ask the user whether to repeat or exit the game
    repeat_game = int(input("Enter 1 to play again \n2 to exit\n"))
    if repeat_game == 1:
        continue
    if repeat_game == 2:
        break
    else:
        print("Invalid input")
        break