import os 
score =  0

#Verify if they'd like to play
answer = input("Would you like to play? ").lower()
if answer == "yes":
    os.system('cls')
    print("Sounds good, let's go!")
else:
    os.system('cls')
    print("Understandable, have a great day!")

#The Questions
answer = input("What color is the sky? ").lower()
if answer == "blue":
    print("That's correct!")
    score += 1
else:
    print("I'm sorry, that's not right. ")

answer = input("What color are bananas? ").lower()
if answer == "yellow":
    print("That's correct!")
    score += 1
else:
    print("I'm sorry, that's not right. ")

answer = input("What do fish breath? ").lower()
if answer == "water":
    print("That's correct!")
    score += 1
else:
    print("I'm sorry, that's not right. ")

answer = input("What is the opposite of 'dark'? ").lower()
if answer == "light":
    print("That's correct!")
    score += 1
else:
    print("I'm sorry, that's not right. ")

#Talley Score
os.system('cls')
print(f"That's the end, you got {score} correct!")
print(f"That's {((score / 4) * 100)}% ")
