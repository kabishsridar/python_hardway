def add(a,b):    
    print(f"\nadding {a} + {b}")
    return a + b

def subtract(a,b):    
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a,b):    
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a,b):    
    print(f"dividing {a} / {b}\n")
    return a / b
 
print("Doing some math with just the functions!")
 #now assigning math values 
age=add(10,7)
height=subtract(135,40)
weight=multiply(50,15)
iq=divide(150,2)

print(f"Age: {age}, height: {height}, weight= {weight} , iq= {iq}")

#that puzzle,now i am typing
print("\nhere is a puzzle\n")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("that becomes : ",what,"can you do it by hand?")
