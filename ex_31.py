print("""you are in coding work with two pc
do you go with pc #1 or pc#2?""")

pc = input(">")

if pc == "1" :    
    print("now you no need to fix the code")
    print("have fun with which you choose")
    print("1. i will take r15")
    print("2.i will take royal enfield")
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
    print("it was very speed like a fraction of second")
    print("1.dell")
    print("2.asus")
    print("3.MAC")

    insanity= input (">")

    if insanity =="1"or insanity == "2":    
        print("the pc had no problem and you done the work successfully.")

        print("good job")
    else:    
        print("the pc is tough to repair but you did it")
        print("good job")

else:    
    print("you stumble around and fall on a krife and die . good job!")
