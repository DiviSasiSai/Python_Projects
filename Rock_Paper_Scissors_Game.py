import random

game = ["rock","paper","scissors"]

while True:
    choice = input("Your Choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(game)
    if choice == "paper" and computer_choice == "rock":
        print("You are win..")
    elif choice == "scissors" and computer_choice == "paper":
        print("You are win..")
    elif choice == "rock" and computer_choice == "scissors":
        print("You are win..")
    else:
        print("You are lose..")
    if input("Are you continue? (y/n)").lower() == "y":
        continue
    print("Thank you for playing")
    break

