#the end= ' ' uses to continue with the next line
print("How old are you?", end=' ')
#now commanding the input() to answer by the reader for these questions
#now assigning the input as age
age= input()
print("How tall are you(cm)?", end=' ')
#now assigning the input as height
height = int(input())
print("How much do you weigh(kg)?", end=' ')
#now assigning the input as weight
weight = int(input())
h = height/100
b= h*h
BMI= weight/b
#printing using format variables.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
if BMI<16:
    print("your BMI is: ",BMI,"it is severe thickness")
elif 18.5<BMI<25:
    print("your BMI is: ",BMI," which is normal")
elif BMI>25:
    print("your BMI is: ",BMI," it is obese Try to lose your weight")
else:
    print(" ")
