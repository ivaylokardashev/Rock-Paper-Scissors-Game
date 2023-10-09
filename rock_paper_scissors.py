import random
import os
import time


GAME_CHOICES = ("rock", "paper", "scissors")
your_wins = 0
computer_wins = 0

while True:
    print(
        ".---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------.\n"
        "|  .________.  ._______.  .______.  .__.  .__.       ._________.      ____       ._________.  ._______.  .________.         .__________.  .______.  ._________.  .__________.  .__________.  ._______.  .________.  .__________.  |\n"
        "|  |  .___. |  | .___. |  |  ____|  |  | /  /        |  .____. |     / /\ \      |  .____. |  | ._____|  |  .___. |         |  ._______|  |  ____|  |__.   .__|  |  ._______|  |  ._______|  | .___. |  |  .___. |  |  ._______|  |\n"
        "|  |  |   | |  | |   | |  |  |      |  |/  /  .___.  |  |    | |    / /  \ \     |  |    | |  | |_____.  |  |   | |  .___.  |  |_______.  |  |         |   |     |  |_______.  |  |_______.  | |   | |  |  |   | |  |  |_______.  |\n"
        "|  |  |___|_|  | |   | |  |  |      |     /   |___|  |  |____|_|   / /____\ \    |  |____|_|  |  _____|  |  |___|_|  |___|  |________. |  |  |         |   |     |________. |  |________. |  | |   | |  |  |___|_|  |________. |  |\n"
        "|  |  | \  \   | |___| |  |  |___.  |  |\  \         |  |         / /------\ \   |  |         |  |____.  |  | \  \          .________| |  |  |___.  .__|   |__.  .________| |  .________| |  | |___| |  |  | \  \   .________| |  |\n"
        "|  |__|  \__\  |_______|  |______|  |__| \__\        |__|        /_/        \_\  |__|         |_______|  |__|  \__\         |__________|  |______|  |_________|  |__________|  |__________|  |_______|  |__|  \__\  |__________|  |\n"
        "|_________________________________________________________________________________________________________________________________________________________________________________________________________________________________|\n")
    print("Your commands: [R] -> Rock, [P] -> Paper, [S] -> Scissors")
    print("Turn on your [CAPS LOCK] button for fast typing of the commands ;)")
    print("")

    computer_choice = random.choice(GAME_CHOICES)
    your_choice = input("Your turn: ")

    if your_choice == "R":
        your_choice = "rock"
    elif your_choice == "S":
        your_choice = "scissors"
    elif your_choice == "P":
        your_choice = "paper"
    else:
        print(f"Incorrect input you can chose only [R], [P] or [S] but you chose [{your_choice}]!")
        print("You will chose again after 10 seconds.")
        time.sleep(10)
        continue

    if (your_choice == "rock" and computer_choice == "scissors") or \
            (your_choice == "scissors" and computer_choice == "paper") or \
            (your_choice == "paper" and computer_choice == "rock"):
        print(f"You win!\nYou chose rock and computer chose {computer_choice}")
        your_wins += 1
    elif your_choice == computer_choice:
        print(f"Draw")
    else:
        print(f"You lose.\nYou chose rock and computer chose {computer_choice}")
        computer_wins += 1

    games = input("Do you want to continue pres [Y] for yes and [N] for no.")

    if games == 'Y':
        os.system('cls')
    elif games == 'N':
        print()
        print(f"Your wins: [{your_wins}]\tComputer wins: [{computer_wins}]")
        print()

        if your_wins > computer_wins:
            print(f"Congratulation you beat the computer :)")
        elif your_wins < computer_wins:
            print(f"Sorry but computer beat you :(")
        else:
            print(f"You and computer have same score :|")

        break
    else:
        print("You enter wrong command! And for this you will play one more game ;)")
        time.sleep(5)
        os.system('cls')


