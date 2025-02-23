print("""you are in coding work with two pc
do you go with pc #1 or pc#2?""")

pc = input(">")

if pc == "1" :    
    print("there was an error ")
    print("how will you fix that")
    print("1. i have r15")
    print("2.i have royal enfield")
#now assigning the input string
    r15 = input(">")

    if r15 == "1":    
        print("this bike is amazing")
    elif r15 == "2":    
        print("this bike is on repair")
    else :    
        print((f"well,the {r15} is better"))

#now assigning elif Statement
elif pc == "2" :    
    print("it was very speed laike a fraction of second")
    print("1.dell")
    print("2.many errors")
    print("3.smooth pc")

    insanity= input (">")

    if insanity =="1"or insanity == "2":    
        print("your body survives powered by a mind jello.")

        print("good job")
    else:    
        print("the insanity roots your eyes into a pool of muck")
        print("good job")

else:    
    print("you stumble around and fall on a krife and die . good job!")
