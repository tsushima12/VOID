import random


while True:
    choices = ["rock","paper","scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissor?: ").lower()


    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie! ")

    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "scissor":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")


    elif player == "paper":
        if computer == "scissor":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")


    elif player == "scissor":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")