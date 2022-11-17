import random
import os

choices = ["rock", "paper", "scissors"]
computer_wins = 0
player_wins = 0
ties = 0

os.system("cls")
answer = input("Would you like to play? ").lower()

if answer == "yes":
    print("Sweet, let's go!")
else:
    print("That's cool, have a nice day!")
    quit()

print("")
while True:
    random_number = random.randint(0,2)
    print('Please choose "rock", "paper" or "scissors".')
    print('Input "q" at any time to quit.')
    answer = input("My answer: ").lower()
    if choices[random_number] == "rock" and answer == "paper":
        print(f"Computer chose {choices[random_number]}")
        print("You won!")
        player_wins += 1
    elif choices[random_number] == "paper" and answer == "scissors":
        print(f"Computer chose {choices[random_number]}")
        print("You won!")
        player_wins += 1
    elif choices[random_number] == "scissors" and answer == "rock":
        print(f"Computer chose {choices[random_number]}")
        print("You won!")
        player_wins += 1
    elif choices[random_number] == answer:
        print(f"Computer chose {choices[random_number]}")
        print("It was a tie!!")
        ties += 1
    elif answer == "q":
        break
    elif answer not in choices:
        print("Sorry, that doesn't appear to be a valid input.")
        continue
    else:
        print(f"Computer chose {choices[random_number]}")
        print("Looks like you lose!")
        computer_wins += 1

os.system("cls")
print("Final score was:")
print(f"Player wins {player_wins}")
print(f"Computer wins {computer_wins}")
print(f"Draws {ties}")
print("")
print("Thanks for playing!")