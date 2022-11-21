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
if answer == "cross":
    os.system("cls")
    print("You swim across the river, fighting the current and losing stamina.  You're able to make it across but now you're tired.")
    print("Do you take a rest or continue onward? (rest/continue)")
    answer = input("My answer: ").lower()
    if answer == "rest":
        os.system("cls")
        print("You decide to stop and rest but while you sleep a pack of wolves surrounds you and eats you in your sleep.")
        print("Unfortunately you have died")
    elif answer == "continue":
        os.system("cls")
        print("You walk for a while but collapse due to the exhaustion.  While collapsed a hungry bear finds you and eats you for dinner.")
        print("Unfortunately you have died")
    else:
        print("That doesn't seem to be a valid input.  You lose.")
        quit()
elif answer == "around":
    os.system("cls")
    print("You spend hours looking for a way around, it's gotten dark and you're unable to see where you are.")
    print("Do you make camp or try to find your way back? (camp/back) ")
    answer = input("My answer: ").lower()
    if answer == "camp":
        os.system("cls")
        print("You make camp, sit down by your fire and hear a noise.  Do you investigate the noise? (yes/no)")
        answer = input("My answer: ").lower()
        if answer == "yes":
            os.system("cls")
            print("You investigate the noise and find a couple rats standing on a treasure chest.  You open the chest and it looks to be the treasure!")
            print("YOU'VE WON!")
            pass
        elif answer == "no":
            os.system("back")
            print("You ignore the sound until you no longer hear it.  After a while a meteor hits the camp and ends up killing you.")
            print("If only you'd moved away from camp.")
            print("Unfortunately you have died")
        else:
            print("That doesn't seem to be a valid input.  You lose.")
            quit()
    elif answer == "continue":
        os.system("back")
        print("You try to head back but get lost in the dark.  Aliens abduct you in the night and you're never seen again.")
        print("Unfortunately you have died")
    else:
        print("That doesn't seem to be a valid input.  You lose.")
        quit()
else:
    print("That doesn't seem to be a valid input.  You lose.")
    quit()

print("THE END")