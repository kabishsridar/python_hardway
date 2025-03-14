from sys import argv

# Unpacking argv into variables
script, user_name = argv

# Assigning the prompt value
prompt = '> '

# Introducing the variables to print
print(f"Hi {user_name}, this is the {script} script.")
print("I'd like to ask you a few questions.")
print(f"How much do you like me, {user_name}?")

# Introducing input string to be answered by the readers
likes = input(prompt)
print("Where are you from?")
place = input(prompt)

# Gathering information from answers
print(f"""
So, now you like me {likes}.
You are from {place}.
""")
#to run this program you should open command prompt and type python (this filename as saved).py (user name)
