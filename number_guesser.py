#Import the "random" library
import random 

#Have player enter a number for the upper limit of the range they'll be guessing in.
top_of_range = input("Type a number: ")

#Verify that the number inputted is actually a number (.isdigit), if it is then convert the str given early into an int.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please only use positive numbers")
        quit()
else:
    print("That doesn't look like a number, please type a number next time.")
    quit()

#Generate a random number for the game.
random_number = random.randint(0, top_of_range)
guesses = 0

#Create a while loop to allow the player to continuously guess until they get it right.
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("That doesn't look like a number, please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        print(f"You got it in {guesses} guesses!")
        break
    elif user_guess > random_number:
        print("Nope! Guess lower.")
    else:
        print("Nope! Guess higher.")
