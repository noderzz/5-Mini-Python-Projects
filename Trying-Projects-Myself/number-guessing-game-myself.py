import random
import os

verify=""
score =0

os.system("cls")
answer = input("Would you like to play? ")
if answer == "yes":
    os.system("cls")
    print("Awesome, let's get started!")
else:
    os.system('cls')
    print("No problem, you have a nice day.")
    quit()

while True:
    upper_range = input("Choose a number to be the upper range of what possible number you're going to guess.")
    if upper_range.isdigit():
        upper_range = int(upper_range)
        print("Input Accepted!")
        break
    else:
        print("That doesn't appear to be a number, please try again.")
        continue

print("")
random_number = random.randrange(upper_range)
print("Random Number Generated.")
print("")
print(f"Please enter a guess between 0 and {upper_range}")

while True: 
    guess = int(input("My guess: "))
    if guess > random_number:
        print("Nope, guess lower! ")
        score += 1
    elif guess < random_number:
        print("Nope, guess higher!")
        score +=1
    else:
        score +=1
        print("That's right, you got it!")
        print(f"You got it in {score} guesses!")
        break