import random

while True:
    User_actions = (input("input rock paper or scissors ")).lower().strip()
    Possibleactions = ["rock","paper","scissors"]
    computeraction = random.choice(Possibleactions)

    print("user chose",User_actions)
    print("computer chose",computeraction)

    if computeraction == User_actions:
        print("Both chose the same, its a tie!")
    elif computeraction == "scissors" and User_actions == "paper":
        print("Computer wins")
    elif computeraction == "scissors" and User_actions == "rock":
        print("You win!")
    elif computeraction == "paper" and User_actions == "rock":
        print("computer wins!")
    elif computeraction == "paper" and User_actions == "scissors":
            print("You win")
    elif computeraction == "rock" and User_actions == "scissors":
            print("computer win!")
    elif computeraction == "rock" and User_actions == "paper":
            print("You win!")
    play = input("do you want to play again {y|n}")
    if play != "y":
        break