#defining the function
def songs_and_bikes(songs_count,no_of_bikes):    
    print(f"now we have {songs_count}songs !")
    print(f"there are {no_of_bikes}in godown!")
    print("this is enough for our ride")
#now feeding a line by \n
    print("get a blanket .\n")
#now intriducing the math values directly to print
print("giving the numbers directly")
songs_and_bikes(300,100)

print("now using variables in script")
songs_count=300
no_of_bikes=100

songs_and_bikes(songs_count,no_of_bikes)

print("using the math")
songs_and_bikes(180+120,25+75)

print("combining the two variables and math:")
songs_and_bikes(songs_count+200,no_of_bikes+400)