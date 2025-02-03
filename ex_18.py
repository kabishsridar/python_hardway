#now defing the function args
def print_two(*args):    
    arg1,arg2 = args
    print(f"arg1: {arg1},arg2:{arg2}")

def print_two_again(arg1,arg2):    
    print(f"arg1: {arg1}, arg2: {arg2}")

#this one is with the arguement

def print_one(arg1):    
    print(f"arg1:{arg1}")

#this one is without the arguement

def print_none():    
    print("i got nothing'.")


#now it considers as kabsih is argv1 and kamal is argv2

print_two("kabish","kamal")
print_two_again("kabish","kamal")
print_one("first!")
print_none()
