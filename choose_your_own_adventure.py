name = input("Type your name: ")
print(f"Welcome {name}, to this adventure!")
print("")

print("You are on a dirt road, it has come to an end and you can go left or right.")
print("")
answer = input('Which way would you like to go? Type "left" to head down the left path or "right" to head down the right path. ').lower()

if answer == "left":
    answer = input('You come to a river, you can walk around it or swim across.  Type "walk" to walk around or "swim" to swim across ')
    if answer == "swim":
        print("You tried to swim across but were unfortunately eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died of dehydration.")
    else:
        print("Not a valid option, you lose")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly.  Do you want to cross it or head back? (cross/back)?" )
    if answer == "back":
        print("You go back to the main road.  You've lost too much time in the season and can no longer make the trip. ")
    elif answer == "cross":
        answer = input("You successfully cross the bridge and meet a stranger.  Do you talk to them? (yes/no) ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold.  You win! ")
        elif answer == "no":
            print("You ignore the stranger and he stabs you in a fit of rage.  You have died. ")
        else:
            print("Not a valid option, you lose")
    else:
        print("Not a valid option, you lose")
else:
    print("Not a valid option, you lose.")

print(f"Thank you for playing {name}, have a great day!")