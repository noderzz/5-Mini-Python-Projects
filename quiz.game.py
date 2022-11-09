print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(f"You said: {playing}")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

#Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("I'm sorry, that's incorrect.")

#Question 2
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("I'm sorry, that's incorrect.")

#Question 3
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("I'm sorry, that's incorrect.")

#Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("I'm sorry, that's incorrect.")

print(f"Your total score is {score}/4")
print("That means you got " + str((score / 4) * 100) + "%")