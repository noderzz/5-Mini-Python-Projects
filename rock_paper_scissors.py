import random
user_score_wins = 0
computer_score_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input('Type in: "Rock", "Paper", "Scissors" to play or "Q" to quit.').lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("That doesn't appear to be a valid option")
        continue

    random_number = random.randint(0,2)
    # rock is 0, paper is 1 and scissors is 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_score_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_score_wins += 1
    elif user_input == "scisors" and computer_pick == "paper":
        print("You won!")
        user_score_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
        continue
    else:
        print("You Lost!")
        computer_score_wins += 1


print(f"You won {user_score_wins} times!")
print(f"The computer won {computer_score_wins} times!")
print("Goodbye!")
