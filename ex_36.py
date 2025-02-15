from sys import exit
from tracemalloc import start

def black_thunder():
    print("we can play every water games here.which one you want to play?")
    choice = input(">")
    if choice == "anything":
        print("you can't take a decision properly but you can enjoy yourself")
    elif choice == "what are the games are here?":
        print("there are many , you please search those in the official website")
    elif choice == "roller coaster":
        print("you will have a joyfull ride in the rller coaster, enjoy it")
    else:
        print("you revisit again when you want to really enjoy") 

def wonderla_park():
    print("you can see the watergames also the drift games")
    print("enjoy the games whatever you need")
    choice = input(">")
    if choice == "what are the watergames avalable here?" :
        print("swimming ,boomerang , lucky falls")
    elif choice == "what are the land drift game?":
        print("flash tower,equinox , maverick")
    else:
        print("play anything you want")

def vac_start():
    print("you have got a vaccational leave")
    print("what idea you have?")
    print("which amusement park you are going to move?")
    choice = input(">")
    if choice ==" black thunder":
        black_thunder()
    elif choice == "wonderla":
        wonderla_park()
    else :
       print(" stay in your home")

vac_start()
