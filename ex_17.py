from sys import argv
from os.path import exists
#now assigning the arguement variables
script, from_file, to_file=argv

#introducing the variables to print funct, by f
print(f"copying from {from_file} to {to_file}")

#doing this in one line
in_file = open("text.txt")
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")

print(f"does the output file exist? {exists(to_file)}")
print("ready, hit return to continue,ctrl-c to abort..")
#using input string to be answered by reader
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("alright,all done.")
out_file.close()
in_file.close()
#the file gets closed
#to execute this programme you should open cmd and type python {this file name} {from file} {to file}
