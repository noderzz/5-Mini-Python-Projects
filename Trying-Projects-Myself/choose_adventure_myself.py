import os
os.system("cls")

print("Would you like to play?")
answer = input("My answer: ").lower()

if answer == "yes" or answer == "y":
    print("Great!  Let's get started!")
else:
    print("No problem, come back when you're ready!")

print("What is your characters name? ")
character_name = input("My name: ")

os.system("cls")
print(f"{character_name} grew up in a small town.  One day, {character_name} heard a story of a small fortune nearby.")
print(f"One morning {character_name} left town and set off to find the treasure.")
print("")
print("You come to a river and need to get to the other side.  Do you cross the river or look for a way around it? (cross/around)")
answer = input("My answer: ").lower()
while True:
    if answer == "cross":
        os.system("cls")
        print("You swim across the river, fighting the current and losing stamina.  You're able to make it across but now you're tired.")
        print("Do you take a rest or continue onward? (rest/continue)")
        answer = input("My answer: ").lower()
    elif answer == "around":
        os.system("cls")
        print("You spend hours looking for a way around, it's gotten dark and you're unable to see where you are.")
        print("Do you make camp or try to find your way back? (camp/back) ")
        answer = input("My answer: ").lower()
    else:
        print("That doesn't seem to be a valid input.  Please try again.")
        continue