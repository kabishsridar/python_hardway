#the end= ' ' uses to continue with the next line
print("How old are you?", end=' ')
#now commanding the input() to answer by the reader for these questions
#now assigning the input as age
age= input()
print("How tall are you?", end=' ')
#now assigning the input as height
height = input()
print("How much do you weigh?", end=' ')
#now assigning the input as weight
weight = input()

#printing using format variables.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")