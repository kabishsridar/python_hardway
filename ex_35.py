from sys import exit
from tracemalloc import start

# Defining the functions
def gold_room():
    print("This room is filled with gold. How much do you need(in numbers)?")
    
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man,type a number.")

    if how_much < 50:
        print("Nice, you aren't greedy! You won!")
        exit(0)
    else:
        dead("You greedy person!")


def bikes_room():
    print("There are many bikes here.")
    print("It is fully new modeled.")
    print("The R15 bike is especially good.")
    print("When are we going for a ride?")
    going_to_ride = False

    while True:
        choice = input("> ")

        if choice == "now":
            print("The bikes are used in wheelies. Feel free to use them!")
            gold_room()
        elif choice == "not now" and not going_to_ride:
            print("We've gone for a ride.")
            print("We can use it now.")
            going_to_ride = True
        elif choice == "ride" and going_to_ride:
            print("Great! We're going for a ride.")
            gold_room()
        elif choice == "good bike" and going_to_ride:
            dead("You got into an accident with that bike.")
        else:
            print("I have no idea what that means. Try again.")

def zombie_room():
    print("Here is the great evil zombie.")
    print("It starts at you and goes insane.")
    print("Do you flee for your life or fight for your head?")

    choice = input("<")

    if "zombie" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was good.")
    else:
        zombie_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your left and right.")
    print("Which one will you choose?")

    choice = input(">")

    if choice == "left":
        bikes_room()
    elif choice == "right":
        zombie_room()
    else:
        gold_room

start()
