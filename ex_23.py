import sys
script,input_encoding,error  = sys.argv

#introducing def funct.
def main(language_file,encoding,errors):    
    line = language_file.readline()
    #now assigning the if statement
    if line:
       print_line(line,encoding,errors)
       return main(language_file,encoding,errors)
#introducing def funct.
def print_line(line,encoding,errors):    
    next_lang=line.strip()
    raw_bytes=next_lang.encode(encoding,errors=errors)
    cooked_string=raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes,"<==>",cooked_string)

languages = open("text.txt",encoding="utf-8")

main(languages,input_encoding,error)
#to execute this code open cmd and enter python {this file name} {language file name}
