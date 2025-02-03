from sys import argv

script , filename = argv,argv
#now opening a file
txt=open(filename)

print(f"this is my file {filename}:")
#using txt.read to read the text in the file
print(txt.read())

print("type the filename again:")
file_again = input(">")

txt_again = open (file_again)

print(txt_again.read())