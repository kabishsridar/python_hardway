from sys import argv

#now assigning the argv value
script, input_file = argv
#now introducing the def funct. to read the file
def print_all(f):    
    print(f.read())
#now introducing the def funct. to rewind it
def rewind(f):    
    f.seek(0)
#now introducing def funct. to print only a line
def print_a_line(line_count,f):    
    print(line_count,f.readline())

current_file = open("text.txt")
#now using \n to line feed
print("first lets print whole file :\n")

print_all(current_file)

print("now lets rewind like kind of tape.")

rewind(current_file)

print("lets print three lines:")

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)
# to execute this programme open cmd and enter python {this file name} {file name to execute}
