from sys import argv


script,user_name = argv,argv
#now assigning the prompt value
prompt='>'

#now introducing the varables to print

print(f"hi {user_name},this is the {script}script.")
print("i'd like to ask you a few questions.")
print(f"how much do you like me {user_name}")
#now we are inroducing input string to be answered by the readers 
likes = input(prompt)

print("what is your name?")
name=input(prompt)

print("where are you from ?")
place=input(prompt)

#now gathering informations from answers

print(f"""
so , now you likes me {likes}.
you are from {place}. 
and your name is {name}.
""")