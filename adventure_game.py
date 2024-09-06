#question 1 task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Error - please input either climb a tree or cross a river.")
elif place == "cave":
    print("You find a hidden treasure!")
else:
    print("Error - please input either forest or cave.")


# question 1 task 2

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Error - please input either climb a tree or cross a river.")
elif place == "cave":
    action = input("Light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("Oh no! You are lost.")
    else:
        print("Error - please enter light a torch or proceed in the dark.")
else:
    print("Error - please input either forest or cave.")


# question 1 task 3


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("Light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("Oh no! You are lost.")
    else:
        pass
else:
    pass

