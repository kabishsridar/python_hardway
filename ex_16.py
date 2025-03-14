from sys import argv

#now assigning arguements
script , filename = argv
#now introducing the filename

print(f"now we are going to erase the {filename}file.")
print("if you dont want hit CTRL-C (^c)")
print("if you dont want that, hit RETURN")

input(">")

print("opening the file....")
target = open( filename, 'w')
#now truncating or deleting the file
print("now truncatin or deleting the file...")
target.truncate()

print("now texting for three ;lines")

lin_1=input("lin_1: ")
lin_2 =input("lin_2: ")
lin_3 =input("lin_3: ")

print("i'm going to write these to the files")

target.write(lin_1)
target.write("\n")
target.write(lin_2)
target.write("\n")
target.write(lin_3)
target.write("\n")
#closing file
print("and  finally ,closing the file")
target.close()

print(f"We're going to read {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("> ")

print("Opening the file...")

txt = open(filename)
print(txt.read())
txt.close()
# to execute this code you should open cmd and enter python {this file name}.py {file name to be trncated and changed}
