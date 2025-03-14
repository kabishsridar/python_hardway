from sys import exit

def black_thunder():
    print("We can play every water game here. Which one do you want to play?")
    choice = input(">")
    if choice == "anything":
        print("You can't take a decision properly, but you can enjoy yourself!")
    elif choice == "what are the games here?":
        print("There are many. Please search for those on the official website.")
    elif choice == "roller coaster":
        print("You will have a joyful ride in the roller coaster. Enjoy it!")
    else:
        print("Revisit again when you want to really enjoy.")

def wonderla_park():
    print("You can see the water games and drift games.")
    print("Enjoy the games you want.")
    choice = input(">")
    if choice == "water games":
        print("Swimming, Boomerang, Lucky Falls.be happy")
    elif choice == "land drift":
        print("Flash Tower, Equinox, Maverick. have fun")
    else:
        print("Play anything you want.")

def vac_start():
    print("You have got a vacation leave.")
    print("What idea do you have?")
    print("Which amusement park are you going to visit?")
    choice = input(">")
    if choice == "black thunder":
        black_thunder()
    elif choice == "wonderla":
        wonderla_park()
    else:
        print("Stay at home and relax.")

vac_start()
