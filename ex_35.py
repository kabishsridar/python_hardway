from sys import exit
from tracemalloc import start
# introducing def funct.
def gold_room():    
    print("this room is filled with gold . how much do you need?")

#now assigning the input 
    choice = input(">")
    if "0" in choice or "1" in choice:    
        how_much = int(choice)
    else:    
        dead("man, learn to type a number.")

    if how_much < 50:    
        print("nice you arent greedy you won!")
        exit(0)
    else:    
        dead("you greedy bastard")


def bikes_room():
    print("there are many bikes here")
    print("it is fully new modeled")
    print("the r15 bike is especially good")
    print("when we are going to a ride?")
    going_to_ride = False

    while True :    
        choice = input(">")

#the choice tells that the reader can type this or that
        if choice == "take bikes":    
            dead("the bikes are used in wheelies")
        elif choice == "good bike"and not going_to_ride:
            print("we gone to a ride")
            print("we can use it now")
            going_to_ride=True
        elif choice == "good bike "and going_to_ride:
            dead("you got accident with that bike")
        elif choice == "good bike "and going_to_ride:
            gold_room()
        else:    
            print("i got no idea what that means")

def zombie_room():    
    print("here is the great evil zombie ")
    print("he,it,whatever starts at you and go insane")
    print("do ypu flee for your life eat for your head")

    choice = input("<")

    if "zombie"in choice:    
        start()
    elif"head" in choice:    
        dead("well that was good ")
    else: zombie_room()

def dead(why):    
    print(why,"good job")
    exit(0)

def start():    
    print("you are in a dark room")
    print("there is a door to your left and right")
    print("which one will you choose")

    choice = input(">")

    if choice == "left":    
        bikes_room()
    elif choice =="left":    
        zombie_room()
    else:    
        dead("you stumble around the room until you starve")

start()    