#now assigning {} to formatter variable
formatter = "{} {} {} {}"

#now introducing formatter to print and using .format
print(formatter.format(1,2,3,4,))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("a","b","c","d"))  
print(formatter.format("apple","ball","cat","dog"))
print(formatter.format("p","c","l","t"))
print(formatter.format("personal","computer","laptop","tablet"))
