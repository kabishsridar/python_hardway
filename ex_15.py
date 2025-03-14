from sys import argv

script , filename = argv
#now opening a file
txt=open(filename)

print(f"this is my file {filename}:")
#using txt.read to read the text in the file
print(txt.readline())

print("type the filename again:")
file_again = input(">")

txt_again = open (file_again)
txt_again.readline()
print(txt_again.readline())
#to execute the code you should open command prompt and type python {this file name}.py {another file name which to be readed}
